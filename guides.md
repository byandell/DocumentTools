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
  - [Guides and Overviews across Ecosystem](#guides-and-overviews)
- [DocumentTools Repository Developer Architecture](#documenttools-repository-developer-architecture)
- Additional Pages
  - [Developer Architecture & Maintenance Guide (`DEVELOPER.md`)](DEVELOPER.md)
  - [Create Developer Guides (Blueprint & Case Study)](prompts/devel_guide.md)

---

## Digital Tool Guides & Prompts

### Prompts

- [Create Developer Guides (Blueprint & Case Study)](prompts/devel_guide.md)
- [Use `pkgdown` to Auto-Build GitHub Website](github/pkgdown.md)

### Guides and Overviews

| Project / Repository | Architecture (`DEVELOPER.md`) | Developer & User Guides | AI Agent Rules (`AGENTS.md`) |
| :--- | :--- | :--- | :--- |
| **[DocumentTools](https://byandell.github.io/DocumentTools)** (`this repo`) | [`DEVELOPER.md`](DEVELOPER.md) | [Developer Guide](DEVELOPER.md) | [`AGENTS.md`](AGENTS.md) |
| **[`qtl2shiny`](https://byandell-sysgen.github.io/qtl2shiny/)** | [`DEVELOPER.md`](https://github.com/byandell-sysgen/qtl2shiny/blob/main/DEVELOPER.md) | [Developer Guide](https://byandell-sysgen.github.io/qtl2shiny/articles/devel_guide/index.html) ([Articles](https://byandell-sysgen.github.io/qtl2shiny/articles/)) | [`AGENTS.md`](https://github.com/byandell-sysgen/qtl2shiny/blob/main/AGENTS.md) |
| **[`geyser`](https://byandell.github.io/geyser/)** | [DEVELOPER.md](https://byandell.github.io/geyser/DEVELOPER.html) | [R Developer Guide](https://byandell.github.io/geyser/vignettes/DeveloperGuide.html)<br/>[Python Developer Guide](https://byandell.github.io/geyser/docs/devel/python.html) | [`AGENTS.md`](https://github.com/byandell/geyser/blob/main/AGENTS.md) |
| **[`landmapyr`](https://byandell-envsys.github.io/landmapyr/)** | [`DEVELOPER.md`](https://github.com/byandell-envsys/landmapyr/blob/main/DEVELOPER.md) | — | [`AGENTS.md`](https://github.com/byandell-envsys/landmapyr/blob/main/AGENTS.md) |
| **[`rainDrought`](https://byandell.github.io/rainDrought/)** | [DEVELOPER.md](https://byandell.github.io/rainDrought/DEVELOPER.html) | [User Guide](https://byandell.github.io/rainDrought/user_guide.html) | [AGENTS.md](https://byandell.github.io/rainDrought/AGENTS.md) |
| **[`byandell-sysgen`](https://byandell-sysgen.github.io/)** | [`DEVELOPER.md`](https://github.com/byandell-sysgen/.github/blob/main/DEVELOPER.md) | — | - |

---

## DocumentTools Repository Developer Architecture

For full details on this repository's static site generation pipeline, directory map, frontmatter metadata rules, automated link-checking workflows, and AI pair-programming instructions, see:

- **[Developer Architecture & Maintenance Guide (`DEVELOPER.md`)](DEVELOPER.md)**: Master reference for maintaining and compiling `DocumentTools`.
- **[Check External Links Guide](prompts/check_links.md)**: Instructions and audit reports for running `scripts/check_links.py`.
- **[Create Developer Guides Blueprint](prompts/devel_guide.md)**: Universal template for authoring developer guides across R, Python, and Documentation projects.

