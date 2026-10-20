---
title: "Create Developer Guides (Blueprint)"
parent: "Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 5
---

# Create Developer Guides (Blueprint)

This document serves as a general blueprint for creating developer guides across different project structures: **R Packages**, **Python Projects**, **Documentation Projects**, and **Hybrid R/Python Projects**.

A developer guide clarifies codebase structure, module boundaries, data routing, reactivity flow, and custom design patterns. It helps human maintainers and AI pair-programming agents understand how to extend and debug the system without introducing architectural drift.

In addition to a Developer Guide, a project would benefit from the following
complementary files:

- [R Package Developer Guide](./R_package_developer_guide.md)
- [Python Developer Guide](./python_developer_guide.md)
- [Documentation Developer Guide](./documentation_developer_guide.md)
- [Hybrid R & Python Developer Guide](./hybrid_r_python_developer_guide.md)
- Additional Pages
  - [`AGENTS.md`](../AI/agents.md): Repository-level systems instructions and agent skills
  - `README.md`: Repository overview and quick start
  - `DEVELOPER.md`: Developer-facing architecture notes and whole-repo guidance

> [!TIP]
> For a concrete case study of this blueprint applied to a mature R Shiny package, see the [qtl2shiny Developer Guide Reference](./devel_guide_qtl2shiny.md). For a hybrid R/Python package case study, see the [`geyser` developer documentation](https://byandell.github.io/geyser/DEVELOPER.html).

---

## R Package Developer Guides (Vignette-Based)

In mature R packages, developer guides are best placed as package vignettes (e.g., `vignettes/DeveloperGuide.Rmd`) so they render as part of the official package documentation (e.g., via `pkgdown`).

### Directory Layout

```text
my_package/
├── vignettes/
│   ├── DeveloperGuide.Rmd          # Master developer guide index
│   └── devel/
│       ├── data_flow.Rmd           # Detailed submodule guide
│       └── custom_plots.Rmd        # Detailed plotting guide
├── _pkgdown.yml                    # Configures navigation bar
└── R/                              # Package source code
```

### Actionable Prompts

1. **Directory & Index Setup**:
   > "Create a master developer guide vignette `vignettes/DeveloperGuide.Rmd` (or `.qmd`). The guide should detail the high-level architecture of the package, including execution entrypoints and core dependencies. Provide an index of all `.R` source files and group them by function category (e.g., DB querying, data loading, plotting, UI panels). Document this creation process in `prompts/devel_guide.md`."
2. **Sub-module/Panel Details**:
   > "Develop a detailed developer sub-guide in `vignettes/devel/module_name.Rmd` describing `module_name`. Document the inputs and outputs, reactive logic, data dependencies, and custom defensive checks. Include a Mermaid reactivity flow diagram if applicable."
3. **Internal Linking**:
   > "Update `vignettes/DeveloperGuide.Rmd` to link to the new sub-guide `vignettes/devel/module_name.Rmd` and ensure all file links are relative. Register the vignettes in the `_pkgdown.yml` site config so they are visible under the articles tab."

### Steps to Perform

1. **Analyze File Structure**: Identify all source files in the `R/` directory. Trace their dependencies and namespace exports.
2. **Create Vignettes Directory**: Ensure `vignettes/` (and subdirectories like `vignettes/devel/`) exists.
3. **Build the Prototype**: Create a single sub-module guide (e.g., `vignettes/devel/geno_module.Rmd`) to serve as a format prototype.
4. **Draft the Master Vignette**: Create `vignettes/DeveloperGuide.Rmd` with high-level architecture, module categorization, layout descriptions, and utility mappings.
5. **Add Sub-module Guides**: Flesh out guides for remaining sub-modules, using the prototype as a blueprint.
6. **Compile and Verify**: Run `devtools::build_vignettes()` to compile and `pkgdown::build_site()` to verify website navigation and layout.

---

## Python Project Developer Guides

Python developer guides are typically placed in `docs/devel/` (e.g., `docs/devel/python.md` for website rendering via Quarto/MkDocs) or inside the Python package source directory (`my_module/README.md`) for package developers, anchored by a root `DEVELOPER.md`.

### Directory Layout

```text
my_project/
├── DEVELOPER.md                    # Root architecture & developer guide entrypoint
├── docs/
│   └── devel/
│       ├── python.md               # Detailed Python Developer Guide (rendered on site)
│       └── environment_setup.md    # Python environment & dependencies
├── tests/                          # Test suite (pytest)
├── pyproject.toml / setup.py       # Configuration and dependencies
└── my_module/                      # Python package source code
    └── README.md                   # Sub-directory developer reference inside Python package source
```

### Actionable Prompts

1. **Initial Architecture Map**:
   > "Inspect the python package `my_module/` and map out the directory layout and core execution pathways (e.g., entrypoint `__main__.py` or class interfaces). Create a developer guide in `docs/developer_guide.md` detailing how classes interact and outline data processing pipelines."
2. **Setup and Testing Instructions**:
   > "Draft `docs/environment_setup.md` containing detailed commands to configure the python virtual environment (using venv, conda, or poetry), install developer dependencies, and execute the test suite via pytest. Note how code linting (ruff, black, flake8) is configured."
3. **API & Extension Guide**:
   > "Write documentation on how to extend the module. Outline class hierarchy interfaces (e.g., adding a new database engine or plot format) and define rules for code standards (e.g., docstrings style, type hints)."

### Steps to Perform

1. **Source Discovery**: Run `find my_module -name "*.py"` to map out files and subdirectories.
2. **Trace Class Interfaces**: Inspect imports and inheritance relationships to map out object-oriented structures.
3. **Create Environment Reference**: Document dependencies defined in `pyproject.toml`, `setup.py`, or `requirements.txt`.
4. **Draft the Developer Guide**: Structure the files into Overview, Class/Module Architecture, Testing Workflows, and Extension Guidelines.
5. **Code Style Definitions**: Detail constraints around docstring formats (Google, NumPy, Sphinx style) and type hinting protocols.

---

## Documentation Projects

For projects whose main deliverable is documentation (such as a Quarto book, Jupyter Book, or Just-the-Docs Jekyll site), the developer guide details site layout, configuration variables, page metadata, navigation structures, and automated checks.

### Directory Layout

```text
documentation_site/
├── guides.md                       # Navigation to user and developer guides
├── AGENTS.md                       # Project-level constraints for AI agents
├── _config.yml / _quarto.yml       # Site config files
├── index.md / README.md            # Landing / index page
└── scripts/
    └── check_links.py              # Automated link-validation scripts
```

### Actionable Prompts

1. **Site Layout Documentation**:
   > "Map out the site's folder hierarchy and page navigation in a root `guides.md` file. Explain the purpose of key configuration files like `_config.yml` or `_quarto.yml` and how the side navigation menu is generated."
2. **Metadata & Writing Conventions**:
   > "Add rules to the top-level developer index or `AGENTS.md` specifying frontmatter metadata standards (e.g., `title`, `parent`, `nav_order`, and `permalink`). Establish conventions for markdown headers, cross-references, and slide inclusions."
3. **Automation & Link Validation**:
   > "Create documentation in `prompts/check_links.md` on how to run automated link verification scripts. Outline how to identify and prune broken internal relative links and external web URLs before publishing."

### Steps to Perform

1. **Identify Configuration Entrypoints**: Map YAML configuration properties to the resulting website structure (navigation menus, page hierarchies).
2. **Define Frontmatter Conventions**: List required frontmatter elements for new pages to ensure correct layout and theme mapping.
3. **Setup Link-Check Tools**: Implement automated checks (e.g., python or bash scripts) to parse markdown links and identify 404s.
4. **Write guides.md / AGENTS.md**: Combine rules, templates, and procedures into readable documents for future editors and AI agents.

---

## Hybrid R & Python Projects

In research repositories (like
[`geyser`](https://byandell.github.io/geyser/)
or
[landmapyr](https://byandell.github.io/landmapyr/)),
R and Python code often sit side-by-side. The developer guide must
reconcile both ecosystems, outlining boundaries and interfaces.

### Dual-Housing Documentation Strategy

Based on experience with the `geyser` package, hybrid repositories succeed by adopting a **multi-tiered documentation and publishing strategy**:

1. **Root Repository Guide (`DEVELOPER.md`)**:
   - Primary entry point for developers of the overall project.
   - Documents shared architecture, cross-language module mappings (e.g., R 5-function modules vs Python `@module.ui` / `@module.server`), execution entry points, setup commands (`devtools::load_all()` and `pip install -e .`), port discovery, and reserved file patterns.
   - Links out to ecosystem-specific sub-guides.
2. **R Package Sub-Guide (`vignettes/DeveloperGuide.Rmd`)**:
   - Master vignette for R package compilation (`devtools::build_vignettes()`) and `pkgdown` / Quarto site rendering.
   - Focuses on R reactive flow, S3/S4 object structures, and R Shiny module patterns.
3. **Python Package Sub-Guide (`docs/devel/python.md` & `my_module/README.md`)**:
   - Housed in `docs/devel/python.md` for web/Quarto site rendering (`byandell.github.io/<project>`).
   - Housed in `my_module/README.md` as an in-source developer reference for Python package developers.
   - Focuses on Python reactivity, async loops, Shinylive WebAssembly build flows, and `rpy2` / dataframe data exchange.
4. **Planning & Execution Record (`guides.md`)**:
   - Consolidates initial blueprint prompts, the implementation plan, and the execution walkthrough for auditability and pair-programming context.
5. **Website Publishing & Dual-Linking**:
   - Registers all developer guides (`DEVELOPER.md`, `vignettes/DeveloperGuide.Rmd`, `docs/devel/python.md`) in site render configurations (e.g., `_quarto.yml`).
   - Integrates a **Developer Guides** dropdown menu into the website navbar linking to all three guides.
   - Provides dual links in `README.md` to both the published website pages and the raw GitHub source code files.

### Directory Layout

```text
hybrid_project/
├── DEVELOPER.md                    # Root architecture index & hybrid guide (both R & Python)
├── README.md                       # Repository overview & quickstart (links to DEVELOPER.md)
├── guides.md                       # Consolidated blueprint prompts, plan, and walkthrough
├── R/                              # R package source code
├── vignettes/                      # R-centric Vignettes
│   └── DeveloperGuide.Rmd          # Master R developer guide vignette
├── my_module/                      # Python package source code
│   ├── README.md                   # Python package sub-directory developer reference
│   └── io.py, hist.py, etc.        # Python package modules
└── docs/                           # Documentation & Quarto / MkDocs Website
    └── devel/                      # Extended sub-guides directory
        └── python.md               # Detailed Python Developer Guide (rendered on site)
```

### Actionable Prompts

1. **Bridge Architecture Map**:
   > "Create a root `DEVELOPER.md` describing how the R and Python components cooperate. Trace the communication boundaries (e.g.,
   [`reticulate`](https://rstudio.github.io/reticulate/),
   [`rpy2`](https://rpy2.readthedocs.io/en/latest/),
   subprocess calls, REST APIs, or shared SQLite/Parquet files). Provide a side-by-side R and Python module cross-reference table mapping equivalent features across ecosystems."
2. **Dual-Environment Configuration**:
   > "Create environment guides mapping out how to bootstrap both R and Python environments on a local machine. Document installation commands (`devtools::load_all()` for R and `pip install -e .` for Python) and dependency declarations."
3. **Shared Data & API Schemas**:
   > "Document data structures shared between R and Python code. Define SQLite database schemas, HDF5 hierarchies, or Parquet column schemas, detailing validation checks on both sides (e.g., `pandas.DataFrame` and R `data.frame` conversion rules)."
4. **Site Publishing & Navbar Integration**:
   > "Configure site render targets (e.g., in `_quarto.yml` or `_pkgdown.yml`) to compile `DEVELOPER.md`, `vignettes/DeveloperGuide.Rmd`, and `docs/devel/python.md` into published HTML site pages. Add a 'Developer Guides' dropdown menu to the website navbar and update `README.md` with side-by-side links to both published site pages and GitHub source code."

### Steps to Perform

1. **Establish Root Entry Point**: Create `DEVELOPER.md` in the repository root as the master developer guide indexing both R and Python architectures.
2. **Implement R Vignette Guide**: Draft `vignettes/DeveloperGuide.Rmd` to document R package modules and integration with `pkgdown`/Quarto.
3. **Implement Python Sub-Guides**:
   - Create `docs/devel/python.md` for site documentation (e.g., Quarto).
   - Create `my_module/README.md` within the Python source folder for direct developer reference.
4. **Define Dual-Testing Workflows**: Outline execution scripts that run both
[`pytest`](https://pytest.org/)
and
[`devtools::test`](https://testthat.r-lib.org/reference/test_package.html)
as part of verification.
5. **Coordinate Shared Data Schemas & Planning**: Formulate explicit specifications for exchange file formats
([CSV](https://allthings.how/what-is-a-csv-file-and-how-to-open-or-create-it/),
[Parquet](https://parquet.apache.org/),
[SQLite](https://www.sqlite.org/))
and maintain a `guides.md` file recording initial prompts, implementation plan, and completion walkthrough.
6. **Publish & Integrate Navbar Navigation**: Add developer guide files to the site build targets (`_quarto.yml`), configure a **Developer Guides** navbar dropdown menu, and update `README.md` with dual links (Published Page + GitHub Source).

---

## Case Study: `qtl2shiny` Package Developer Guide

> [!NOTE]
> This case study illustrates how the R package blueprint was applied to create the developer guide for the [`qtl2shiny`](https://byandell-sysgen.github.io/qtl2shiny/articles/DeveloperGuide.html) package ([source](https://github.com/byandell-sysgen/qtl2shiny/blob/master/vignettes/DeveloperGuide.Rmd)). See also [Use `pkgdown` to Auto-Build GitHub Website](../github/pkgdown.md).

### Prompts

The developer guide structure and content were developed interactively using the following prompts:

1. **Initial Setup**: "Create a developer guide to `qtl2shiny` package in `inst/doc/devel_guide/` folder. This will have a high-level guide to the panels used in `R/qtl2shinyApp.R` and major sections for each of those panels. It should focus on `R/*App.R` files, noting how some are integral to a panel and other are more generic. Consider the `doc/genoDataApp.md` as a model, which should be moved into the folder. Include a `README.md` in that folder. Use this file `inst/doc/devel_guide.md` to document the process of creating this guide."
2. **Relative Links Conversion**: "Make links in `inst/doc/devel_guide/README.md` relative."
3. **Table of Contents**: "Provide a TOC to `inst/doc/devel_guide/README.md`. After internal TOC, include a link to `./genoDataApp.md` in anticipation of more guide detail pages like this."
4. **Genotypes Panel Expansion**: "Develop detailed guides for `genoApp`, `genoPlotApp` and `genoEffectApp`. Make this an expansion (and renaming) of `genoDataApp.md`, reusing material as possible."
5. **Remaining Panel Guides**: "Using `genoApp.md` as a model, create developer guides for the other panels, including a link back to the developer's guide main page (`README.md`)."
6. **Prototype History**: "Add to `inst/doc/devel_guide.md` documentation of creating the initial `inst/doc/genoDataApp.md` as a prototype/model for the full developer's guide."
7. **Prompts Documentation**: "Add a front section on `## Prompts` used to develop this process."

### Prototype Development

Prior to launching the full developer guide, a single-module documentation prototype was created: `inst/doc/genoDataApp.md` (which documented the genotype data submodule `genoDataApp`). This prototype served as a model for the entire developer guide, establishing standard headings and design representations:

- **Module Hierarchy and Entrypoints**: Detailing the standalone entrypoint, the server module, and UI inputs/outputs.
- **Data Dependencies**: Clarifying what RDS and SQLite files the module reads.
- **Workflow Reactivity Diagrams**: Utilizing Mermaid flowcharts to visualize reactive logic.
- **Defensive Design Patterns**: Explaining code defensive checks (e.g. updating sliders reactively to prevent out-of-bounds errors when chromosome coordinates reset).

The success of the `genoDataApp.md` prototype in clarifying module logic led to expanding it into a unified Genotypes guide (`genoApp.md`) and reproducing the same structured format for all other major panels.

### Steps Performed

1. **Analysis of File Structure**:
   - Identified all 41 `R/*App.R` files on the filesystem.
   - Traced their loading and execution hierarchy within `R/qtl2shinyApp.R` and `inst/qtl2shinyApp/app.R`.

2. **Creation of Guide Directory**:
   - Created the directory `inst/doc/devel_guide/` to house developer documentation.

3. **Relocation & Expansion of Genotypes Guide (`genoApp.md`)**:
   - Relocated and renamed `inst/doc/genoDataApp.md` to [inst/doc/devel_guide/genoApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/genoApp.md).
   - Expanded the document to provide detailed developer guides for `genoApp` (the container panel), `genoPlotApp` (genotype probability plotter), and `genoEffectApp` (phenotype association effect calculator), reusing the original `genoDataApp` documentation.

4. **Creation of the Master Guide (`README.md`)**:
   - Created [inst/doc/devel_guide/README.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/README.md) as the high-level entrypoint.
   - Documented:
     - **UI Layout & Navigation**: The Bootstrap 5 layout, reactive linking across tabs, and standardizing panel names.
     - **Data Routing & Downloader Integration**: How active tabs route plot/table outputs to the external `downr` downloader module.
     - **Tab Panels & Submodules**: Divided into Hotspots & Phenotypes, Scans, Patterns, Genotypes, and Mediation.
     - **Utility Classification**: Grouped global controls like `projectApp.R`, `setParApp.R`, `winParApp.R`, `dipParApp.R`, `snpListApp.R`, and data loaders like `probsApp.R` and `kinshipApp.R`.
     - **Complete File Index**: Indexed and linked every `R/*App.R` file to its corresponding module type (Entrypoint, Integral Submodule, Data Loader, Normalizer, Selector, DB Query, and Generic Utility).

5. **Creation of Detailed Guides for Remaining Panels**:
   - Created detailed guides for remaining panels, each linking back to [README.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/README.md):
     - [hotspotApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/hotspotApp.md) for Hotspots & Phenotypes.
     - [scanApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/scanApp.md) for Allele & SNP Scans.
     - [patternApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/patternApp.md) for SDP Pattern Analysis.
     - [mediateApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/mediateApp.md) for Mediation.

### Rationale for Module Categorization

To maintain a clean separation of concerns, files were categorized based on lifecycle and data scope:

- **Integral Panel Modules**: Highly specific to a particular mathematical analysis (e.g. mediation computations, SDP pattern scans, LOD genome curves). They consume global reactives but do not mutate state consumed by other panels.
- **Generic/Utility Modules**: Mutate global states (e.g., changing chromosome or peak coordinates via `winPar` / `snpList`) or load large disk-backed data objects (e.g., genotype probabilities via `probs` / `kinship`) consumed globally by all panels.

