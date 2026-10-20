---
title: "R in VS Code with Radian"
parent: "R Language"
nav_order: 8
---

# R in VS Code with Radian

- [R in Visual Studio Code](https://code.visualstudio.com/docs/languages/r)
- [Interactive R Programming in VSCode (Datanovia)](https://www.datanovia.com/books/r-in-vscode/interactive-r-programming-and-running-code-in-vscode.html#google_vignette)
- [Setup Visual Studio Code to run R on VSCode 2021 (R-Bloggers)](https://www.r-bloggers.com/2021/01/setup-visual-studio-code-to-run-r-on-vscode-2021/)
- [radian: a modern console for R](https://fromthebottomoftheheap.net/2019/06/18/radian-console-for-r/)
- [Rmarkdown Code Chunks](https://rmarkdown.rstudio.com/lesson-3.html)
- [VS Code: Add a Rmarkdown Code Chunk Snippet Key Binding](https://www.schmidtynotes.com/blog/r/2021-09-28-vscode-rmd-code-chunk-snippet/)

_[byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools)_  

## Radian and AI Environments

While you can use the enhanced R tool
[radian](https://github.com/randy3k/radian)
within
[AI environments](../AI/env.md), they are not as seamless as
[Posit's RStudio](https://posit.co/download/rstudio-desktop/).
In fact, `radian` can interfere with the "memory" and operation of these tools.

## Files and Setups

```bash
export PATH=$PATH:/usr/local/bin/radian
```

Some useful VS Code Settings for `settings.json` file:

```json
{
  "r.bracketedPast": true,
  "r.rterm.linux": "/usr/local/bin/radian",
  "r.rterm.mac": "/usr/local/bin/radian",
  "r.rterm.windows": "C:\\Users\\<username>\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\radian.exe",
  "r.alwaysUseActiveTerminal": true,
  "r.rterm.option": [
      "--no-save",
      "--no-restore",
      "--quiet",
      "--r-binary=/usr/local/bin/radian"
  ],
  "r.sessionWatcher": true,
  "r.sessionWatcher.showSavePrompt": false,
  "r.sessionWatcher.showRestartPrompt": false,
  "r.sessionWatcher.showRestartConfirmation": false
}
```

In the `.Rprofile` in home directory, add this line:

```r
options(radian.complete_while_typing = FALSE)
```
