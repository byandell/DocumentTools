#!/usr/bin/env Rscript
# ==============================================================================
# scripts/render_rmd.R
#
# Automatically renders R Markdown (*.Rmd) documents across R/ sub-folders into
# self-contained GitHub Pages Markdown (*.md) files with base64 Data URIs for plots.
#
# Key Features:
# 1. Zero External Files: Sets knitr upload.fun to image_uri so all plots
#    (ggplot2, base R, igraph, lattice) are base64-inlined into the .md file.
# 2. Just-the-Docs Integration: Automatically adds Jekyll YAML frontmatter
#    (title, parent, grand_parent, nav_order) matching site hierarchy.
# 3. Interactive Widget Support: Compiles network_visNetwork.Rmd to self-contained
#    HTML (with interactive visNetwork JS) and generates a matching .md page.
# 4. Clean Artifact Hygiene: Removes any temporary figure/ folders after knitting.
#
# Usage:
#   Rscript scripts/render_rmd.R              # Render all 26 Rmd documents
#   Rscript scripts/render_rmd.R --file path  # Render a single document
# ==============================================================================

suppressPackageStartupMessages({
  library(knitr)
  library(rmarkdown)
})

# Manifest of all Rmd files with their Just-the-docs navigation metadata
rmd_manifest <- list(
  # --- R/curate/ (Parent: "Curate R Data", grand_parent: "R Language") ---
  list(path = "R/curate/data_tables.Rmd", title = "Working with Data in R",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 1),
  list(path = "R/curate/applyExample.Rmd", title = "Examples Using for and apply",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 2),
  list(path = "R/curate/intro_dplyr.Rmd", title = "Intro to R Adapted to dplyr",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 3),
  list(path = "R/curate/tidyverse.Rmd", title = "Tidyverse Split-Apply-Combine Example",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 4),
  list(path = "R/curate/purrr.Rmd", title = "purrr Package Example",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 5),
  list(path = "R/curate/species.Rmd", title = "Species Analysis with dplyr and purrr",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 6),
  list(path = "R/curate/string.Rmd", title = "Characters and Strings",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 7),
  list(path = "R/curate/regex.Rmd", title = "Regular Expressions (regex)",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 8),
  list(path = "R/curate/file.Rmd", title = "Reading and Writing Files",
       parent = "Curate R Data", grand_parent = "R Language", nav_order = 9),

  # --- R/analyze/ (Parent: "Analyze Data", grand_parent: "R Language") ---
  list(path = "R/analyze/correlate.Rmd", title = "Correlation Analysis",
       parent = "Analyze Data", grand_parent = "R Language", nav_order = 1),
  list(path = "R/analyze/covary.Rmd", title = "Covariation Analysis",
       parent = "Analyze Data", grand_parent = "R Language", nav_order = 2),
  list(path = "R/analyze/linear_model.Rmd", title = "Linear Models",
       parent = "Analyze Data", grand_parent = "R Language", nav_order = 3),
  list(path = "R/analyze/Formulas.Rmd", title = "Formulas for Linear Models",
       parent = "Analyze Data", grand_parent = "R Language", nav_order = 4),

  # --- R/organize/ (Parent: "Organize Data & Docs", grand_parent: "R Language") ---
  list(path = "R/organize/RmarkdownExample.Rmd", title = "R Markdown Example",
       parent = "Organize Data & Docs", grand_parent = "R Language", nav_order = 1),
  list(path = "R/organize/function.Rmd", title = "R Functions",
       parent = "Organize Data & Docs", grand_parent = "R Language", nav_order = 2),
  list(path = "R/organize/SQLiteDplyr.Rmd", title = "SQLite and dplyr",
       parent = "Organize Data & Docs", grand_parent = "R Language", nav_order = 3),
  list(path = "R/organize/package.Rmd", title = "R Packages",
       parent = "Organize Data & Docs", grand_parent = "R Language", nav_order = 4),

  # --- R/profile/ (Parent: "Profile & Simulate", grand_parent: "R Language") ---
  list(path = "R/profile/profile.Rmd", title = "Profiling R Code",
       parent = "Profile & Simulate", grand_parent = "R Language", nav_order = 1),
  list(path = "R/profile/lineprof.Rmd", title = "Memory Profiling with lineprof",
       parent = "Profile & Simulate", grand_parent = "R Language", nav_order = 2),
  list(path = "R/profile/simulate.Rmd", title = "Simulation Studies in R",
       parent = "Profile & Simulate", grand_parent = "R Language", nav_order = 3),

  # --- R/visualize/ (Parent: "Visualize Data with R", grand_parent: "R Language") ---
  list(path = "R/visualize/ggplot2.Rmd", title = "ggplot2 Visualization",
       parent = "Visualize Data with R", grand_parent = "R Language", nav_order = 1),
  list(path = "R/visualize/shiny.Rmd", title = "Shiny Web Applications",
       parent = "Visualize Data with R", grand_parent = "R Language", nav_order = 2),

  # --- R/visualize/network/ (Parent: "Network Observatins in Connected Graphs") ---
  list(path = "R/visualize/network/network_data.Rmd", title = "Network Data Preparation",
       parent = "Network Observatins in Connected Graphs", grand_parent = "Visualize Data with R", nav_order = 1),
  list(path = "R/visualize/network/network_igraph.Rmd", title = "igraph Network Visualization (Dataset 1)",
       parent = "Network Observatins in Connected Graphs", grand_parent = "Visualize Data with R", nav_order = 2),
  list(path = "R/visualize/network/network2_igraph.Rmd", title = "igraph Network Visualization (Dataset 2)",
       parent = "Network Observatins in Connected Graphs", grand_parent = "Visualize Data with R", nav_order = 3),
  list(path = "R/visualize/network/network_visNetwork.Rmd", title = "visNetwork Interactive Visualization",
       parent = "Network Observatins in Connected Graphs", grand_parent = "Visualize Data with R", nav_order = 4)
)

# Parse command line args
args <- commandArgs(trailingOnly = TRUE)
target_filter <- NULL
if (length(args) > 0) {
  if (args[1] == "--file" && length(args) >= 2) {
    target_filter <- args[2]
  } else if (!startsWith(args[1], "-")) {
    target_filter <- args[1]
  }
}

if (!is.null(target_filter)) {
  rmd_manifest <- Filter(function(item) grepl(target_filter, item$path, fixed = TRUE), rmd_manifest)
  if (length(rmd_manifest) == 0) {
    stop(sprintf("No matching file found for pattern: %s", target_filter))
  }
}

root_dir <- getwd()
cat(sprintf("Starting render for %d Rmd file(s)...\n\n", length(rmd_manifest)))

render_file <- function(item, root_dir) {
  rel_path <- item$path
  base_name <- basename(rel_path)
  sub_dir <- dirname(rel_path)
  out_md_name <- sub("\\.Rmd$", ".md", base_name)
  out_md_path <- file.path(sub_dir, out_md_name)
  
  cat(sprintf("[Rendering] %s -> %s ... ", rel_path, out_md_path))
  
  # Special handling for visNetwork interactive HTML widget
  is_visnetwork <- grepl("network_visNetwork\\.Rmd$", rel_path)
  
  result <- tryCatch({
    setwd(file.path(root_dir, sub_dir))
    
    # Configure knitr to base64 encode all figures directly into markdown
    opts_knit$set(upload.fun = image_uri)
    opts_chunk$set(
      echo = TRUE,
      warning = FALSE,
      message = FALSE,
      fig.width = 7,
      fig.height = 5
    )
    
    tmp_out <- tempfile(fileext = ".md")
    
    # Knit Rmd to markdown
    knit(base_name, tmp_out, quiet = TRUE)
    
    # Clean up temporary figure/ directory left by knitr
    if (dir.exists("figure")) {
      unlink("figure", recursive = TRUE)
    }
    
    # If interactive visNetwork, also render standalone self-contained HTML
    if (is_visnetwork) {
      suppressMessages(rmarkdown::render(
        base_name,
        output_format = "html_document",
        output_file = "network_visNetwork.html",
        output_options = list(self_contained = TRUE),
        quiet = TRUE
      ))
    }
    
    # Read knitted content
    lines <- readLines(tmp_out, warn = FALSE)
    
    # Strip existing YAML frontmatter if present
    if (length(lines) > 0 && lines[1] == "---") {
      end_yaml <- which(lines[-1] == "---")
      if (length(end_yaml) > 0) {
        lines <- lines[-(1:(end_yaml[1] + 1))]
      }
    }
    
    # Trim leading empty lines
    while (length(lines) > 0 && grepl("^\\s*$", lines[1])) {
      lines <- lines[-1]
    }
    
    # Construct clean Just-the-Docs YAML frontmatter
    yaml_header <- c(
      "---",
      sprintf('title: "%s"', item$title),
      sprintf('parent: "%s"', item$parent),
      sprintf('grand_parent: "%s"', item$grand_parent),
      sprintf('nav_order: %d', item$nav_order),
      "---",
      ""
    )
    
    # Ensure there is an # H1 Title tag at top of body
    has_h1 <- any(grepl("^#\\s+", lines[1:min(length(lines), 5)]))
    body_header <- if (!has_h1) {
      c(sprintf("# %s", item$title), "")
    } else {
      character(0)
    }
    
    # For interactive visNetwork, add banner link to the standalone interactive HTML
    vis_banner <- if (is_visnetwork) {
      c(
        "> **Interactive Widget**: An interactive version of this network visualization is available at [Open Interactive Visualization](network_visNetwork.html).",
        ""
      )
    } else {
      character(0)
    }
    
    final_content <- c(yaml_header, body_header, vis_banner, lines)
    writeLines(final_content, out_md_name)
    
    plots_count <- sum(grepl("data:image", final_content))
    file_bytes <- file.size(out_md_name)
    
    cat(sprintf("DONE (%d plots, %s)\n", plots_count, format(file_bytes, big.mark = ",")))
    list(
      file = rel_path,
      out = out_md_path,
      status = "SUCCESS",
      plots = plots_count,
      bytes = file_bytes
    )
    
  }, error = function(e) {
    cat(sprintf("ERROR: %s\n", conditionMessage(e)))
    list(
      file = rel_path,
      out = out_md_path,
      status = "ERROR",
      plots = 0,
      bytes = 0,
      msg = conditionMessage(e)
    )
  }, finally = {
    setwd(root_dir)
  })
  
  return(result)
}

results <- lapply(rmd_manifest, render_file, root_dir = root_dir)

cat("\n======================================================================\n")
cat("RENDERING SUMMARY\n")
cat("======================================================================\n")
cat(sprintf("%-42s | %-8s | %-6s | %-10s\n", "Output File", "Status", "Plots", "Size"))
cat(paste(rep("-", 72), collapse = ""), "\n")
for (i in seq_along(results)) {
  res <- results[[i]]
  cat(sprintf("%-42s | %-8s | %-6d | %-10s\n",
              res$out, res$status, res$plots, format(res$bytes, big.mark = ",")))
}
cat("======================================================================\n")
