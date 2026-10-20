---
title: "Publish Quarto Dashboard"
parent: "Publish GitHub Pages"
grand_parent: "Organize Projects with GitHub"
nav_order: 3
---

# Publish Quarto Dashboard

**Prompt**:
Is there a way to use shinylive to publish demo.qmd (demo.html) as a static file much as we did with the shiny app?

**Response**:
No, you cannot directly export a standard `server: shiny` Quarto Dashboard (which uses markdown sections for the layout and separates the server code in `#| context: server` blocks) using `shinylive::export`.

Here is why, and how you can achieve a static Shinylive version of the dashboard.
[The advice would work for a much simpler app.
It did not work in this case.]

---

### Why a standard Shiny Quarto Dashboard cannot be exported directly

1. **Server dependency**: Standard Quarto dashboards with `server: shiny` rely on a running backend R session (like Posit Connect or Shiny Server) to sync the inputs/outputs spread throughout the document.
2. **Shinylive's "Standalone" requirement**: When using Shinylive in Quarto, the entire Shiny application (both UI and Server logic) **must be self-contained inside a single code block** defined as `#| standalone: true`. You cannot distribute widgets across different markdown headings/sidebar columns.

---

### How to publish it statically with Shinylive

If you want a serverless, static version of this dashboard, you have two options:

#### Option A: Use the R Shiny App (Already Done)

The Shiny application in [inst/connect_modules/app.R](https://github.com/byandell/geyser/blob/main/inst/connect_modules/app.R) already contains the same plots and logic as `demo.qmd`.

* Because it is a standard Shiny app, it is fully compatible with `shinylive::export()`.
* It is already successfully exported as a serverless, static app in your `docs/shiny/` directory.

#### Option B: Embed a Shinylive App inside a Quarto Document

If you specifically want a `.qmd` document that compiles to a static page containing the interactive dashboard, you can embed the R code inside a `{shinylive-r}` block:

1. **Install the Shinylive Quarto Extension** (locally in your terminal):

   ```bash
   quarto add quarto-ext/shinylive
   ```

2. **Create a new `.qmd` file** (e.g. `docs/demo_shinylive.qmd`) with the `shinylive` filter:

   ```yaml
   ---
   title: "Geyser Dashboard (Static)"
   format: html
   filters:
     - shinylive
   ---
   ```

3. **Embed the code** in a single standalone block:

   ```markdown
   ```{shinylive-r}
   #| standalone: true
   #| viewerHeight: 700

   # Paste the loading helper, ui structure, and server logic here
   # (e.g. your source code from inst/connect_modules/app.R)
   ```

   ```
4. **Render it**:
   When you run `quarto render docs/demo_shinylive.qmd`, it will compile into a serverless interactive HTML page that runs entirely in the browser and can be served statically on GitHub Pages.

---

## Walkthrough: Option B Implementation

I have implemented and automated Option B to host a serverless, interactive Quarto dashboard on GitHub Pages:

### 1. Installed Quarto Shinylive Extension

Installed the extension in the repository:

```bash
quarto add quarto-ext/shinylive --no-prompt
```

### 2. Created Self-Contained Shinylive Document

Created [docs/demo_shinylive.qmd](file:///Users/brianyandell/Documents/GitHub/geyser/docs/demo_shinylive.qmd). It is structured to run completely in the browser via WebAssembly:

* **YAML Header**: Configured format as `html` and registered the `shinylive` filter. Explicitly specified `engine: knitr` to bypass Jupyter/Python kernel execution checks (avoiding errors like `ModuleNotFoundError: No module named 'nbformat'`).
* **Code Chunk**: Set `#| standalone: true` and concatenated all the R modules (from the root `R/` directory) and the navbar UI layout (from `app.R`) inside a single `{shinylive-r}` code block.

### 3. Integrated into CI/CD Deployment Workflow

Updated [.github/workflows/deploy.yml](file:///Users/brianyandell/Documents/GitHub/geyser/.github/workflows/deploy.yml) to automate the build-and-deploy process on GitHub Actions:

* Installs `shinylive`, `knitr`, and `rmarkdown` R packages inside the runner.
* Installs the Quarto Shinylive extension inside the GitHub Actions runner.
* Renders `docs/demo_shinylive.qmd` using `quarto render docs/demo_shinylive.qmd`.
* Deploys the output `docs/demo_shinylive.html` (along with the other pages in the `docs/` folder) directly to GitHub Pages.

This avoids local rendering Deno cache errors, bypasses unnecessary Jupyter python dependencies, and automates updates every time you push to the `main` or `master` branch.
