---
title: "Create Shiny App Gallery"
parent: "Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 6
---

# Create Shiny App Gallery

This guide explains how to display both a Shiny application and its source code side-by-side or on the same page, similar to the
[Posit Shiny Gallery](https://shiny.posit.co/r/gallery/).

We cover two main approaches: using embedded client-side **Shinylive** apps in a Quarto page (highly recommended for hosting on static sites like GitHub Pages without folder clutter), and R's built-in **Showcase Mode** (best for local R console development).

See also [GitHub Actions](../github/actions.md) for information on how to deploy the app.

---

## Method 1: Embedded Shinylive (Recommended for Web Galleries)

By using `{shinylive-r}` or `{shinylive-python}` Quarto blocks, your app code is compiled and embedded directly inside the rendered WebAssembly page. This provides an interactive, copyable, and runnable app directly inside the browser.

> [!TIP]
> **Customizing Layout Components**:
>
> - **Viewer-Only Mode (Default for Galleries)**: To hide the code editor entirely and only display the running app, set `#| components: [viewer]`. This is ideal when you want to show the code in separate static tabs below the app.
> - **Interactive Code Editor**: To allow users to modify the code and run it inside their browser, set `#| components: [editor, viewer]`.

### 1. Configure the Quarto Document

Create a `.qmd` file (e.g., `demos/my_app_demo.qmd`) that includes the `shinylive` filter in the YAML header (or share it across the directory via `_metadata.yml`):

```yaml
---
title: "Interactive App Demo (Shinylive)"
filters:
  - shinylive
---
```

### 2. Embed R Apps using `{shinylive-r}`

Add your self-contained R Shiny code (combining module server and app UI) in a `{shinylive-r}` block:

```markdown
\`\`\`{shinylive-r}
#| standalone: true
#| viewerHeight: 500
#| components: [viewer]

library(shiny)
library(bslib)

# --- Module definitions ---
myModuleServer <- function(id) { ... }
myModuleInput <- function(id) { ... }
myModuleOutput <- function(id) { ... }

# --- Main App ---
ui <- bslib::page_sidebar(
  sidebar = bslib::sidebar(myModuleInput("mod")),
  bslib::card(myModuleOutput("mod"))
)

server <- function(input, output, session) {
  myModuleServer("mod")
}

shiny::shinyApp(ui, server)
\`\`\`
```

### 2b. Embed Python Apps using `{shinylive-python}`

For Python-based Shiny apps, use `{shinylive-python}`. Declare package dependencies in `## file: requirements.txt` and define virtual multi-file apps using `## file:` headers:

```markdown
\`\`\`{shinylive-python}
#| standalone: true
#| viewerHeight: 600
#| components: [viewer]

## file: requirements.txt
pandas
numpy
matplotlib
plotnine

## file: my_module.py
# custom module logic goes here...

## file: app.py
from shiny import App, ui
from my_module import my_module_ui, my_module_server

app_ui = ui.page_fluid(
    my_module_ui("demo")
)

def server(input, output, session):
    my_module_server("demo")

app = App(app_ui, server)
\`\`\`
```

> [!NOTE]
> **WebAssembly Restrictions (CORS & C-Extensions)**:
>
> - **CORS Policies**: Fetching live remote data dynamically over `http` in browser Pyodide may fail due to browser CORS blocks. Mock data as static `pandas.DataFrame` or `data.frame`.
> - **C-Extensions**: Packages compiling custom C libraries locally (e.g., custom DB drivers) cannot run directly inside Pyodide/webR. Use pure Python/R equivalents.

### 3. Rendering and Local Preview

Service Workers and WebAssembly do not run over local `file://` protocol URLs. To test your gallery locally, serve it using a local HTTP server:

- **Quarto Preview**:

  ```bash
  quarto preview demos/index.qmd
  ```

- **Python HTTP Server**:

  ```bash
  python3 -m http.server 8000
  ```

---

### 4. Deploying to GitHub Pages

> [!WARNING]
> **Do NOT use `embed-resources: true` or `self-contained: true`**:
> Shinylive WebAssembly binaries (`webR`, Pyodide, service workers `shinylive-sw.js`, and `site_libs/shinylive`) **cannot** be base64-embedded into standalone single-file HTML pages. Setting `embed-resources: true` will break Shinylive app execution.
> Always configure `output-dir: _site` in `_quarto.yml` and let GitHub Actions render and publish `_site/` dynamically.

#### Standard `.gitignore` Configuration

Add build artifacts to `.gitignore` to keep your Git repository clean (do NOT commit 70MB `site_libs/` or generated HTML files):

```gitignore
# Quarto output and build folders (built & deployed dynamically by GitHub Actions)
_site/
_extensions/
.quarto/
/.quarto/
site_libs/
index.html
demos/*.html
docs/demos/*.html
```

#### Automated GitHub Actions Pipeline (`.github/workflows/deploy.yml`)

Create `.github/workflows/deploy.yml` to automatically compile the website and publish `_site` to GitHub Pages on every push to `main`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up R
        uses: r-lib/actions/setup-r@v2
        with:
          use-public-rspm: true

      - name: Install R package dependencies
        run: |
          install.packages(c("rmarkdown", "knitr", "shinylive", "bslib", "shiny", "ggplot2", "dplyr", "rlang"))
        shell: Rscript {0}

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Install Quarto Shinylive Extension
        run: |
          quarto add --no-prompt quarto-ext/shinylive

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install shinylive plotnine plotly pandas numpy shinywidgets

      - name: Render Website
        run: |
          quarto render .

      - name: Prevent Jekyll Processing
        run: |
          touch _site/.nojekyll

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '_site'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## Organizing Directory Layout Options

Depending on your preference and GitHub Pages configuration, gallery demos can be organized into top-level `./demos/` or nested `./docs/demos/`.

### Option A: Top-Level Layout (`./demos/`)

Recommended when building a project website with GitHub Actions rendering from root.

```
repo_root/
├── _quarto.yml                # Quarto website settings (output-dir: _site)
├── index.qmd                  # Root page (includes README.md)
├── README.md                  # README & demo cards table
├── .gitignore                 # Ignores _site/, _extensions/, site_libs/
├── .github/workflows/
│   └── deploy.yml             # Automated CI/CD deployment
└── demos/
    ├── _metadata.yml          # Shared settings (filters: [shinylive])
    ├── index.qmd              # Demos gallery listing grid (listing: type: grid)
    ├── r_app.qmd              # R Shinylive app & code tabsets
    └── python_app.qmd         # Python Shinylive app & code tabsets
```

- **Relative Paths**: Files inside `./demos/*.qmd` are **1 level deep** relative to root. Use `../` to access root assets (e.g. `image: "../images/preview.png"` or `readLines("../R/my_module.R")`).

---

### Option B: Docs-Level Layout (`./docs/demos/`)

Recommended when publishing directly from the `/docs` directory branch on GitHub.

```
repo_root/
├── _quarto.yml                # Quarto website settings (output-dir: _site or docs)
├── index.qmd                  # Root page
├── README.md                  # Landing page content
└── docs/
    └── demos/
        ├── _metadata.yml      # Shared settings (filters: [shinylive])
        ├── index.qmd          # Demos gallery listing grid
        ├── r_app.qmd          # R Shinylive app
        └── python_app.qmd     # Python Shinylive app
```

- **Relative Paths**: Files inside `./docs/demos/*.qmd` are **2 levels deep** relative to root. Use `../../` to access root assets (e.g. `image: "../../images/preview.png"` or `readLines("../../R/my_module.R")`).

---

### Shared Directory Settings (`_metadata.yml`)

Create `_metadata.yml` in your demos directory (`demos/_metadata.yml` or `docs/demos/_metadata.yml`) so all demo pages inherit wide display settings and the `shinylive` filter:

```yaml
engine: knitr
toc: false
page-layout: full
filters:
  - shinylive
```

---

### Automated Listing Gallery Grid (`demos/index.qmd`)

Quarto's built-in **Listings** feature automatically constructs gallery cards:

```yaml
---
title: "Demos Gallery"
toc: false
listing:
  contents:
    - r_app.qmd
    - python_app.qmd
  type: grid
  categories: true
---

Explore interactive WebAssembly application demos below:
```

#### Customizing Preview Card Images

- **Assigning Card Images**: Add `image` to frontmatter in each demo `.qmd` file:

  ```yaml
  ---
  title: "R Scatter App"
  image: "../images/r_scatter_preview.png"
  ---
  ```

- **Preventing Image Cropping (Different Shapes & Sizes)**: By default, Quarto grid cards apply `object-fit: cover` to thumbnail images, cropping images of varying aspect ratios. To display card images fully without cropping:
  1. Specify `image-height` in your `listing:` configuration in `index.qmd` (e.g. `image-height: 180px`).
  2. Add `object-fit: contain !important;` in a custom CSS stylesheet (e.g. `styles.css` linked in `_quarto.yml` under `format: html: css: styles.css`):

     ```css
     .quarto-grid-item .card-img-top img,
     .quarto-grid-item .card-img-top,
     .quarto-grid-item .card-img,
     .quarto-grid-item .thumbnail-image {
       object-fit: contain !important;
       background-color: #f8f9fa;
     }
     ```

---

## Specific Reference Implementations

Below are concrete repository examples demonstrating these gallery patterns:

1. **`byandell/scattyr` (Option A: Top-Level `./demos/` Layout)**:
   - Root Quarto website with Shinylive R and Python scatter plot modules.
   - Files: `_quarto.yml`, `demos/index.qmd`, `demos/r_scatter_app.qmd`, `demos/python_scatter_app.qmd`, `.github/workflows/deploy.yml`.

2. **`byandell/geyser` (Option B: Docs-Level `./docs/demos/` Layout)**:
   - Quarto website gallery for Old Faithful Geyser R and Python modules.
   - Files: `_quarto.yml`, `docs/demos/index.qmd`, `docs/demos/build_module.qmd`, `docs/demos/python_module.qmd`, `.github/workflows/deploy.yml`.

---

## Method 2: Shiny Showcase Mode (Local R Console Development)

For local R console debugging, Shiny's built-in **Showcase Mode** highlights reactive execution in real-time alongside your code:

```r
shiny::runApp("inst/app_folder", display.mode = "showcase")
```

Add a `DESCRIPTION` file to the app directory:

```dcf
Title: Module Demo App
Author: Developer
Description: Interactive Shiny module demo.
DisplayMode: Showcase
```
