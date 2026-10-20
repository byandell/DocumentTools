---
title: "Check External Links"
parent: "Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 10
---

# Check External Links

This was developed to maintain the integrity of external links across the repository's documentation. Since the documentation site references many third-party tools, tutorials, packages, and research papers, it is essential to periodically scan all files and verify that these references are still valid and active.

The process parses all `.md`, `.qmd`, and `.Rmd` files, extracts HTTP/HTTPS URLs, cleans formatting and punctuation (including nested parentheses in Wikipedia links), and runs parallel network checks to identify dead or misconfigured links.
See
[Broken Links Summary](./broken_links.md)
for current status.

**Use**:
Run the script directly on the terminal to check external links across the repo. If you want an AI agent to check links, improve the tool, or scan specific files, use the prompt below.

**Prompt**:
"Use the link checker in
[scripts/check_links.py](../scripts/check_links.py)
to scan all documentation files (`.md`, `.qmd`, `.Rmd`) for broken links, or run `python3 scripts/check_links.py` to identify any broken URLs and check the generated report."

---

**Goal**: Extract and verify the validity of all external HTTP/HTTPS links in the repository.

**Instructions**:

1. **Scans Documentation files**:
   - Recursively search the repository for `.md` (Markdown), `.qmd` (Quarto), and `.Rmd` (R Markdown) files.
   - Skip hidden directories like `.git`, `.quarto`, `.Rproj.user`, and output dirs like `_site` or `site_libs`.

2. **Extracts and Cleans URLs**:
   - Identify all strings starting with `http://` or `https://`.
   - Clean trailing punctuation (`.`, `,`, `:`, `;`, `!`) and markdown formatting characters (`_`, `*`, `` ` ``, `~`).
   - Intelligently balance brackets/parentheses to correctly extract links containing parentheses (like Wikipedia pages: `https://en.wikipedia.org/wiki/R_(programming_language)`).
   - Ignore internal links, anchor hashes, and localhost domains (`localhost`, `127.0.0.1`).

3. **Verifies URLs in Parallel**:
   - Send requests concurrently using Python's `ThreadPoolExecutor` to speed up checking across thousands of URLs.
   - First, try an HTTP `HEAD` request with a custom web browser `User-Agent` (to prevent bot blocking).
   - If the `HEAD` request fails or returns a status code $\ge 400$, fall back to a `GET` request (using `stream=True` to avoid downloading full page bodies).
   - Classify responses with status codes $< 400$ as successful. Flag timeouts, connection issues, SSL errors, and status codes $\ge 400$ as broken.

4. **Outputs Results**:
   - Print a terminal summary of scan statistics.
   - If any broken links are found, write a detailed table in `link_check_report.md` detailing the file, line number, URL, status code or connection error, and optionally the Wayback Machine snapshot link if `--wayback-year` was specified.
   - Exit with code `1` if broken links exist, or code `0` if all links are working.

## Execution Guide

To run the link checker manually, execute the following command in the workspace root:

```bash
python3 scripts/check_links.py
```

### Advanced Usage

- **Check a single file**:

  ```bash
  python3 scripts/check_links.py --file README.md
  ```

- **Ignore SSL certificate errors** (useful if sites have expired certs but are otherwise active):

  ```bash
  python3 scripts/check_links.py --ignore-ssl
  ```

- **Increase/Decrease parallel threads** (default is 16):

  ```bash
  python3 scripts/check_links.py --threads 30
  ```

- **Set a custom timeout** (default is 10 seconds):

  ```bash
  python3 scripts/check_links.py --timeout 5
  ```

- **Specify a custom report output path**:

  ```bash
  python3 scripts/check_links.py --report custom_report.md
  ```

- **Fetch historical snapshots from the Wayback Machine**:
  To look up Wayback snapshots close to a specific year (e.g. 2017) for all broken links and append them as a column in the report:

  ```bash
  python3 scripts/check_links.py --wayback-year 2017
  ```

### Report Location

The report `link_check_report.md` is automatically created in the repository root if there are broken links. It is added to `.gitignore` so it will not be checked into Git commits.

## Addressing Broken Links

Here is a structured strategy for addressing the broken links identified in the file `link_check_report.md`. We can categorize them by the root cause and handle them accordingly:

### 1. Structure/Slug Changes (404 Not Found)

Many websites reorganize their documentation, causing old paths to break.

- **Examples from report**:
  - `https://www.promptingguide.ai/introduction/what-is-prompt-engineering` $\rightarrow$ now located at `https://www.promptingguide.ai/introduction` or `https://www.promptingguide.ai/basics/prompting`.
  - `https://esiil.org/working_groups` $\rightarrow$ renamed to use a hyphen: `https://esiil.org/working-groups`.
- **Fix**: Search the root domain of the site to locate the new path, then update the target file.

### 2. Scraping Block / Bot Prevention (403 Forbidden)

Some servers (e.g., Columbia University's `~gelman` directory) actively block programmatic/headless requests to prevent scraping, returning a `403 Forbidden` status even though the page works perfectly in a browser.

- **Fix**: Verify them manually in a browser. If they work, they do not need to be updated.
- **Enhancement**: We can update [check_links.py](file:///Users/brianyandell/Documents/GitHub/Documentation/scripts/check_links.py) to support an **Allowlist/Ignore List** for specific domains (like `columbia.edu` or `mcmaster.ca`) so they are skipped in future scans.

### 3. Expired or Misconfigured SSL Certificates

Links like `https://docs.cursor.sh/mcp` fail verification due to certificate expiry or custom domain configurations.

- **Fix**: Run the link checker with SSL verification disabled to see if the link is otherwise responsive:

  ```bash
  python3 scripts/check_links.py --ignore-ssl
  ```

  If it succeeds, the link is alive and can be left as-is.

### 4. Permanently Dead / Removed Content

Some tutorial files or academic papers (e.g., `http://www.stat.columbia.edu/~martin/W2024/R10.pdf`) may have been deleted or archived by their authors.

- **Fix Options**:
  - Check the `Wayback {Year} Link` column in `link_check_report.md` (generated by passing `--wayback-year` to the link checker) to find a working historical snapshot. If available, you can replace the broken link in the source document with this archive URL.
  - Search GitHub or Google for another host/mirror of the same document.
  - Replace the link with a newer, equivalent reference.

## Annotating Broken Links with Warning Glyphs

To make broken links visually identifiable to readers of the documentation site, you can append a warning glyph (like `⚠️`) to all broken URLs in the repository.

A utility script [add_glyphs.py](../scripts/add_glyphs.py) is provided to automate this:

```bash
python3 scripts/add_glyphs.py
```

### How it Works

1. Parses `link_check_report.md` to locate the files, line numbers, and broken URLs.
2. Appends a yellow warning sign glyph (`⚠️`) directly to each broken URL's location.
3. Automatically inserts the glyph **outside** the markdown link parenthesis (i.e. `[Link text](url) ⚠️` or `<url> ⚠️`) to keep the markdown structural validity intact.
4. Safely handles multiple broken URLs on a single line by modifying them from right to left.
5. Is idempotent and prevents adding duplicate glyphs on subsequent runs.

---

### How we can proceed

If you want to start updating these, you can instruct me to fix a specific file or folder. For example:
> *"Help me fix the broken links in [AI/prompt.md](../AI/prompt.md) and [AI/env.md](../AI/env.md)"*

I will then use web search to find the correct active URLs, verify them, and update the markdown files directly.

---

## Broken Links Audit Summary

Below is the summary of link check results across all documentation files generated by `scripts/check_links.py`.

### Link Statistics by Folder (Summed across files)

| Folder | Unique Broken Links | Total Unique Links | % Broken |
| :--- | :---: | :---: | :---: |
| `(root)/` | 107 | 746 | 14.3% |
| `AI/` | 23 | 190 | 12.1% |
| `R/analyze/` | 4 | 28 | 14.3% |
| `R/connect/` | 218 | 544 | 40.1% |
| `R/curate/` | 17 | 78 | 21.8% |
| `R/learn/` | 27 | 147 | 18.4% |
| `R/organize/` | 8 | 58 | 13.8% |
| `R/profile/` | 1 | 8 | 12.5% |
| `R/visualize/` | 43 | 155 | 27.7% |
| `R/visualize/network/` | 1 | 3 | 33.3% |
| `datasci/` | 41 | 92 | 44.6% |
| `envsys/` | 6 | 108 | 5.6% |
| `github/` | 6 | 61 | 9.8% |
| `prompts/` | 2 | 33 | 6.1% |
| `python/` | 15 | 162 | 9.3% |
| `quarto/` | 32 | 235 | 13.6% |

---

### Detailed Link Statistics by File

| Folder | File | Unique Broken Links | Total Unique Links | % Broken |
| :--- | :--- | :---: | :---: | :---: |
| `(root)/` | [README.md](../README.md) | 2 | 38 | 5.3% |
| `shiny/` | [README.md](../shiny/README.md) | 103 | 152 | 67.8% |
| `(root)/` | [link_check_report.md](../link_check_report.md) | 2 | 556 | 0.4% |
| `AI/` | [LLM.md](../AI/LLM.md) | 1 | 24 | 4.2% |
| `AI/` | [README.md](../AI/README.md) | 9 | 49 | 18.4% |
| `AI/` | [context.md](../AI/context.md) | 1 | 35 | 2.9% |
| `AI/` | [env.md](../AI/env.md) | 10 | 60 | 16.7% |
| `AI/` | [prompt.md](../AI/prompt.md) | 2 | 22 | 9.1% |
| `R/analyze/` | [linear_model.md](../R/analyze/linear_model.md) | 4 | 28 | 14.3% |
| `R/connect/` | [README.md](../R/connect/README.md) | 2 | 11 | 18.2% |
| `R/connect/` | [beyondR.md](../R/connect/beyondR.md) | 5 | 24 | 20.8% |
| `R/connect/` | [blended_online.md](../R/connect/blended_online.md) | 80 | 184 | 43.5% |
| `R/connect/` | [docker.md](../R/connect/docker.md) | 3 | 9 | 33.3% |
| `R/connect/` | [latex.md](../R/connect/latex.md) | 5 | 16 | 31.2% |
| `R/connect/` | [linux.md](../R/connect/linux.md) | 7 | 20 | 35.0% |
| `R/connect/` | [nontrad.md](../R/connect/nontrad.md) | 2 | 7 | 28.6% |
| `R/connect/` | [profSkills.md](../R/connect/profSkills.md) | 3 | 8 | 37.5% |
| `R/connect/` | [programs.md](../R/connect/programs.md) | 40 | 79 | 50.6% |
| `R/connect/` | [reproducible.md](../R/connect/reproducible.md) | 44 | 104 | 42.3% |
| `R/connect/` | [scaling_up.md](../R/connect/scaling_up.md) | 5 | 25 | 20.0% |
| `R/connect/` | [software.md](../R/connect/software.md) | 8 | 10 | 80.0% |
| `R/connect/` | [stat692notes.md](../R/connect/stat692notes.md) | 4 | 25 | 16.0% |
| `R/connect/` | [writing.md](../R/connect/writing.md) | 10 | 22 | 45.5% |
| `R/curate/` | [data_tables.md](../R/curate/data_tables.md) | 9 | 55 | 16.4% |
| `R/curate/` | [file.md](../R/curate/file.md) | 1 | 3 | 33.3% |
| `R/curate/` | [intro_dplyr.md](../R/curate/intro_dplyr.md) | 1 | 4 | 25.0% |
| `R/curate/` | [purrr.md](../R/curate/purrr.md) | 1 | 3 | 33.3% |
| `R/curate/` | [regex.md](../R/curate/regex.md) | 2 | 7 | 28.6% |
| `R/curate/` | [string.md](../R/curate/string.md) | 3 | 6 | 50.0% |
| `R/learn/` | [Bates.md](../R/learn/Bates.md) | 1 | 14 | 7.1% |
| `R/learn/` | [README.md](../R/learn/README.md) | 2 | 16 | 12.5% |
| `R/learn/` | [background.md](../R/learn/background.md) | 1 | 14 | 7.1% |
| `R/learn/` | [learnR.md](../R/learn/learnR.md) | 15 | 53 | 28.3% |
| `R/learn/` | [reference.md](../R/learn/reference.md) | 6 | 35 | 17.1% |
| `R/learn/` | [syllabus.md](../R/learn/syllabus.md) | 2 | 15 | 13.3% |
| `R/organize/` | [RmarkdownExample.md](../R/organize/RmarkdownExample.md) | 1 | 1 | 100.0% |
| `R/organize/` | [SQLiteDplyr.md](../R/organize/SQLiteDplyr.md) | 1 | 8 | 12.5% |
| `R/organize/` | [function.md](../R/organize/function.md) | 3 | 26 | 11.5% |
| `R/organize/` | [package.md](../R/organize/package.md) | 3 | 23 | 13.0% |
| `R/profile/` | [README.md](../R/profile/README.md) | 1 | 8 | 12.5% |
| `R/visualize/` | [README.md](../R/visualize/README.md) | 10 | 30 | 33.3% |
| `R/visualize/` | [ggplot2.md](../R/visualize/ggplot2.md) | 13 | 41 | 31.7% |
| `R/visualize/` | [graphics.md](../R/visualize/graphics.md) | 13 | 40 | 32.5% |
| `R/visualize/` | [shiny.md](../R/visualize/shiny.md) | 7 | 44 | 15.9% |
| `R/visualize/network/` | [README.md](../R/visualize/network/README.md) | 1 | 3 | 33.3% |
| `datasci/` | [bigdata.md](../datasci/bigdata.md) | 27 | 50 | 54.0% |
| `datasci/` | [repositories.md](../datasci/repositories.md) | 14 | 42 | 33.3% |
| `envsys/` | [README.md](../envsys/README.md) | 2 | 48 | 4.2% |
| `envsys/` | [geospatial.md](../envsys/geospatial.md) | 4 | 60 | 6.7% |
| `github/` | [pages.md](../github/pages.md) | 1 | 32 | 3.1% |
| `github/` | [version.md](../github/version.md) | 3 | 26 | 11.5% |
| `prompts/` | [README.md](../prompts/README.md) | 1 | 30 | 3.3% |
| `prompts/` | [workflow.md](../prompts/workflow.md) | 1 | 3 | 33.3% |
| `python/` | [README.md](../python/README.md) | 13 | 138 | 9.4% |
| `python/` | [strategy.md](../python/strategy.md) | 2 | 24 | 8.3% |
| `quarto/` | [AI.qmd](../quarto/AI.qmd) | 12 | 78 | 15.4% |
| `quarto/` | [R.qmd](../quarto/R.qmd) | 1 | 16 | 6.2% |
| `quarto/` | [README.md](../quarto/README.md) | 5 | 22 | 22.7% |
| `quarto/` | [ShinyApps.qmd](../quarto/ShinyApps.qmd) | 7 | 27 | 25.9% |
| `quarto/` | [envsys.qmd](../quarto/envsys.qmd) | 5 | 57 | 8.8% |
| `quarto/` | [python.qmd](../quarto/python.qmd) | 2 | 35 | 5.7% |

*Note: The summary lists files that contain at least one broken link.*
