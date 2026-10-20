---
title: "Render R Markdown to GitHub Pages"
parent: "Prompt Examples"
nav_order: 13
---

# Render R Markdown to GitHub Pages

## Prompt and Response

**Prompt:**
> Sub-folders of `R/` have several `*.Rmd` files that are not properly rendered via GitHub Pages. Develop a plan to properly render them, noting that some pages have images (using `ggplot2`) while others may be simply calculations. The latter could be rendered "on the fly" as `*.md`, but the former may require rendering to `*.html`. However this is done, each rendered page should be complete and not require external files such as JSON or `*_files` folders.

**Response:**
I have analyzed the repository structure, developed a complete rendering strategy, and automated the process in [`scripts/render_rmd.R`](../scripts/render_rmd.R).

---

## 1. Architectural Strategy & Technical Context

GitHub Pages statically serves Jekyll markdown sites. When hosting R-based tutorials and exploratory documents (`*.Rmd`), several deployment challenges arise:

| Challenge | Issue on GitHub Pages | Solution |
| :--- | :--- | :--- |
| **No R Engine in Jekyll** | GitHub Pages' default Jekyll builder does not run R or `knitr`. Uncompiled `.Rmd` files are treated as raw text or ignored. | Pre-compile `.Rmd` documents locally into Markdown (`.md`) before pushing to GitHub. |
| **External Figure Folders** | Default `knitr` markdown rendering exports plots to a separate folder (e.g., `filename_files/figure-html/`), cluttering the repository. | Set `knitr::opts_knit$set(upload.fun = knitr::image_uri)` to encode all plots directly into `.md` as **base64 Data URIs** (`![plot](data:image/png;base64,...)`). |
| **Theme / Sidebar Collision** | Raw standalone `.html` files override Jekyll and bypass the `just-the-docs` theme layout (losing the sidebar, navigation, search bar, and CSS). | Render calculations and static plots to **Jekyll `.md`** pages with standard YAML frontmatter so they inherit the theme naturally. |
| **Interactive Widgets** | Interactive JavaScript libraries like `visNetwork` cannot execute as static PNGs in pure Markdown. | Compile interactive widgets to a standalone self-contained `.html` file (`self_contained = TRUE`) and pair it with a companion `.md` page linking to the live widget. |

---

## 2. Manifest of Rendered Sub-folders

The 26 `*.Rmd` documents across `R/` subfolders are organized into the following hierarchy:

### `R/curate/` (Parent: "Curate R Data")

- [`data_tables.md`](../R/curate/data_tables.md): Working with data tables in R (Calculations)
- [`applyExample.md`](../R/curate/applyExample.md): Examples using `for` and `apply` (Calculations)
- [`intro_dplyr.md`](../R/curate/intro_dplyr.md): Intro to R adapted to `dplyr` (Calculations)
- [`tidyverse.md`](../R/curate/tidyverse.md): Tidyverse split-apply-combine example (Calculations)
- [`purrr.md`](../R/curate/purrr.md): `purrr` example using `map` and `transpose` (Calculations)
- [`species.md`](../R/curate/species.md): Species analysis with `dplyr` and `purrr` (Calculations)
- [`string.md`](../R/curate/string.md): Character and string operations (Calculations)
- [`regex.md`](../R/curate/regex.md): Regular expressions (Calculations)
- [`file.md`](../R/curate/file.md): Reading and writing files (2 embedded plots)

### `R/analyze/` (Parent: "Analyze Data")

- [`correlate.md`](../R/analyze/correlate.md): Correlation analysis (5 embedded `ggplot2` plots)
- [`covary.md`](../R/analyze/covary.md): Covariation analysis (13 embedded `ggplot2` plots)
- [`linear_model.md`](../R/analyze/linear_model.md): Linear models overview (Calculations)
- [`Formulas.md`](../R/analyze/Formulas.md): Formulas for linear models (5 embedded lattice/base plots)

### `R/organize/` (Parent: "Organize Data & Docs")

- [`RmarkdownExample.md`](../R/organize/RmarkdownExample.md): R Markdown syntax and options (3 embedded plots)
- [`function.md`](../R/organize/function.md): Creating reusable functions (Calculations)
- [`SQLiteDplyr.md`](../R/organize/SQLiteDplyr.md): SQLite and `dplyr` database workflows (Calculations)
- [`package.md`](../R/organize/package.md): Building R packages (Calculations)

### `R/profile/` (Parent: "Profile & Simulate")

- [`profile.md`](../R/profile/profile.md): Profiling R code with `Rprof` and `profvis` (Calculations)
- [`lineprof.md`](../R/profile/lineprof.md): Memory profiling with `lineprof` (Calculations)
- [`simulate.md`](../R/profile/simulate.md): Simulation studies and speed benchmarks (Calculations)

### `R/visualize/` (Parent: "Visualize Data with R")

- [`ggplot2.md`](../R/visualize/ggplot2.md): `ggplot2` reference and links
- [`shiny.md`](../R/visualize/shiny.md): Shiny applications overview
- Sub-folder **`network/`** (Parent: "Network Observatins in Connected Graphs"):
  - [`network_data.md`](../R/visualize/network/network_data.md): Network dataset setup
  - [`network_igraph.md`](../R/visualize/network/network_igraph.md): `igraph` visualization (19 embedded network plots)
  - [`network2_igraph.md`](../R/visualize/network/network2_igraph.md): `igraph` bipartite graphs (Calculations)
  - [`network_visNetwork.md`](../R/visualize/network/network_visNetwork.md): `visNetwork` overview with link to standalone interactive HTML

---

## 3. Automation Script (`scripts/render_rmd.R`)

The rendering process is fully automated via [`scripts/render_rmd.R`](../scripts/render_rmd.R).

### Running the Script

Run from the repository root:

```bash
# Render all 26 Rmd documents across R/
Rscript scripts/render_rmd.R

# Or render a single target file
Rscript scripts/render_rmd.R --file correlate.Rmd
```

### Core Implementation Details

```r
suppressPackageStartupMessages({
  library(knitr)
  library(rmarkdown)
})

# Configure knitr to inline all plots directly into Markdown as base64 Data URIs
opts_knit$set(upload.fun = image_uri)
opts_chunk$set(
  echo = TRUE,
  warning = FALSE,
  message = FALSE,
  fig.width = 7,
  fig.height = 5
)

# Knit document to temporary file
knit(base_name, tmp_out, quiet = TRUE)

# Remove temporary figure/ directory to preserve artifact hygiene
if (dir.exists("figure")) {
  unlink("figure", recursive = TRUE)
}

# Prepend Just-the-Docs YAML frontmatter
yaml_header <- c(
  "---",
  sprintf('title: "%s"', item$title),
  sprintf('parent: "%s"', item$parent),
  sprintf('grand_parent: "%s"', item$grand_parent),
  sprintf('nav_order: %d', item$nav_order),
  "---",
  ""
)
```

---

## 4. Frontmatter & Navigation Standards

To ensure each rendered `.md` file appears correctly in the Just-the-Docs sidebar and breadcrumbs:

1. **Sub-folder Indices**: Each sub-folder `README.md` (e.g. `R/curate/README.md`) must include `has_children: true`.
2. **Rendered Files**: Each rendered `.md` file includes `parent` and `grand_parent: "R Language"`.
3. **Internal Links**: Links in `README.md` point directly to `.md` files rather than source `.Rmd` files.
