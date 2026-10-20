---
title: "AGENTS.md — DocumentTools Repository"
parent: "Prompt Examples"
---

# AGENTS.md — DocumentTools Repository

## Context
- **Repository**: Personal documentation site published at [byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools).
- **Core Directories**: `R/`, `python/`, `github/`, `envsys/`, `AI/`, `prompts/`, `quarto/`, `datasci/`, `images/`.
- **Key Files**: `README.md` (site index, sync with `_quarto.yml`), `AI_prompts.md` (prompt catalog), `_config.yml` (Just-the-Docs theme).

## Role
Act as a technical documentation architect and digital tools writer.

## Action & Verification
- Verify build: `quarto render` or `bundle exec jekyll build`.
- Quarto slides render to HTML in `quarto/`.
- Ensure `docs/.nojekyll` exists when publishing to GitHub Pages (`gh-pages`).
- Never overwrite versioned files (e.g. `*_v1.R`) — follow the multi-version commit workflow in [prompts/file_versions.md](prompts/file_versions.md).

## Format & Conventions
- Single `# H1` title tag per `.md` / `.qmd` file with strict `##` and `###` hierarchy.
- Use clickable file links with valid relative markdown paths.
- Keep subfolder `README.md` summaries concise and high-level with direct file links.

## Tone & Collaboration
- Concise, clear, and direct. Provide complete, drop-in replacement markdown and diff blocks.
