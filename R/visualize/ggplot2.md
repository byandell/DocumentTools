---
title: "ggplot2 Visualization"
parent: "Visualize Data with R"
grand_parent: "R Language"
nav_order: 1
---

# ggplot2 Visualization

## General thoughts on visualizing data

- [Visualizing Data from Data Carpentry](http://www.datacarpentry.org/R-ecology-lesson/04-visualization-ggplot2.html) ⚠️
- [Michael Deutsch Real-life Data Visualization](https://www.slideshare.net/mdeutschmtl/2012-04-data-viz-for-insy442-final)
- <http://gapminder.org> | [GapMinder World](http://www.gapminder.org/world) | [GapMinderDev](https://www.gapminderdev.org/) | [Hans Rosling TED Talk](http://www.gapminder.org/videos/ted-us-state-department/)
- [The Grammar of Graphics by Leland Wilkinson](https://www.cs.uic.edu/~wilkinson/TheGrammarOfGraphics/GOG.html) ⚠️

## ggplot2

- [ggplot2 Tutorial by Jenny Bryan](https://github.com/jennybc/ggplot2-tutorial)
    + [Jenny Bryan's Graph Things](http://stat545.com/graph00_index.html)
    + [Graph Dos and Don'ts](http://stat545-ubc.github.io/block015_graph-dos-donts.html) ⚠️
- [bar charts](http://ggplot2.tidyverse.org/reference/geom_bar.html) | [position_dodge](http://ggplot2.tidyverse.org/reference/position_dodge.html) | [Layout panels in grid](http://ggplot2.tidyverse.org/reference/facet_grid.html)

## ggplot2 examples

- Sarah Stevens [plot](https://drive.google.com/open?id=0Bwlo0AMx9pqmSWF0TDd4cXhUUTQ) | [
[code](https://drive.google.com/open?id=0Bwlo0AMx9pqmb2pxbk9wSndDa28) ⚠️
- [Graphics by Examples](http://www.ats.ucla.edu/stat/r/gbe/) ⚠️: [boxplot](http://www.ats.ucla.edu/stat/r/gbe/ggplot_boxplot.htm) ⚠️


## Interactive graphics

- [plotly](https://plot.ly/ggplot2/) | [Plotly Book (Casper Sievert)](https://cpsievert.github.io/plotly_book) ⚠️
- [ggvis](http://blog.revolutionanalytics.com/2014/06/interactive-web-ready-ggplot2-style-graphics-with-ggvis.html) ⚠️)
- [D3 HeatMap](https://github.com/rstudio/d3heatmap/blob/master/README.md) | [Shiny D3 Heatmap](http://www.htmlwidgets.org/showcase_d3heatmap.html) ⚠️

## Multiple plots

- [cowplot](https://cran.r-project.org/web/packages/cowplot/vignettes/introduction.html) | [plots on grid](https://cran.r-project.org/web/packages/cowplot/vignettes/plot_grid.html) ⚠️
- [cowplot, gridExtra & Viewport tutorial](http://www.sthda.com/english/wiki/ggplot2-easy-way-to-mix-multiple-graphs-on-the-same-page-r-software-and-data-visualization)
- [GGally](https://ggobi.github.io/ggally/)
- [grid viewports](https://stat.ethz.ch/R-manual/R-devel/library/grid/doc/viewports.pdf)
- ggplot2 workarounds
    + [Mixing ggplot2 graphs with other graphical output](https://github.com/hadley/ggplot2/wiki/Mixing-ggplot2-graphs-with-other-graphical-output)
    + [Editing raw grid objects from a ggplot](https://github.com/hadley/ggplot2/wiki/Editing-raw-grid-objects-from-a-ggplot)

## color palletes (particularly color blind)

- [ColorBrewer](http://colorbrewer2.org/) | [scale_color_brewer()](http://docs.ggplot2.org/current/scale_brewer.html) ⚠️ | [Brewer Palettes Swatches](http://mkweb.bcgsc.ca/brewer/swatches/brewer-palettes-swatches.pdf) ⚠️
- [ggsci](https://cran.r-project.org/web/packages/ggsci/vignettes/ggsci.html) (several color pallettes modeled after NPG, AAAS, etc. Also includes two themes for Rick & Morty as well as The Simpsons)
- [viridis](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html) (another set of color schemes that are logically selected to be color-blind friendly and have an even transition between colors.)

## Other gg packages

- [ggalt](https://github.com/hrbrmstr/ggalt)
- [ggtree](https://guangchuangyu.github.io/ggtree/) ⚠️ | [ggdendro](https://cran.r-project.org/web/packages/ggdendro/vignettes/ggdendro.html)
- [ggExtra](https://github.com/daattali/ggExtra)
- [vcfR](https://cran.r-project.org/web/packages/vcfR/vignettes/intro_to_vcfR.html)

## Heatmaps

- pretty heatmaps with [pheatmap](https://github.com/raivokolde/pheatmap)
- [Gplots and heatmap.2 for heatmaps](https://cran.r-project.org/web/packages/gplots/)

---

## Dynamic & Scientific Graphics References

Visualization is the key to quick insights with data:

- **Interactive Frameworks & D3**:
  - [d3: Data-Driven Documents](http://d3js.org)
  - [Interactive Graphics With D3 (Karl Broman)](http://www.biostat.wisc.edu/~kbroman/presentations/InteractiveGraphs3/) ⚠️
  - [D3 Graphics Gallery & Tutorials](https://github.com/mbostock/d3/wiki/Gallery)
- **Effective Presentation Principles**:
  - [How to Display Data Badly & Top 10 Worst Graphs (Karl Broman)](http://www.biostat.wisc.edu/~kbroman/topten_worstgraphs/) ⚠️
  - [Edward Tufte: Visual Explanations](http://www.edwardtufte.com/tufte/)
  - [Six Simple Techniques for Presenting Data (Hans Rosling)](http://sixminutes.dlugan.com/six-simple-techniques-for-presenting-data-hans-rosling-ted-2006/)
- **Biological & Network Visualization Tools**:
  - [Circos Circular Visualization](http://circos.ca/) ⚠️
  - [Cytoscape Network Visualizer](http://www.cytoscape.org/)
  - [igraph R Library](http://igraph.org/)

