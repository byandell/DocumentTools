---
title: "Build and Launch a Serverless Interactive Website"
parent: "Publish GitHub Pages"
grand_parent: "Organize Projects with GitHub"
nav_order: 3
---

# Build and Launch a Serverless Interactive Website

This section resulted from a conversation with Patrick Freeland
([ATNI Tribes](https://atnitribes.org/about/our-staff/),
[Liken Knowledge](https://www.likenknowledge.org/likeneers/patrick-freeland))
about the many projects he has been developing using Claude.
See
[ATNI Climate](https://github.com/atniclimate)
and the specific project
[ATNI Climate Dynamic Drought Module](https://atniclimate.github.io/dynamic-drought-module/),
as well as
[high-level system architecture of that project](https://byandell.github.io/DocumentTools/quarto/serverless.html#/high-level-system-architecture).
Brian Yandell framed the prompt below.

- [1. High-level architecture how it works without a backend](#1-high-level-architecture-how-it-works-without-a-backend)
- [2. Fundamentals: Tooling Explained for Non-Node Developers](#2-fundamentals-tooling-explained-for-non-node-developers)
- [3. Configuration Files in This Repository](#3-configuration-files-in-this-repository)
- [4. How the GitHub Actions Pipeline Deploys to GitHub Pages](#4-how-the-github-actions-pipeline-deploys-to-github-pages)
- [5. Local Developer Workflow: Running and Building Locally](#5-local-developer-workflow-running-and-building-locally)
- [6. Summary: The Lifecycle at a Glance](#6-summary-the-lifecycle-at-a-glance)
- [7. Architectural Variations Across Projects](#7-architectural-variations-across-projects)

**Prompt:**

Explain how this repo uses `npm` or other tools to launch an interactive website via GitHub Pages. Likely there is useful information in `DEVELOPER.md`, `.nvmrc` and `.github/`. Include information on what is `npm` and other tools for a developer unfamiliar with this approach. Save in `EXPLAIN_NPM.md` in this directory.

**Model Answer:**

This guide explains how this repository uses **Node.js**, **npm**, **Vite**, and **GitHub Actions** to build, verify, and host a interactive, high-performance web mapping application on **GitHub Pages**,
which acts as a "serverless"
[high-speed static file server (CDN)](https://blog.blazingcdn.com/en-us/boost-repo-speeds-github-cdn-tips-faster-delivery).
It is written for developers, data scientists, and researchers who may be more familiar with Python, R, or traditional server architectures than the modern JavaScript/TypeScript ecosystem.

---

## 1. High-Level Architecture: How It Works Without a Backend

A common point of confusion for data scientists and developers coming from R (Shiny) or Python (Streamlit, Flask, Django) is: **how can a complex, interactive mapping tool run on GitHub Pages without a backend server?**

```mermaid
flowchart TD
    subgraph Dev["1. Development & Build (Local or CI)"]
        direction TB
        Src["Source Code<br/>• TypeScript (src/main.ts, src/layers/, etc.)<br/>• Styles (src/styles/)<br/>• Static Assets (public/data/)"]
        BuildEngine["Node.js + npm + Vite Bundler<br/>• tsc verifies static types<br/>• Vite bundles & minifies code<br/>• Splits MapLibre & PMTiles chunks"]
        Dist["Production Bundle (dist/)<br/>• index.html (with SHA stamp)<br/>• Optimized JS & CSS<br/>• Vector tiles & GeoJSON"]
        Src --> BuildEngine --> Dist
    end

    subgraph Hosting["2. GitHub Pages Deployment"]
        direction TB
        GHA["GitHub Actions (deploy.yml)<br/>• Checks out commit & runs gate<br/>• Uploads dist/ artifact<br/>• Publishes via actions/deploy-pages"]
        CDN["GitHub Pages CDN<br/>• Global HTTPS static hosting<br/>• HTTP Range-request support for tiles"]
        GHA --> CDN
    end

    subgraph Client["3. Client's Web Browser"]
        direction TB
        Browser["Visitor's Web Browser<br/>• Loads HTML, JS, CSS from Pages CDN<br/>• Executes MapLibre GL JS (WebGL / GPU)<br/>• Streams .pmtiles slices on demand<br/>• Directly queries public APIs (USGS, NIFC, NOAA)"]
    end

    Dist --> GHA
    CDN --> Browser
```

### Key Differences from Server-Driven Apps

- **R Shiny / Streamlit**: Require an active R or Python process running on a server 24/7 to compute data, filter tables, and render graphics whenever a user clicks a button.
- **Dynamic Drought Module (DDM) on GitHub Pages**: Has **zero application backend**.
  - All source TypeScript code is compiled down beforehand into static HTML, JavaScript, and CSS.
  - The map rendering engine (MapLibre GL JS) uses the visitor's computer/phone GPU via WebGL.
  - Data layers are either pre-compiled into static vector tile archives (`.pmtiles` and `.geojson` in `public/data/`) or fetched directly from public REST endpoints (USGS stream gauges, NIFC wildfires, etc.).
  - GitHub Pages simply acts as a
[high-speed static file server (CDN)](https://blog.blazingcdn.com/en-us/boost-repo-speeds-github-cdn-tips-faster-delivery)
delivering those static files to the browser.

---

## 2. Fundamentals: Tooling Explained for Non-Node Developers

If you are unfamiliar with the Node.js and npm ecosystem, here is how each piece maps to concepts in Python or R:

| Tool / Concept | What it is | Python Analogy | R Analogy | Role in this Project |
| :--- | :--- | :--- | :--- | :--- |
| **Node.js** | JavaScript runtime engine outside the browser | Python interpreter (`python3`) | R executable (`R`) | Runs build scripts, testing tools, and compilers on developers' laptops and GitHub servers. |
| **`.nvmrc`** | Node Version Manager config file | `.python-version` (pyenv) | `.Rversion` / `renv.lock` R version | Enforces that everyone uses the exact pinned version of Node (**24.20.0**). |
| **npm** | Node Package Manager | `pip` + `venv` / `poetry` / `uv` | `install.packages()` + `renv` | Downloads third-party libraries and runs workflow scripts. |
| **`package.json`** | Project manifest and task definition | `pyproject.toml` / `requirements.txt` | `DESCRIPTION` file | Lists dependencies, licenses, and command-line scripts. |
| **`package-lock.json`** | Cryptographic lockfile | `poetry.lock` / `requirements.lock` | `renv.lock` | Locks the exact checksums and versions of every transitive dependency. |
| **`npm ci`** | "Clean Install" command | `pip install --no-deps -r ...` | `renv::restore()` | Strictly installs from `package-lock.json` without modifying it. Used in CI and automated builds. |
| **`npm run <name>`** | Script runner | `make <task>` or `poetry run <task>` | `devtools::check()`, custom Makefile | Executes scripts defined in the `"scripts"` block of `package.json`. |
| **TypeScript (`tsc`)** | Statically typed JavaScript | Python type hints (`mypy`) | Static linters / type checkers | Catches errors before runtime; compiled away during build. |
| **Vite** | Modern frontend bundler & dev server | Not typically used; like a fast webpack/Sphinx | `pkgdown` / Quarto asset compiler | Assembles TypeScript, stylesheets, and assets into an optimized `dist/` bundle. |
| **Playwright** | Browser automation test framework | `pytest-playwright` / Selenium | `shinytest2` | Boots a headless browser and verifies user clicks, map interactions, and accessibility. |

---

## 3. Configuration Files in This Repository

### 1. `.nvmrc`

The single line `24.20.0` pins the exact patch release of Node.js Active LTS.

- Developers use `nvm use` to switch to this version locally.
- GitHub Actions reads this file with `actions/setup-node` (`node-version-file: .nvmrc`) so that cloud runners execute identical binaries.

### 2. `package.json`

Located at the root of the repository, this file organizes three crucial things:

1. **Engines**: Requires `node >= 24.0.0`.
2. **Dependencies**:
   - `dependencies`: Runtime libraries that ship into the user's browser (e.g., `maplibre-gl` for maps, `pmtiles` for reading archived vector tiles, `@preact/signals` for UI reactivity).
   - `devDependencies`: Development-only tools that never get sent to the end user (e.g., `typescript`, `vite`, `@playwright/test`, `mapshaper`).
3. **Scripts**: Command shortcuts executed via `npm run <name>`. Essential ones include:
   - `npm run dev`: Starts the local development server at `http://localhost:5173`.
   - `npm run build`: Runs TypeScript typechecking (`tsc --noEmit`) and invokes `vite build`.
   - `npm run preview`: Boots a local static HTTP server at `http://localhost:4173` serving the built `dist/` directory for production simulation.
   - `npm run gate`: Deterministic quality gate; builds `dist/`, checks bundle sizes and activation budgets, and runs all unit contracts.
   - `npm run test:serial`: Runs end-to-end browser tests via Playwright.

### 3. `vite.config.ts`

The configuration file for the Vite build tool. Key decisions implemented here:

- **`base: './'`**: Forces all asset links (scripts, CSS, images) to be relative rather than absolute (`/`). This allows the app to be hosted under a root domain, a GitHub Pages subfolder (e.g., `/dynamic-drought-module/`), or inside an iframe.
- **Build Stamping (`DDM_BUILD_SHA` and `DDM_BUILD_NONCE`)**: Injects the exact Git commit SHA and CI run identifier into the compiled HTML. When deployed, automated verification scripts read `document.documentElement.dataset.ddmBuildSha` to prove the live website actually runs the code that was merged.
- **Code Splitting (`rolldownOptions`)**: Isolates the heavy `maplibre-gl` (approx. 800 kB) and `pmtiles` libraries into dedicated chunks so browser caches preserve them across application updates.
- **`outDir: 'dist'`**: Instructs Vite to output the final website into the `dist/` folder.

---

## 4. How the GitHub Actions Pipeline Deploys to GitHub Pages

The automated deployment pipeline is governed by files in `.github/workflows/`:

```mermaid
flowchart TD
    Push["Push to 'main' Branch<br/>(paths-ignore filters docs-only commits)"] --> Concurrency["Concurrency Gate<br/>group: pages, cancel-in-progress: true"]

    subgraph DeployWorkflow["deploy.yml (GitHub Actions)"]
        direction TB
        subgraph BuildJob["Job: build (Gate & Build)"]
            direction TB
            Setup["Set up Node.js 24.20.0 (.nvmrc) & npm ci"]
            Gate["Run 'npm run gate'<br/>• tsc --noEmit (typecheck)<br/>• vite build (outputs dist/)<br/>• Bundle size & activation budget checks<br/>• Contract & unit tests"]
            UploadArtifact["actions/upload-pages-artifact<br/>Packages dist/ for Pages"]
            Setup --> Gate --> UploadArtifact
        end

        subgraph BrowserJob["Job: browser (Advisory)"]
            direction TB
            Playwright["Playwright Browser Suite<br/>• 8 parallel shards<br/>• Non-blocking (advisory on main)<br/>• Reports failures to GitHub Issue"]
        end

        subgraph DeployJob["Job: deploy (Publish to Pages)"]
            direction TB
            HeadCheck["Confirm commit is still HEAD of main"]
            DeployPages["actions/deploy-pages<br/>• Writes to GitHub Pages CDN<br/>• Automatic 30s retry on transient error"]
            HeadCheck --> DeployPages
        end

        BuildJob -->|needs: build| DeployJob
        BuildJob -.->|parallel advisory| BrowserJob
    end

    subgraph VerifyWorkflow["verify-live.yml (Post-Deploy Proof)"]
        direction TB
        LiveProof["Probe Live Site<br/>• Verify live SHA & nonce match commit<br/>• Validate PMTiles byte-range requests<br/>• Run live browser smoke tests<br/>• File divergence issue if checks fail"]
    end

    Concurrency --> BuildJob
    DeployJob -->|workflow_run on success| VerifyWorkflow
```

### Detailed Breakdown of Workflow Files

#### A. `.github/workflows/deploy.yml`

This is the primary deployment workflow. It triggers automatically when code lands on the `main` branch:

1. **Paths Ignore**: It ignores edits to pure documentation files (like `docs/**`, `*.md`). Documentation updates do not alter code in `dist/`, avoiding unnecessary rebuilds.
2. **Concurrency Control**: It specifies `concurrency: group: pages, cancel-in-progress: true`. If multiple commits land in quick succession, older in-progress builds are cancelled so only the newest commit is deployed, preventing race conditions on GitHub Pages.
3. **Least Privilege Security**: The `build` job has read-only permissions (`contents: read`, `pages: read`). Only the specific `deploy` job is granted `pages: write` and `id-token: write` to authenticate with GitHub's OpenID Connect (OIDC) token issuer.
4. **Build & Gate**: It executes `npm ci` followed by `npm run gate`. If any TypeScript error, bundle size violation, or data inconsistency exists, the build halts and nothing is deployed.
5. **Publish to Pages**:
   - `actions/configure-pages`: Prepares GitHub Pages metadata.
   - `actions/upload-pages-artifact`: Packages `dist/`.
   - `actions/deploy-pages`: Publishes the packaged files directly to the GitHub Pages environment.

#### B. `.github/workflows/verify-live.yml`

A unique engineering practice in this repository is that **merging a commit is not considered proof that the release succeeded**.

- Once `deploy.yml` succeeds, `verify-live.yml` wakes up.
- It queries the public site (`https://atniclimate.github.io/dynamic-drought-module/` or configured domain).
- It verifies that the deployed commit SHA stamped on the page matches the repository SHA.
- It tests that the web server properly handles HTTP `Range` requests (vital for MapLibre streaming `.pmtiles` vector tiles without downloading whole gigabyte files).
- If divergence is detected, it automatically files a GitHub Issue alerting maintainers.

---

## 5. Local Developer Workflow: Running and Building Locally

If you want to test and run this application on your local machine:

### 1. Install Node.js

Ensure you have Node.js 24 installed. If you use `nvm` (Node Version Manager):

```bash
nvm install
nvm use
```

### 2. Install Project Dependencies

Run `npm ci` (rather than `npm install`) to ensure you install the exact versions locked in `package-lock.json`:

```bash
npm ci
```

### 3. Start the Interactive Local Development Server

```bash
npm run dev
```

Open `http://localhost:5173` in your browser. Any change you make to TypeScript, HTML, or CSS files will immediately update in your browser using Hot Module Replacement (HMR).

### 4. Build and Preview the Production Site

To test the exact static output that will be uploaded to GitHub Pages:

```bash
# 1. Typecheck and build the static bundle into dist/
npm run build

# 2. Preview the built dist/ folder on a local production-style server
npm run preview
```

Visit `http://localhost:4173`.

### 5. Run the Deterministic Quality Gate

Before pushing changes to GitHub, run:

```bash
npm run gate
```

This executes the exact checks that the GitHub Actions `deploy.yml` workflow will run in the cloud.

---

## 6. Summary: The Lifecycle at a Glance

1. **Write Code**: Developers edit TypeScript files in `src/` and assets in `public/`.
2. **Typecheck & Bundle**: `npm run build` runs `tsc` to verify type safety and `vite build` to generate static assets into `dist/`.
3. **Validate**: `npm run gate` ensures bundle size, schemas, and contracts pass.
4. **Continuous Deployment**: On push to `main`, GitHub Actions (`deploy.yml`) runs the gate, bundles `dist/`, and publishes it to GitHub Pages via `actions/deploy-pages`.
5. **Serve Client-Side**: Users open the site in their browser. The client browser executes MapLibre GL JS, streams vector tiles, and pulls live environmental data directly without needing a custom application server.
6. **Live Verification**: `verify-live.yml` probes the live site to ensure the deployed bytes, build SHA, and tile-range queries are healthy.

---

## 7. Architectural Variations Across Projects

While the **Dynamic Drought Module** illustrates a full-scale Node.js/Vite CI pipeline, serverless static delivery on GitHub Pages accommodates several lighter or specialized architectures across the ATNI project portfolio:

```mermaid
flowchart TD
    Start["How do you want to build and deploy?"] --> Q1{"Requires build or compilation?"}
    
    Q1 -->|No: Pure Vanilla HTML/JS| PatternA["Pattern A: Zero-Build Direct<br/>(TieredSovereignDataFramework)<br/>• Author in docs/<br/>• Deploy via main:/docs"]
    Q1 -->|Yes| Q2{"Build engine & toolchain?"}
    
    Q2 -->|Python Tooling| Q3{"Deploy mechanism?"}
    Q3 -->|Native GitHub Pages| PatternB["Pattern B: Local Python Generator<br/>(Climate Curriculum)<br/>• python source/build.py -> docs/<br/>• Deploy via main:/docs with .nojekyll"]
    Q3 -->|GitHub Actions CI Gate| PatternC["Pattern C: Gated Isolated Root<br/>(ATNI Task Force)<br/>• Local rebuild_all.py -> site/<br/>• CI runs validate_public.py<br/>• Actions deploys path: site"]

    Q2 -->|Node / TypeScript / Bundler| Q4{"External API secrets or CORS required?"}
    Q4 -->|No: Public APIs / Static Tiles| PatternBase["Baseline: Full Cloud CI/CD<br/>(Dynamic Drought Module)<br/>• GitHub Actions builds dist/<br/>• actions/deploy-pages + verify-live"]
    Q4 -->|Yes: Gated Federal APIs| PatternD["Pattern D: Hybrid Edge Proxy<br/>(Policy Sentinel)<br/>• Vite bundles into docs/<br/>• Cloudflare Worker proxies private API keys"]
```

### Pattern A: Zero-Build Direct Static Authoring (`TieredSovereignDataFramework`)

- **Reference**: [TieredSovereignDataFramework](https://atniclimate.github.io/TieredSovereignDataFramework/)
- **Use Case**: Lightweight analytical sites, interactive framework guides, or decision trees that do not require module bundling or transpilation.
- **Workflow**: Authors write standard HTML5, CSS3, and ES6 JavaScript directly inside the `docs/` folder (`index.html`, `styles.css`, `app.js`).
- **Deployment**: Configured via native GitHub Pages settings pointing directly to the `main` branch `/docs` folder. No GitHub Actions workflows (`.github/workflows/`), npm dependencies, or build runners are involved.
- **Benefits**: Zero build latency, zero third-party dependency vulnerabilities, and immediate updates upon push.

### Pattern B: Local Python Generation with Deterministic Quality Gates (`climate-curriculum`)

- **Reference**: [Climate Curriculum](https://atniclimate.github.io/climate-curriculum/)
- **Use Case**: Educational or research modules where templates, vector graphics (e.g., SVG geometries), and static data are maintained with Python scripts.
- **Workflow**:
  1. Developers compile editable templates (`source/template.html`) and geospatial data (`source/columbia_svg.json`) into `docs/index.html` by running a local Python script (`python source/build.py`).
  2. Local deterministic checks (`tools/check.py` and Playwright `tools/probe.js`) run before committing to verify strict constraints: zero external network dependencies, ATNI editorial styles, layout responsiveness, and accessibility (a11y).
- **Deployment**: Published via native GitHub Pages (`main:/docs`). The presence of `docs/.nojekyll` ensures GitHub Pages serves raw SVG, font, and asset directories directly without Jekyll interference.
- **Benefits**: Self-contained single-file delivery that operates 100% offline (e.g., in tribal school classrooms or low-connectivity environments) with user state saved in browser `localStorage`.

### Pattern C: Isolated Subdirectory with CI Boundary Gates (`atni-task-force`)

- **Reference**: [ATNI Task Force](https://atniclimate.github.io/atni-task-force/)
- **Use Case**: Multi-tier data projects where sensitive notes, planning documents, or raw registries must remain strictly segregated from public deliverables.
- **Workflow**:
  1. Maintainers compile open claims locally using a Python script orchestrator (`scripts/rebuild_all.py`), generating static HTML, data plates, explorer blocks, and briefing PDFs into an isolated `site/` folder.
  2. Commits pushed to `main` trigger `.github/workflows/pages.yml`. The runner executes `scripts/validate_public.py` using Python 3.12, enforcing schema compliance, link safety, and verifying that no Tier 1 (internal community network) text or confidential data has leaked into public files.
  3. If all validation checks pass, `actions/upload-pages-artifact` packages only `path: site` (with `include-hidden-files: true` to preserve `site/.nojekyll`), and `actions/deploy-pages` publishes the bundle.
- **Benefits**: Internal working files, planning drafts, build scripts, and tests remain in the repository root without ever being uploaded to the public web server.

### Pattern D: Hybrid Static SPA with Serverless Edge Proxy (`policy-sentinel`)

- **Reference**: [Policy Sentinel](https://atniclimate.github.io/policy-sentinel/)
- **Use Case**: Client-side interactive applications that require authenticated access to external APIs with secret keys, rate limits, or strict CORS policies (e.g., GovInfo, Congress.gov, Regulations.gov).
- **The Problem**: GitHub Pages is purely client-side; embedding an API key in client JavaScript leaks the secret publicly to anyone inspecting browser network traffic.
- **The Solution**:
  1. **Frontend**: A Preact/TypeScript application is compiled locally with Vite (`vite.demo.config.ts`, `npm run demo:build`) into `docs/` and published via native GitHub Pages (`main:/docs`). A local gate script (`scripts/finish-demo-build.mjs`) packages licenses into `docs/THIRD-PARTY-NOTICES.txt` and verifies that no secrets or analytics scripts leak into the bundle.
  2. **Edge Proxy**: A lightweight serverless proxy (Cloudflare Worker configured in `worker/wrangler.toml`) runs at the network edge. It validates requesting origin domains, securely injects the private `DATA_GOV_API_KEY`, handles CORS, and implements version-scoped response caching.
  3. **Verification**: A post-deployment browser audit script (`scripts/verify-demo-browser.mjs`) tests the live production URL for automated WCAG accessibility (via axe) and Content Security Policy (CSP) integrity.

---

### Comparative Architecture Matrix

| Dimension | Baseline ([`dynamic-drought-module`](https://atniclimate.github.io/dynamic-drought-module/)) | Zero-Build ([`Tiered Sovereign Data Framework`](https://atniclimate.github.io/TieredSovereignDataFramework/)) | Local Python ([`climate-curriculum`](https://atniclimate.github.io/climate-curriculum/)) | Gated Isolated Root ([`atni-task-force`](https://atniclimate.github.io/atni-task-force/)) | Hybrid Edge Proxy ([`policy-sentinel`](https://atniclimate.github.io/policy-sentinel/)) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Purpose** | High-performance interactive geospatial mapping | Sovereign data framework guide & decision tool | Offline-capable climate education module | Regional energy & tech policy coordination library | Federal policy intelligence & document analysis |
| **Source Directory** | `src/` (TypeScript, SCSS) | `docs/` (Vanilla JS, CSS) | `source/` (`template.html`, JSON) | `scripts/` & open data files | `demo/` (Preact, TypeScript) |
| **Build Toolchain** | Node.js, `npm`, Vite, `tsc` | None (Zero build step) | Python 3 (`build.py`) | Python 3 (`rebuild_all.py`) | Vite (`vite.demo.config.ts`) |
| **Build Environment** | Cloud CI (GitHub Actions runner) | None | Local workstation | Local workstation | Local workstation |
| **Publishing Target** | Ephemeral `dist/` | Tracked `docs/` | Tracked `docs/` | Tracked `site/` | Tracked `docs/` |
| **Deployment Method** | GitHub Actions (`deploy.yml` + OIDC) | Native Pages (`main:/docs`) | Native Pages (`main:/docs`) | GitHub Actions (`pages.yml` with `path: site`) | Native Pages (`main:/docs`) |
| **Jekyll Bypass** | Handled by Actions artifact | Handled automatically | Required (`docs/.nojekyll`) | Required (`site/.nojekyll`) | Required (`docs/.nojekyll`) |
| **Quality & Security Gates** | CI: `npm run gate` (bundle budgets, unit contracts) | None | Local: `check.py` & Playwright layout/a11y probes | CI: `validate_public.py` (checks T1 data leaks & schemas) | Local: `finish-demo-build.mjs` (token & pixel scans) |
| **Data & API Architecture** | Direct public APIs & streamed PMTiles vector tiles | Embedded static JSON & client-side DOM rendering | Inlined SVG geometry & browser `localStorage` | Embedded JSON registry & static briefing PDFs | Cloudflare Worker edge proxy injecting private API keys |
| **Post-Deploy Audit** | `verify-live.yml` (DOM SHA & HTTP Range tests) | Manual browser inspection | Local Playwright probe suite | Local preview server inspection | `verify-demo-browser.mjs` (axe WCAG & CSP audit) |

---

### Key Takeaways for Serverless Publishing

1. **Choosing Between Native `/docs` and GitHub Actions (`actions/deploy-pages`)**:
   - **Use Native `/docs`** if you prefer committing built static assets or zero-dependency files directly to Git. It provides instant deployments with zero CI runner minutes.
   - **Use GitHub Actions (`actions/deploy-pages`)** if you want to keep compiled artifacts out of Git history (e.g., ephemeral `dist/`), build on the cloud runner, isolate publishing to a custom folder (e.g., `site/`), or enforce automated quality/governance gates before publishing.

2. **Jekyll Bypass (`.nojekyll`) Hygiene**:
   - GitHub Pages enables Jekyll processing by default, which ignores folders or filenames beginning with underscores (e.g., `_assets/`, `_kernel/`) or periods. Adding an empty `.nojekyll` file to the root of the published directory (`docs/.nojekyll` or `site/.nojekyll`) ensures that all assets serve as intended.

3. **Managing Secrets in Serverless Frontends**:
   - A static frontend hosted on GitHub Pages cannot securely hold confidential API keys; any key included in client JavaScript is visible to visitors.
   - When private APIs or strict CORS endpoints are necessary, pair the static frontend with a serverless edge worker (such as Cloudflare Workers or AWS Lambda@Edge) that injects credentials and manages rate limiting before forwarding data to the browser.

4. **Data Governance & Boundary Enforcement**:
   - In open repositories containing multiple tiers of sensitivity (such as the Tiered Sovereign Data Framework), use isolated publishing directories (`site/`) coupled with automated pre-deploy boundary scripts (`validate_public.py`) to mathematically guarantee that internal drafts, community notes, or unredacted files are never deployed to public CDNs.
