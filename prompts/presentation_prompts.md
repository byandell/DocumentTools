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

This workflow transforms existing markdown notes into a styled, interactive Reveal.js presentation with a modern aesthetic and custom typography.

### Prompt and Response

**Prompt:**
> "Create a quarto slide deck from `[slidedeck].md` in light mode and place it in folder `quarto/` as `[slidedeck].qmd`. Adjust slide styling to use a more compact layout so that content fits neatly on each slide. Do not use `chalkboard` features, instead embed all resources. Update `.gitignore` for quarto documents as needed."

**Key Configurations & Structure:**

1. **Quarto Slide Deck (`[slidedeck].qmd`)**:
   - Converted to the modern web-based **Reveal.js** format.
   - Structured into logical sections using background-colored slide breaks (`# Section Title {background-color="..."}`).
   - Utilizes advanced Quarto features such as column layouts (`::: {.columns}`), callout boxes, and incremental lists (`::: {.incremental}`).
   - Adjusts all relative file links to match the subdirectory structure.

2. **Custom Presentation Styling ([quarto/custom.scss](../quarto/custom.scss))**:
   - Designed a premium dark-mode aesthetic using Slate and Sky/Rose accents.
   - Customized typography using modern sans-serif fonts (`Outfit`, `Inter`).
   - Added glowing shadows and rounded borders to code blocks, and styled Quarto callouts to pop against dark backgrounds.

3. **Rendered Output**:
   - Compiled using `quarto render quarto/[slidedeck].qmd` to ensure syntax validity.

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
