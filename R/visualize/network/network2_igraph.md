---
title: "igraph Network Visualization (Dataset 2)"
parent: "Network Observatins in Connected Graphs"
grand_parent: "Visualize Data with R"
nav_order: 3
---

# igraph Network Visualization (Dataset 2)

Examples pulled from **Network Visualization with R**, [Polnet 2016](http://www.kateto.net/polnet2016) by Katya Ognyanova.


``` r
suppressPackageStartupMessages({
  library(RColorBrewer)
  library(readr)
  library(dplyr)
  library(igraph)
})
```


``` r
data_dir <- "Data files"
```

For igraph plotting parameters, node options start with `vertex.` and edge options start with `edge.`. Get options with


``` r
?igraph.plotting
```

Set node & edge options in two ways:

1. specify them in `plot()` function
2. add them to the `igraph` object

### igraph with Dataset 2


``` r
nodes2 <- read_csv(file.path(data_dir, 
                              "Dataset2-Media-User-Example-NODES.csv"))
## First row is names, so need to use read.csv.
links2 <- read.csv(file.path(data_dir, 
                              "Dataset2-Media-User-Example-EDGES.csv"),
                   header = TRUE, 
                   row.names = 1)
```

Create a igraph network object from the two-mode matrix: 


``` r
net2 <- graph_from_incidence_matrix(links2)
```

```
## Error in `biadjacency_impl()`:
## ! 'list' object cannot be coerced to type 'double'
```

Built-in vertex attribute 'type' shows which mode vertices belong to.


``` r
table(V(net2)$type)
```

```
## Error:
## ! object 'net2' not found
```


``` r
plot(net2,vertex.label=NA)
```

```
## Error:
## ! object 'net2' not found
```

To transform a one-mode network matrix into an igraph object,
use `graph_from_adjacency_matrix()`.

### Identify Media Outlets and Users

Modify network object visual properties -- color, size and shape. 
Media outlets are squares; users are circles.


``` r
# Media outlets are blue squares, audience nodes are orange circles:
V(net2)$color <- c("steel blue", "orange")[V(net2)$type+1]
```

```
## Error:
## ! object 'net2' not found
```

``` r
V(net2)$shape <- c("square", "circle")[V(net2)$type+1]
```

```
## Error:
## ! object 'net2' not found
```

``` r
# Media outlets will have name labels, audience members will not:
V(net2)$label <- ""
```

```
## Error:
## ! object 'net2' not found
```

``` r
V(net2)$label[V(net2)$type==F] <- nodes2$media[V(net2)$type==F] 
```

```
## Error:
## ! object 'net2' not found
```

``` r
V(net2)$label.cex=.6
```

```
## Error:
## ! object 'net2' not found
```

``` r
V(net2)$label.font=2
```

```
## Error:
## ! object 'net2' not found
```

``` r
plot(net2, vertex.label.color="white", vertex.size=(2-V(net2)$type)*8) 
```

```
## Error:
## ! object 'net2' not found
```

Text only for nodes.


``` r
plot(net2, 
     vertex.shape = "none", 
     vertex.label = nodes2$media,
     vertex.label.color = V(net2)$color, 
     vertex.label.font = 2, 
     vertex.label.cex = .6, 
     edge.color = "gray70",  
     edge.width = 2)
```

```
## Error:
## ! object 'net2' not found
```

### Generate bipartite projections

Calculate co-memberships by multiplying the network matrix by its transpose, or using `bipartite.projection()`.


``` r
(net2.bp <- bipartite.projection(net2)) 
```

```
## Error:
## ! object 'net2' not found
```


``` r
par(mfrow=c(1,2))
vtype <- c("media","users")[1 + is.na(nodes2$media.type)]
plot(net2.bp$proj1, 
     vertex.label.color = "black", 
     vertex.label.dist = 1,
     vertex.label = nodes2$media[vtype == "media"])
```

```
## Error:
## ! object 'net2.bp' not found
```

``` r
plot(net2.bp$proj2, 
     vertex.label.color = "black", 
     vertex.label.dist = 1,
     vertex.label = nodes2$media[vtype == "users"]) 
```

```
## Error:
## ! object 'net2.bp' not found
```

Now force layout to be the same and drop shapes.


``` r
par(mfrow=c(1,2))
lay <- layout_with_fr(net2)
```

```
## Error:
## ! object 'net2' not found
```

``` r
plot(net2.bp$proj1, 
     vertex.shape = "none", 
     vertex.label.color = "black", 
     vertex.label.dist = 1,
     vertex.label = nodes2$media[vtype == "media"],
     layout = lay[vtype == "media",])
```

```
## Error:
## ! object 'net2.bp' not found
```

``` r
plot(net2.bp$proj2, 
     vertex.shape = "none", 
     vertex.label.color = "red", 
     vertex.label.dist = 1,
     vertex.label = nodes2$media[vtype == "users"],
     layout = lay[vtype == "users",]) 
```

```
## Error:
## ! object 'net2.bp' not found
```
