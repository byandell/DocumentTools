---
title: "visNetwork Interactive Visualization"
parent: "Visualize Data with R"
grand_parent: "R Language"
nav_order: 5
---

# visNetwork Interactive Visualization

> **Interactive Widget**: An interactive version of this network visualization is available at [Open Interactive Visualization](network_visNetwork.html).

Examples pulled from **Network Visualization with R**, [Polnet 2016](http://www.kateto.net/polnet2016) by Katya Ognyanova.


``` r
suppressPackageStartupMessages({
  library(RColorBrewer)
  library(readr)
  library(dplyr)
  library('visNetwork') 
})
```


``` r
data_dir <- "Data files"
```

Here use [visNetwork](http://datastorm-open.github.io/visNetwork/) package.
visNetwork enables setting graphic properties as node or edge attributes by adding them as data columns before calling `visNetwork()`. See available options with:


``` r
?visNodes
?visEdges
```

For more information, see:


``` r
?visOptions # available options 
?visLayout  # available layouts
?visGroups  # using node groups
?visLegend  # adding a legend
```

### Basic visNetwork with Dataset 1


``` r
nodes <- 
   read_csv(file.path(data_dir,
                      "Dataset1-Media-Example-NODES.csv"))
links <- 
   read_csv(file.path(data_dir, 
                      "Dataset1-Media-Example-EDGES.csv")) %>%
   group_by(from,to,type) %>%
   summarize(weight = sum(weight)) %>%
   ungroup %>%
   arrange(from,to)
```

Open dataset 1 with visNetwork.


``` r
visNetwork(nodes, links, width="100%", height="400px", main="Network!")
```

```
## Error in `loadNamespace()`:
## ! there is no package called 'webshot'
```

Changing some node parameters:

* shape (ellipse, circle, database, box, text, image, circularImage, diamond, dot, star, triangle, triangleDown, square, icon)
* color.background (node color)
* color.border (frame color)
* color.highlight (color on mouse click)
* color.hover (color on mouseover)


``` r
nodes$shape <- "dot"  
nodes$shadow <- TRUE # Nodes will drop shadow
nodes$title <- nodes$media # Text on click
nodes$label <- nodes$type.label # Node label
nodes$size <- nodes$audience.size # Node size
nodes$borderWidth <- 2 # Node border width

nodes$color.background <- c("slategrey", "tomato", "gold")[nodes$media.type]
nodes$color.border <- "black"
nodes$color.highlight.background <- "orange"
nodes$color.highlight.border <- "darkred"

visNetwork(nodes, links)
```

```
## Error in `loadNamespace()`:
## ! there is no package called 'webshot'
```

Set up hover option.


``` r
nodes$color.hover.background <- "green"
visNetwork(nodes, links) %>%
 visInteraction(hover = TRUE)
```

```
## Error in `loadNamespace()`:
## ! there is no package called 'webshot'
```

Change visual properties of edges.


``` r
links$width <- 1 + links$weight/8 # line width
links$color <- "gray"    # line color  
links$arrows <- "middle" # arrows: 'from', 'to', or 'middle'
links$smooth <- FALSE    # should the edges be curved?
links$shadow <- FALSE    # edge shadow

visNetwork(nodes, links)
```

```
## Error in `loadNamespace()`:
## ! there is no package called 'webshot'
```

`visNetwork` offers a number of other options in the `visOptions()` function. For instance, highlight all neighbors of a selected node (`highlightNearest`), or add a drop-down menu to select groups of nodes (`selectedBy`). The groups are based on data columns such as `type label`.


``` r
visNetwork(nodes, links) %>%
  visOptions(highlightNearest = TRUE, 
             selectedBy = "type.label")
```

```
## Error in `loadNamespace()`:
## ! there is no package called 'webshot'
```

