---
title: "Refactor Workflows"
parent: "Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 3
---

# Refactor Workflows

This was developed as I began using AI agents in creating the R package
[sysgenAnalysis](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis)
based on analysis workflows developed in the
[Attie Lab](https://attie.lab.wisc.edu/) ⚠️.
The goal was to refactor a set of analysis workflows, one at a time, into a modular R package structure.

The process starts with a single-file analysis workflow script, say `[basename].R`,
for an analysis named `[workflow]`.
Typically `[basename].R` has a mix of analysis steps, data cleaning and organization steps, and plotting steps.
There may be several data objects used by the script,
and the script may write several data objects and plots to files.
Further, different scripts may share common functions.

**Use**:
Be sure you are working in a folder where you want the new package components to live.
Type the following prompt into AI, substituting for `[basename].R` and `[workflow]`

**Prompt**:
"follow the
[workflow prompt](https://github.com/byandell/DocumentTools/blob/main/prompts/workflow.md) to refactor `[basename].R` into a modular R package structure
for the analysis `[workflow]`".

---

**Goal**: Refactor a [workflow] into a modular R package structure.

**Instructions**:

1. **Set the [workflow] and [basename] variables from user input**:
    - [workflow]: The name of the workflow to refactor.
    - [basename]: The `basename` to use for the refactored workflow.

2. **Understand the workflow**: Read the [workflow] and understand what it does.

3. **Extract Functions**: Move all logical units (data processing, analysis, plotting) into `R/[basename].R`.
    - Document each function with **Roxygen2** syntax (including `@param`, `@return`, and `@export`).
    - Use R native pipes (`|>`) and explicit namespace calls (e.g., `dplyr::mutate`).
    - Centralize shared constants (like coordinate maps) if not already in `common.R`.

4. **Create Entry Script**: Create an execution script `inst/scripts/analyze_[basename].R`.
    - Use it as a clean entry point that calls the functions defined in `R/`.
    - Handle environment setup, file paths, and high-level execution flow here.

5. **Return S3 Objects**: Refactor the main "run" function to return an S3 object of class `[basename]_analysis`.
    - Implement `print`, `summary`, and `plot` methods in `R/[basename].R`.
    - Move file-saving logic (`write.csv`, `ggsave`) out of the functions and into the entry script.

6. **Verify Integration**: Check package and scripts, correcting any issues that arise.
    - Verify documents with `devtools::document()`.
    - Build the package.
    - Ask user whether or not to run the analyze_[basename].R script to make sure it works.

7. **Create Exploration Document**: Create an interactive Shiny-based Quarto document `inst/scripts/explore_[basename].qmd` allowing for dynamic filtering and exploration.
    - Set `server: shiny` in the YAML header.
    - Use `context: setup` to load data via `sysgenAnalysis::read_[basename]_analysis()`.
    - Use `::: {.panel-tabset}` to organize sections into **Summary**, **Tables**, and **Plots**.
    - Use Shiny's `fluidRow` and `column` within each tab to create a side-bar like experience for controls next to outputs.
    - Integrate `downr::downloadUI` and `downr::downloadServer` for exporting tables and plots.
    - This approach provides a premium, interactive experience while keeping rendering fast by loading pre-calculated CSVs.

**Requested Files**:

- `R/[basename].R`
- `inst/scripts/analyze_[basename].R`
- `inst/scripts/explore_[basename].qmd`
