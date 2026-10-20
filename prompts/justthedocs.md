---
title: "Configure Just-the-Docs"
parent: "Prompt Examples"
nav_order: 5
---

# Configure Just-the-Docs

**Challenge**:
When setting up a documentation site using GitHub Pages, you want a clean, modern, responsive design with hierarchical navigation (headings, sub-pages) and proper SEO tags (including page names in browser tabs), without having to build a custom site from scratch.

**Use**:
Set up a standard Jekyll repository and apply the following configuration to enable the
[just-the-docs](https://just-the-docs.com/)
theme, customize navigation hierarchy, and configure site metadata.

**Prompt**:
"Follow [Configure Just-the-Docs](justthedocs.md) to set up and configure the `just-the-docs` remote theme, establish a site-wide navigation structure, enable page names in browser tabs, and enable Mermaid diagram rendering."

---

## Just-the-Docs Configuration Guide

### 1. Remote Theme Configuration

To run
[just-the-docs](https://just-the-docs.com/)
directly on GitHub Pages without installing local gems, configure `_config.yml` in the root of your repository:

```yaml
# Site branding and URLs
title: "Document Tools"
description: "Documentation for Digital Tools"
url: "https://byandell.github.io"
baseurl: "/DocumentTools"

# Theme setup
remote_theme: just-the-docs/just-the-docs

# Enable Mermaid diagram support
mermaid:
  version: "10.9.1"

# Plugins for remote theme and relative links
plugins:
  - jekyll-relative-links
  - jekyll-remote-theme

relative_links:
  enabled: true
  collections: true

# Apply default theme layout to all pages
defaults:
  - scope:
      path: ""
      type: pages
    values:
      layout: default
```

### 2. Page Navigation and Hierarchy

Use Jekyll front matter at the top of each Markdown (`.md`) file to configure where it appears in the navigation sidebar:

#### Homepage (`index.md` or `README.md`)

Specify `permalink: /` to render this page at the root URL.

```yaml
---
title: "Documentation for Digital Tools"
nav_order: 1
permalink: /
---
```

#### Top-level Navigation Page

Set a high-level page order using `nav_order`.

```yaml
---
title: "AI (Artificial Intelligence)"
nav_order: 5
has_children: true
---
```

#### Second-level child page

Link to a parent page by matching its exact title in `parent`.

```yaml
---
title: "AI Prompt Examples"
parent: "AI (Artificial Intelligence)"
nav_order: 1
has_children: true
---
```

#### Third-level grandchild page

Link to a parent and grandparent page.

```yaml
---
title: "Just the Docs Configuration"
parent: "AI Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 2
---
```

### 3. Enabling Page Names in Browser Tabs

To display tab titles in the browser as `Page Title | Site Title` (e.g. `Configure Just the Docs | Documentation`), the site must have:

1. `title` defined in `_config.yml` (e.g., `title: "Documentation"`).
2. `title` defined in the page's YAML front matter (e.g., `title: "Configure Just the Docs"`).
3. The `jekyll-seo-tag` plugin (which is loaded automatically by the
[just-the-docs](https://just-the-docs.com/)
theme through its `{% seo %}` block in `_includes/head.html`).

### 4. Enabling Mermaid Diagrams

To render interactive Mermaid diagrams (flowcharts, sequence diagrams, architecture trees) in Markdown, enable Mermaid in `_config.yml`:

```yaml
mermaid:
  version: "10.9.1"
```

Once enabled, standard Markdown ` ```mermaid ` code blocks render automatically as responsive SVG diagrams:

```mermaid
graph TD
    A[Markdown File] --> B[Jekyll / Just-the-Docs]
    B --> C[Mermaid JS Engine]
    C --> D[SVG Diagram Output]
```

