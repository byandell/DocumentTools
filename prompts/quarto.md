---
title: "Create Quarto Slides"
parent: "Prompt Examples"
nav_order: 3
---

# Create Quarto Slides

## Prompt and Response

**Prompt:** Create a quarto slide deck from `[slidedeck].md`
in light mode and place it in folder `quarto/` as `[slidedeck].qmd`.
Adjust slide styling to use a more compact layout so that content fits neatly on each slide.
Do not use `chalkboard` features, instead embed all resources.
Update `.gitignore` for quarto documents as needed.

**Response:**
I have created a Quarto slide deck based on the contents of `[slidedeck].qmd`.

Here is a summary of the files created and configured:

1. **Quarto Slide Deck**: `[slidedeck].qmd`
   - Converted to the modern web-based **Reveal.js** format.
   - Structured into logical sections using background-colored slide breaks (`# Section Title {background-color="..."}`).
   - Utilizes advanced Quarto features such as column layouts (`::: {.columns}`), callout boxes, and incremental lists (`::: {.incremental}`).
   - Adjusted all relative file links to match the new subdirectory structure.

2. **Custom Presentation Styling**: [quarto/custom.scss](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/custom.scss)
   - Designed a premium dark-mode aesthetic using Slate and Sky/Rose accents.
   - Customized typography using modern sans-serif fonts (`Outfit`, `Inter`).
   - Added glowing shadows and rounded borders to code blocks, and styled Quarto callouts nicely to pop against the dark background.

3. **Rendered Output**: `[slidedeck].html`
   - Compiled using `quarto render` to ensure syntax validity. It rendered successfully without errors.

### Slide Structure Overview

- **Section 1: Introduction & Core Concepts**
  - *Documenting AI Workflows*: Core principles of saving prompt/walkthrough files.
  - *Prompt Engineering Resources*: Reference links and guides.

- **Section 2: Saving Prompts & Agent Conversations**
  - *Saving Prompts and Walkthroughs*: Practical commands and real-world repository examples.
  - *AI Agent Conversation Structure*: Multi-turn prompt chaining and version control.
  - *System Instructions*: Config examples for Python (`scikit-learn` & `pandas`) and R (`tidyverse`).
  - *The CRAFT Framework*: Context, Role, Action, Format, and Tone, with the grant proposal example.
- **Section 3: Practical Prompt Examples**
  - *Documenting Files & Folders*: Automated README and TOC generation prompts.
  - *Convert DOCX to Markdown & Slides*: Pandoc conversion and Reveal.js slide deck generation.
  - *GitHub Prompts (Versioning Files)*: R file multi-version commit workflow.
  - *GitHub Prompts (Git Conflict Resolution)*: The "Git Hell" walkthrough prompt.
  - *Organizing a Workflow*: Transforming R workflows into functions in packages.
  - *Folder Documentation in ResearchDrive*: Balancing private RD directories with public GitHub documentation.

*[byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools)*  
