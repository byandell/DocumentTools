---
title: "AGENTS_mini.md (Mini)"
nav_exclude: true
---

# AGENTS.md (Mini)

Personal documentation site for Brian Yandell (`byandell`): [byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools) ([GitHub](https://github.com/byandell/DocumentTools)).

## Structure

- `R/`, `python/`, `github/`, `envsys/`, `shiny/`, `AI/`, `prompts/`, `quarto/`, `datasci/`, `images/`
- `README.md` (Main site index; sync with `_quarto.yml`)
- `AI_prompts.md` (AI prompts index; update when adding new ones)
- `prompts/` (Saved prompts, e.g., `workflow.md`)

## Key Rules

- **No Overwriting Versioned Files**: Follow multi-version commit workflow in [prompts/workflow.md](prompts/workflow.md) (e.g., do not overwrite `*_v1.R`).
- **Prose**: Markdown (`.md`) or Quarto (`.qmd`). Quarto slides render to HTML in `quarto/`.
- **Sub-folder READMEs**: Concise, high-level summaries with file links.

## Code Preferences

- **R**: `tidyverse`, standard `roxygen2` docs, build packages with `devtools`.
- **Python**: `pandas`, `scikit-learn`, docstrings, type hints.
- **Reports/Slides**: Quarto (`.qmd`) over R Markdown (`.Rmd`).
- **Shiny**: `bslib` for UI/theming.
