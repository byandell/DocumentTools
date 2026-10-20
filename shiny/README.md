---
title: "Shiny Apps"
parent: "Document Tools"
nav_order: 5
has_children: true
permalink: /shiny/
---

# Shiny Apps

Shiny apps are cool, but they can get complicated, and frustrating to debug.
Complicated apps--longer than 500 lines of code--can
have subtle paradoxes caused by reactive elements.
It is helpful to think carefully about how to modularize apps,
much as we do with functions, so that we can debug piece by piece.

R language apps developed with collaborators by [Brian Yandell](https://github.com/byandell)
using the
[Shiny](https://shiny.posit.co/)
package
illustrate in various ways an evoling design over time,
which made the apps easier
to use, understand and debug.
These repos include some lessons learned that hopefully will
help others as they design and evolve apps for this project.
For those interested in comparing shiny apps built in R vs. python,
there is a useful development in the
[Shiny Geyser App](https://github.com/byandell/geyser)
repo.

The best reference for building shiny apps is
[Mastering Shiny](https://mastering-shiny.org),
with particular attention to Ch 19 on
[Shiny modules](https://mastering-shiny.org/scaling-modules.html).
See also
[Modularizing Shiny app code](https://shiny.rstudio.com/articles/modules.html).
Yandell's key working repos that inform this document are

## Shiny App Overviews

- [View Shiny Apps Slides](https://byandell.github.io/DocumentTools/quarto/ShinyApps.html)
- [geyser: modular concepts and construction](geyser.md)
- [foundrShiny: pragmatic code reuse driven by collaborators](foundrShiny.md)
- [qtl2shiny: localized QTL analysis and visualization](qtl2shiny.md)

## Shiny App Examples

- [Shiny Geyser App with and without Modules](https://byandell.github.io/geyser/)
- [Founder Shiny App](https://byandell-sysgen.github.io/foundrShiny)
- [Shiny app for R/qtl2](https://byandell-sysgen.github.io/qtl2shiny)
- [Learning about Shiny Modules](https://github.com/byandell/shiny_module)
- [Helper Apps](https://github.com/byandell/helperApps)
- [Scaled QTL Visualizers (qtlApp)](https://github.com/AttieLab-Systems-Genetics/qtlApp)
