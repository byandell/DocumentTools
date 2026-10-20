---
title: "Create Guides"
parent: "Document Tools"
nav_order: 7
has_children: true
---

# Create Guides

User and Developer Guides are handy to provide help users and developers understand projects
by highlighting the features, functions and approaches.
In addition, `README.md`, `DEVELOPER.md` and `AGENTS.md` files are handy for overviews.

## Table of Contents

- [Digital Tool Guides & Prompts](#digital-tool-guides--prompts)
  - [Prompts](#prompts)
  - [Guides and Overviews](#guides-and-overviews)
- [DocumentTools Repo Developer Guide](#documenttools-repo-developer-guide)
  - [Site Layout & Directory Map](#site-layout--directory-map)
  - [Page Metadata & Frontmatter Standards](#page-metadata--frontmatter-standards)
  - [Automation & Link Checking](#automation--link-checking)
  - [DEVELOPER.md vs Full Developer Guide](#developermd-vs-full-developer-guide)
- Additional Pages
  - [Developer Architecture & Maintenance Guide (`DEVELOPER.md`)](DEVELOPER.md)
  - [Create Developer Guides (Blueprint)](../prompts/devel_guide.md)
    - [Create Developer Guide to `qtl2shiny` (Reference Case Study)](../prompts/devel_guide_qtl2shiny.md)

---

## Digital Tool Guides & Prompts

### Prompts

- [Create Developer Guides (Blueprint)](prompts/devel_guide.md)
- [Create Developer Guide to `qtl2shiny` (Reference Case Study)](prompts/devel_guide_qtl2shiny.md)
- [Use `pkgdown` to Auto-Build GitHub Website](github/pkgdown.md)

### Guides and Overviews

| Project / Repository | Architecture (`DEVELOPER.md`) | Developer & User Guides | AI Agent Rules (`AGENTS.md`) |
| :--- | :--- | :--- | :--- |
| **[DocumentTools](https://byandell.github.io/DocumentTools)** (`this repo`) | [`DEVELOPER.md`](DEVELOPER.md) | [Developer Guide](#documenttools-repo-developer-guide) | [`AGENTS.md`](AGENTS.md) |
| **[`qtl2shiny`](https://byandell-sysgen.github.io/qtl2shiny/)** | [`DEVELOPER.md`](https://github.com/byandell-sysgen/qtl2shiny/blob/main/DEVELOPER.md) | [Developer Guide](https://byandell-sysgen.github.io/qtl2shiny/articles/devel_guide/index.html) ([Articles](https://byandell-sysgen.github.io/qtl2shiny/articles/)) | [`AGENTS.md`](https://github.com/byandell-sysgen/qtl2shiny/blob/main/AGENTS.md) |
| **[`geyser`](https://byandell.github.io/geyser/)** | [DEVELOPER.md](https://byandell.github.io/geyser/DEVELOPER.html) | [R Developer Guide](https://byandell.github.io/geyser/vignettes/DeveloperGuide.html)<br/>[Python Developer Guide](https://byandell.github.io/geyser/docs/devel/python.html) | [`AGENTS.md`](https://github.com/byandell/geyser/blob/main/AGENTS.md) |
| **[`landmapyr`](https://byandell-envsys.github.io/landmapyr/)** | [`DEVELOPER.md`](https://github.com/byandell-envsys/landmapyr/blob/main/DEVELOPER.md) | — | [`AGENTS.md`](https://github.com/byandell-envsys/landmapyr/blob/main/AGENTS.md) |
| **[`rainDrought`](https://byandell.github.io/rainDrought/)** | [DEVELOPER.md](https://byandell.github.io/rainDrought/DEVELOPER.html) | [User Guide](https://byandell.github.io/rainDrought/user_guide.html) | [AGENTS.md](https://byandell.github.io/rainDrought/AGENTS.md) |
| **[`byandell-sysgen`](https://byandell-sysgen.github.io/)** | [`DEVELOPER.md`](https://github.com/byandell-sysgen/.github/blob/main/DEVELOPER.md) | — | - |

---

## DocumentTools Repo Developer Guide

This section serves as the developer guide for managing, editing, and checking the integrity of this `DocumentTools` repository.

### Site Layout & Directory Map

The repository is built as a Jekyll static site using the `just-the-docs` theme, compiled automatically on GitHub Pages. Quarto is used to build slides.

```text
DocumentTools/
├── _config.yml                     # Jekyll configuration (remote theme, plugins)
├── _quarto.yml                     # Quarto website output options
├── README.md                       # Main site landing page (index)
├── guides.md                       # Main guides index & repo developer guide (this page)
├── AGENTS.md                       # Workspace conventions and rules for AI agents
├── R/                              # R language tutorials and notebooks
├── python/                         # Python language tutorials and notebooks
├── github/                         # Git and GitHub publishing workflows
├── envsys/                         # Environmental systems data notes
├── datasci/                        # Data science resources
├── AI/                             # AI tool summaries and agents research
├── prompts/                        # System prompts and case studies
├── quarto/                         # Quarto source slides and compiled slide decks
└── scripts/                        # Repository helper scripts
    ├── check_links.py              # Automated link checking script
    └── add_glyphs.py               # Glyphs addition helper
```

#### Configuration Files

- **`_config.yml`**: Uses the `remote_theme: just-the-docs/just-the-docs`. It enables `jekyll-relative-links` (allowing markdown files to reference each other with standard relative links like `[text](folder/file.md)`) and auto-generates the side navigation tree based on metadata.
- **`_quarto.yml`**: Configures Quarto slide projects to compile `.qmd` files in place (`output-dir: .`) so they can be processed and served alongside Jekyll markdown files.

---

### Page Metadata & Frontmatter Standards

To ensure Jekyll organizes the navigation sidebar and breadcrumbs correctly, every markdown and Quarto file must begin with standard YAML frontmatter:

```yaml
---
title: "The Page Title"                # Shows in navigation menu and page title
parent: "Parent Page Title"           # MUST match the exact title of the parent page (optional)
nav_order: 3                           # Determines layout order under parent (optional)
permalink: /optional/custom/path/      # Absolute URL path override (optional)
---
```

#### Folder Conventions

- Save general conceptual notes as markdown files (`.md`) inside their respective folders (e.g. `github/`, `AI/`, `python/`).
- Save slides as Quarto slides (`.qmd`) under `quarto/`.
- Ensure all relative link paths to other documents do not include leading slashes or absolute domain prefixes, so that they render correctly in local previews and on the published GitHub Pages site.

---

### Automation & Link Checking

To prevent dead references and broken links as external websites change, use the automated script in `scripts/check_links.py` to scan the repository.

#### Running the Link Checker

Run the script from the repository root:

```bash
python3 scripts/check_links.py
```

#### Features

- Scans all `.md`, `.qmd`, and `.Rmd` files in the repository.
- Extracts and checks all `http://` and `https://` URLs in parallel using threaded execution.
- If broken links are found, generates a detailed markdown report (`link_check_report.md` in the root) listing the file, line number, URL, and HTTP status code or connection error.

For more details on link checking parameters (ignoring SSL errors, checking a single file, fetching historical Wayback Machine snapshots), see the [Check External Links Guide](prompts/check_links.md).

### DEVELOPER.md vs Full Developer Guide

Analysis: `qtl2pattern` vs `qtl2shiny` Developer Guides

#### Why `qtl2shiny` Has an Extensive `vignettes/devel_guide/`

`qtl2shiny` is an interactive Shiny application featuring complex reactive networks, multi-module UI/server contracts (`snpPatternApp`, `patternDataApp`, `patternPlotApp`, `scanApp`, `genoApp`, `mediateApp`, `hotspotApp`), and state management across tabs. Each Shiny module required a dedicated document (`pattern.Rmd`, `scan.Rmd`, `geno.Rmd`, etc.) to map out reactive inputs/outputs, server parameters, and Shiny UI hierarchies.

#### Current State of `qtl2pattern`

`qtl2pattern` is the underlying R computational engine (~29 R source files). The root **[DEVELOPER.md](https://github.com/byandell-sysgen/qtl2pattern/blob/main/DEVELOPER.md)** already provides a comprehensive single-page reference covering:

- **System Architecture & Data Flow** (with Mermaid diagram)
- **Subsystem Module Maps** (Pattern Conversions, Scanning, Feature Querying, `fst` Storage, `ggplot2` Extensions)
- **R Coding Rules & Safety** (vector subsetting, namespacing, roxygen)
- **Development & Verification Workflow**

#### Comparison of Options

| Feature / Goal | **Option A: Root `DEVELOPER.md` Only** (Current) | **Option B: Add `vignettes/devel_guide/`** |
| :--- | :--- | :--- |
| **Primary Audience** | GitHub contributors, AI agents, IDE developers | `pkgdown` site readers, CRAN/R vignette users |
| **Maintenance Burden** | **Low** (Single document to update) | **Moderate** (Multiple Rmd files to sync) |
| **Structure** | Single comprehensive Markdown document | `vignettes/devel_guide/index.Rmd` + sub-Rmds (`patterns.Rmd`, `scans.Rmd`, `features.Rmd`, `plots.Rmd`) |
| **`pkgdown` Integration** | Markdown file in repo root | Built into package documentation / vignette menus |

#### Recommendation

- **If your goal is GitHub maintainability**: **Option A** (current [DEVELOPER.md](https://github.com/byandell-sysgen/qtl2pattern/blob/main/DEVELOPER.md)) is sufficient and easier to keep up to date.
- **If you plan to build a `pkgdown` site or want vignette-indexed developer docs**: **Option B** can be created by splitting [DEVELOPER.md](https://github.com/byandell-sysgen/qtl2pattern/blob/main/DEVELOPER.md) into `vignettes/devel_guide/index.Rmd` alongside modular Rmds for the major subsystems (`patterns.Rmd`, `scans.Rmd`, `features.Rmd`, `plots.Rmd`).
