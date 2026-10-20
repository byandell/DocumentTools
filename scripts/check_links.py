#!/usr/bin/env python3
"""
External Link Checker Utility
Scans markdown (.md), Quarto (.qmd), and R Markdown (.Rmd) files for HTTP/HTTPS links
and verifies their validity in parallel.
"""

import os
import re
import sys
import argparse
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

# Default settings
DEFAULT_TIMEOUT = 10
DEFAULT_THREADS = 16
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# Regex to extract URLs starting with http or https
URL_REGEX = re.compile(r'https?://[^\s<>"\']+')

def parse_args():
    parser = argparse.ArgumentParser(
        description="Scan and verify external links in Markdown, Quarto, and R Markdown files."
    )
    parser.add_argument(
        "--dir", "-d",
        default=".",
        help="Root directory to search for documentation files (default: current directory)"
    )
    parser.add_argument(
        "--threads", "-t",
        type=int,
        default=DEFAULT_THREADS,
        help=f"Number of parallel request threads (default: {DEFAULT_THREADS})"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds (default: {DEFAULT_TIMEOUT})"
    )
    parser.add_argument(
        "--ignore-ssl",
        action="store_true",
        help="Ignore SSL certificate errors"
    )
    parser.add_argument(
        "--report", "-r",
        default="link_check_report.md",
        help="Path to save the markdown report (default: link_check_report.md)"
    )
    parser.add_argument(
        "--file", "-f",
        help="Scan only a specific file instead of scanning the whole directory"
    )
    parser.add_argument(
        "--wayback-year",
        type=int,
        help="Find historical snapshots close to the specified year (e.g. 2017) using the Wayback Machine Availability API."
    )
    return parser.parse_args()

def scan_files(root_dir, extensions):
    """Finds all files in root_dir with matching extensions, ignoring hidden directories."""
    matched_files = []
    for root, dirs, files in os.walk(root_dir):
        # Exclude hidden directories (like .git, .quarto, etc.)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                matched_files.append(os.path.join(root, file))
    return sorted(matched_files)

def clean_url(url):
    """Cleans up trailing punctuation and balances unmatched parentheses/brackets."""
    # Strip trailing punctuation and markdown formatting characters
    while url and url[-1] in '.,;:!?)]}*_`~':
        char = url[-1]
        if char == ')':
            # Only stop stripping if the URL has balanced opening parentheses
            if url.count('(') >= url.count(')'):
                break
        elif char == ']':
            if url.count('[') >= url.count(']'):
                break
        elif char == '}':
            if url.count('{') >= url.count('}'):
                break
        url = url[:-1]
    return url

def extract_links(file_path):
    """Parses a file and extracts all valid external HTTP/HTTPS links with line numbers."""
    extracted = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f, 1):
                # Simple markdown link format check or general URL regex
                for match in URL_REGEX.finditer(line):
                    url = clean_url(match.group(0))
                    try:
                        parsed = urllib.parse.urlparse(url)
                    except ValueError:
                        continue
                    # Ignore empty host, localhost, loopback IP, or local paths
                    if not parsed.netloc or parsed.netloc in ("localhost", "127.0.0.1"):
                        continue
                    extracted.append({
                        "file": file_path,
                        "line": line_num,
                        "url": url
                    })
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    return extracted

def check_link(url, timeout, ignore_ssl):
    """Checks the validity of a URL: tries HEAD first, falls back to GET on failure."""
    headers = {"User-Agent": DEFAULT_USER_AGENT}
    verify = not ignore_ssl

    # 1. Try HEAD request first (faster, saves bandwidth)
    try:
        response = requests.head(url, headers=headers, timeout=timeout, allow_redirects=True, verify=verify)
        if response.status_code < 400:
            return True, response.status_code, None
    except Exception:
        # Fall back to GET below
        pass

    # 2. Try GET request (stream=True avoids downloading entire body)
    try:
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True, verify=verify, stream=True)
        if response.status_code < 400:
            return True, response.status_code, None
        return False, response.status_code, f"HTTP Status {response.status_code}"
    except requests.exceptions.Timeout:
        return False, None, "Timeout"
    except requests.exceptions.SSLError as e:
        return False, None, f"SSL Certificate Error: {e}"
    except requests.exceptions.ConnectionError:
        return False, None, "Connection Error"
    except Exception as e:
        return False, None, f"Error: {str(e)}"

def get_wayback_snapshot(url, year, timeout=5):
    """Queries the Wayback Machine Availability API for a snapshot from a given year."""
    api_url = f"https://archive.org/wayback/available?url={url}&timestamp={year}0101"
    headers = {"User-Agent": DEFAULT_USER_AGENT}
    try:
        r = requests.get(api_url, headers=headers, timeout=timeout)
        if r.status_code == 200:
            data = r.json()
            snapshots = data.get("archived_snapshots", {})
            if "closest" in snapshots and snapshots["closest"].get("available"):
                return snapshots["closest"].get("url")
    except Exception:
        pass
    return None

def run_checker():
    args = parse_args()
    extensions = [".md", ".qmd", ".Rmd"]

    if args.file:
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        files = [args.file]
    else:
        print(f"Scanning directory '{args.dir}' for {', '.join(extensions)} files...")
        files = scan_files(args.dir, extensions)

    print(f"Found {len(files)} files to scan.")
    
    # Extract all links
    all_occurrences = []
    unique_urls = set()
    for file in files:
        file_links = extract_links(file)
        all_occurrences.extend(file_links)
        for item in file_links:
            unique_urls.add(item["url"])

    print(f"Found {len(all_occurrences)} external link references ({len(unique_urls)} unique URLs).")
    if not unique_urls:
        print("No external links found.")
        sys.exit(0)

    # Check links in parallel
    print(f"Verifying {len(unique_urls)} unique URLs with {args.threads} threads...")
    results = {}
    
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_url = {
            executor.submit(check_link, url, args.timeout, args.ignore_ssl): url 
            for url in unique_urls
        }
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                success, status_code, error_msg = future.result()
                results[url] = {
                    "success": success,
                    "status_code": status_code,
                    "error_msg": error_msg
                }
            except Exception as e:
                results[url] = {
                    "success": False,
                    "status_code": None,
                    "error_msg": f"Unhandled Exception: {str(e)}"
                }

    # Group occurrences into successful/broken
    broken_occurrences = []
    success_count = 0
    broken_count = 0

    for occ in all_occurrences:
        url = occ["url"]
        res = results[url]
        if res["success"]:
            success_count += 1
        else:
            broken_count += 1
            broken_occurrences.append({
                "file": occ["file"],
                "line": occ["line"],
                "url": url,
                "status_code": res["status_code"],
                "error": res["error_msg"]
            })

    # Output Console Summary
    print("\n" + "="*50)
    print("LINK CHECKER SUMMARY")
    print("="*50)
    print(f"Files scanned:         {len(files)}")
    print(f"Total URL references:  {len(all_occurrences)}")
    print(f"Unique URLs checked:   {len(unique_urls)}")
    print(f"Successful references: {success_count}")
    print(f"Broken references:     {broken_count}")
    print("="*50)

    # Fetch Wayback Machine snapshots if requested
    wayback_links = {}
    if args.wayback_year and broken_count > 0:
        broken_unique_urls = {item["url"] for item in broken_occurrences}
        print(f"Querying Wayback Machine for snapshots from {args.wayback_year} for {len(broken_unique_urls)} broken URLs...")
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            future_to_url = {
                executor.submit(get_wayback_snapshot, url, args.wayback_year, args.timeout): url
                for url in broken_unique_urls
            }
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    wb_url = future.result()
                    if wb_url:
                        wayback_links[url] = wb_url
                except Exception as e:
                    print(f"Failed to fetch Wayback snapshot for {url}: {e}", file=sys.stderr)

    # Generate Markdown Report
    if broken_count > 0:
        print(f"\nFound {broken_count} broken link references. Generating report...")
        try:
            with open(args.report, "w", encoding="utf-8") as rf:
                rf.write("# External Link Checker Report\n\n")
                rf.write(f"This report lists all broken external links found in the repository.\n\n")
                rf.write("## Summary Statistics\n\n")
                rf.write(f"- **Files Scanned**: {len(files)}\n")
                rf.write(f"- **Total References**: {len(all_occurrences)}\n")
                rf.write(f"- **Unique URLs**: {len(unique_urls)}\n")
                rf.write(f"- **Working Links**: {success_count}\n")
                rf.write(f"- **Broken Links**: {broken_count}\n\n")
                
                rf.write("## Broken Link Reference Details\n\n")
                if args.wayback_year:
                    rf.write(f"| File | Line | Broken Link URL | Status Code / Error | Wayback {args.wayback_year} Link |\n")
                    rf.write("| :--- | :--- | :--- | :--- | :--- |\n")
                else:
                    rf.write("| File | Line | Broken Link URL | Status Code / Error |\n")
                    rf.write("| :--- | :--- | :--- | :--- |\n")
                
                # Sort broken references by file and line
                sorted_broken = sorted(broken_occurrences, key=lambda x: (x["file"], x["line"]))
                for item in sorted_broken:
                    rel_path = os.path.relpath(item["file"], args.dir)
                    # Create markdown link to file if possible (local syntax)
                    status_desc = f"{item['status_code']}" if item['status_code'] else f"{item['error']}"
                    if args.wayback_year:
                        wb_url = wayback_links.get(item['url'])
                        wb_link_md = f"[Wayback Snapshot]({wb_url})" if wb_url else "N/A"
                        rf.write(f"| [{rel_path}]({rel_path}#L{item['line']}) | {item['line']} | `{item['url']}` | {status_desc} | {wb_link_md} |\n")
                    else:
                        rf.write(f"| [{rel_path}]({rel_path}#L{item['line']}) | {item['line']} | `{item['url']}` | {status_desc} |\n")
            
            print(f"Markdown report generated: {args.report}")
        except Exception as e:
            print(f"Failed to write markdown report: {e}", file=sys.stderr)
        
        # Exit with error code if there are broken links
        sys.exit(1)
    else:
        print("\nAll external links are valid and active!")
        # Clean up old report if it exists
        if os.path.exists(args.report):
            try:
                os.remove(args.report)
            except Exception:
                pass
        sys.exit(0)

if __name__ == "__main__":
    run_checker()
