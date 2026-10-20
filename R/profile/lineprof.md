---
title: "Memory Profiling with lineprof"
parent: "Profile & Simulate"
grand_parent: "R Language"
nav_order: 2
---

# Memory Profiling with lineprof

This is taken directly from <http://adv-r.had.co.nz/Profiling.html>.


``` r
library(lineprof)
```

```
## Error in `library()`:
## ! there is no package called 'lineprof'
```

``` r
f <- function() {
  pause(0.1)
  g()
  h()
}
g <- function() {
  pause(0.1)
  h()
}
h <- function() {
  pause(0.1)
}
```


``` r
tmp <- tempfile()
Rprof(tmp, interval = 0.1)
f()
```

```
## Error in `pause()`:
## ! could not find function "pause"
```

``` r
Rprof(NULL)
```


``` r
file.show(tmp)
```


``` r
(l <- lineprof(f()))
```

```
## Error in `lineprof()`:
## ! could not find function "lineprof"
```


``` r
shine(l)
```

