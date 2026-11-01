---
title: "Quarto & Presentation Prompts"
parent: "Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 2
---

# Quarto & Presentation Automation Prompts

This guide gathers prompts and workflows for automatically generating presentations from analysis pipelines and documentation, covering both web-based **Reveal.js** slide decks and Microsoft **PowerPoint** (`.pptx`) presentations.

---

## 1. Web-Based Reveal.js Presentations with Quarto

This workflow transforms existing documentation, PDF publications, or markdown notes into a styled, interactive Reveal.js presentation with a modern aesthetic, calibrated typography, and self-contained asset embedding.

### Prompts and Refinements

**Initial Generation Prompt:**
> "Create a quarto slide deck from `[slidedeck].md` (or article PDF in `data/`) in light mode and place it in folder `quarto/` as `[slidedeck].qmd`. Start by developing a staged outline based on the main sections. Adjust slide styling to use a compact layout so that content fits neatly on each slide. Do not use chalkboard features; instead embed all resources (`embed-resources: true`). Calibrate inline backtick code elements so their font size matches the visual height of surrounding text. Update `.gitignore` for quarto documents as needed."

**Production-Grade Refinement Directives:**
- **Typography & Back-Quoted Strings**: Calibrate inline monospace elements (`code:not(pre code)`) to `0.88em` with baseline alignment and inherited line height across paragraphs, list items, tables, and spans to match adjacent sans-serif font size without distorting vertical rhythm.
- **Figure Asset Sourcing**: Link directly to official CDN or publication URLs for high-resolution figures when available; Quarto dynamically base64-encodes them into the self-contained deck, avoiding large local binary files in version control.
- **Layout Architecture & Collision Prevention**: For complex conceptual overviews or multi-part hypotheses, use responsive 2×2 callout grids (`::: {.columns}`) or statistical cards (`.stat-card`) rather than tall SVG/Mermaid flowcharts to prevent browser clipping and hidden slide rendering collisions.
- **Slide Navigation & Overview**: Configure 16:9 widescreen slides with progress bars, slide numbers, and matrix overview mode (`O` key).

### Key Configurations & Structure

1. **Quarto Slide Deck (`quarto/[slidedeck].qmd`)**:
   - Web-based **Reveal.js** format with self-contained bundling:
     ```yaml
     format:
       revealjs:
         theme: [default, custom.scss]
         slide-number: true
         embed-resources: true
         width: 1600
         height: 900
         transition: fade
     ```
   - Structured into logical sections using background-colored slide breaks (`# Section Title {background-color="..."}`).
   - Utilizes advanced Quarto features such as column layouts (`::: {.columns}`), callout boxes, and incremental lists (`::: {.incremental}`).
   - Uses responsive 2×2 card or callout grids for multi-part hypotheses or methods to prevent SVG rendering collisions.
   - Adjusts all relative file links to match the subdirectory structure.

2. **Custom Presentation Styling ([quarto/custom.scss](../quarto/custom.scss))**:
   - **Light-Mode Scientific Aesthetic**: Clean Slate-50 background (`#f8fafc`), Slate-900 headings (`#0f172a`), Sky-600 links/accents (`#0284c7`), and subtle slate borders (`#e2e8f0`).
   - **Modern Font Pairing**: Google Fonts pairing with `Outfit` for presentation and slide headings, and `Inter` for body copy, tables, and statistics.
   - **Back-Quoted String Calibration (Inline Code)**: Monospace fonts inherently have taller x-heights and cap-heights than proportional sans-serif fonts. Calibrate inline backtick code elements to match surrounding text:
     ```scss
     // Inline code styling (backticks) - calibrated to match adjacent text size
     code:not(pre code) {
       font-family: var(--r-code-font, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace);
       font-size: 0.88em !important;
       background-color: #f1f5f9;
       padding: 0.06em 0.28em;
       border-radius: 4px;
       color: #0369a1;
       border: 1px solid #e2e8f0;
       vertical-align: baseline;
       line-height: inherit;
       font-weight: 500;
     }

     li code:not(pre code),
     p code:not(pre code),
     td code:not(pre code),
     th code:not(pre code),
     span code:not(pre code) {
       font-size: 0.88em !important;
     }
     ```
   - **Card & Compact Slide Utilities**: Includes `.stat-card` for KPI/metric highlights and `.compact-slide` class for high-density slides.

3. **Rendered Output, Verification & PDF Export**:
   - **Compile HTML**: Compile using `quarto render quarto/[slidedeck].qmd` (verifying exit code `0` and clean asset embedding).
   - **Presentation Navigation**:
     - `F`: Toggle full screen
     - `O`: Toggle slide overview matrix
     - `Space` / `Arrow Keys`: Advance slides
   - **Export to PDF (Headless Chrome — 11" × 8.5" Landscape)**:
     ```bash
     "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
       --headless \
       --run-all-compositor-stages-before-draw \
       --no-pdf-header-footer \
       --print-to-pdf="quarto/[slidedeck].pdf" \
       "file://$(pwd)/quarto/[slidedeck].html?print-pdf"
     ```
   - **Export to PDF (Browser Print Dialog)**:
     Open `quarto/[slidedeck].html?print-pdf` in Chrome/Safari/Edge, press `Cmd + P`, select *Save as PDF*, Layout: *Landscape*, Margins: *None*, and check *Background graphics*.

---

## 2. Automated PowerPoint Deck Generation from R Pipelines

This workflow automates the assembly of a Microsoft PowerPoint presentation (`.pptx`) directly from an R data analysis pipeline, embedding generated PNG figures, titles, tables of contents, and biological narrative slides.

### Case Study: Glucose Tolerance Test (GTT) Analysis Pipeline

*Date: 2026-03-19* (Updated: 2026-03-25)

**Execution Prompt Used:**
> "Run the prompt and do all the steps listed in `promptsAlan.md`. Make sure all software needed is installed."

### Consolidated Pipeline Instructions

1. **Data Initialization**:
   > Analyze Glucose Tolerance Test (GTT) data from the master spreadsheet `'NDNB-25 B6 and NZO Masterdate sheet v2 R.xlsx'`.

2. **Time-Course Line Graphs (Glucose, Insulin, & Log Ratio)**:
   > Generate time-course line graphs for GTT data at 0, 15, 30, and 120 minutes vs. time. Create separate plots for:
   > - **Glucose levels**
   > - **Insulin levels**
   > - **log(Insulin / Glucose) ratio**
   >
   > Output individual figures for both the **NZO** and **B6** strains across each of the three metrics (6 plots total). Map Vehicle-treated to black dots and lines, and Compound-treated to blue dots and lines. Include standard error bars.

3. **Cross-Sectional Scatter Plot**:
   > Create a cross-sectional scatter plot mapping **change in fasting glucose** (Y-axis) against **change in body weight** (X-axis) across all mice.
   > - Color NZO strain blue and B6 strain black.
   > - Drug-treated mice as circles, vehicle-treated as squares.
   > - Add linear regression lines for each of the 4 subgroups.
   > - Calculate and display Pearson correlation coefficients (`r`) and `p-values` on the plot.

4. **File Management**:
   > Format spaces to underscores (`Hsp90_GTT.R`), and explicitly add the `.R` extension.

5. **Presentation Generation via Quarto**:
   > Use Quarto to automatically generate a PowerPoint deck (`.pptx`) embedding all of the outputted PNG figures. Ensure the presentation includes:
   > - A two-column Table of Contents slide with functional intra-document hyperlinks.
   > - A background section on Gluconeogenesis, split across multiple clean slides with academic references.

6. **Insulin Baseline Normalization**:
   > Remove time 0 insulin baseline measurements and calculate two new subgroup metrics: the `Insulin / Insulin_0` ratio and log-regression residuals (`log(Insulin) ~ log(Insulin_0)`). Plot both over time, splitting NZO and B6 strains side-by-side using `facet_wrap`. Add these plots to the PowerPoint deck.
