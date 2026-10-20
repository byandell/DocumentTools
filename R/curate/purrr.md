---
title: "purrr Package Example"
parent: "Curate R Data"
grand_parent: "R Language"
nav_order: 5
---

# purrr Package Example

The `dplyr` package acts on data frames, `filter`ing rows and `select`ing columns as one would in a database. The `purrr` package acts on lists, including data frames. The cool thing is that the lists may contain rather complicated objects. There is now a [purrr cheatsheat](https://github.com/rstudio/cheatsheets/raw/master/purrr.pdf) ⚠️ Below is a made-up example to illustrate some features.


``` r
library(purrr)
library(dplyr)
library(tidyr)
```


Let's create some fake data. Here `x` is random and `y` equals column number + `x` + noise.


``` r
nc <- 5
nr <- 10
```


``` r
x <- as.list(seq_len(nc))
```



``` r
x <- as.data.frame(matrix(rnorm(nr * nc), nr, nc))
x <- as.data.frame(x)
```


``` r
y <- t(seq_len(nc) + t(x) * seq_len(nc)) + 
  matrix(rnorm(nr * nc,, 0.001), nr, nc)
y <- as.data.frame(y)
```

Now we want to run a regress of each column of `x` on each column of `y` and report out the coefficients. This could be done in a loop, but let's instead imagine what we would do with a single column.


``` r
lm_coef <- function(x1, y1) {
  dat <- data.frame(x = x1, y = y1)
  coef(lm(y ~ x, dat))
}
```


``` r
lm_coef(x[,1], y[,1])
```

```
## (Intercept)           x 
##    1.000270    0.999616
```

We want to combine `x` and `y` into one list. We first make a list of lists, then transpoe it.


``` r
xy <- list(x = as.list(x), y = as.list(y))
str(xy)
```

```
## List of 2
##  $ x:List of 5
##   ..$ V1: num [1:10] 0.3023 0.5069 0.4507 0.2571 0.0841 ...
##   ..$ V2: num [1:10] -0.00606 0.34345 -0.82974 -2.13689 1.16764 ...
##   ..$ V3: num [1:10] 0.668 1.37 -0.705 0.903 0.251 ...
##   ..$ V4: num [1:10] -0.541 0.756 -1.147 0.988 -0.332 ...
##   ..$ V5: num [1:10] 1.338 0.935 -0.224 1.878 -1.074 ...
##  $ y:List of 5
##   ..$ V1: num [1:10] 1.3 1.51 1.45 1.26 1.08 ...
##   ..$ V2: num [1:10] 1.987 2.687 0.341 -2.273 4.334 ...
##   ..$ V3: num [1:10] 5.006 7.109 0.887 5.71 3.752 ...
##   ..$ V4: num [1:10] 1.838 7.023 -0.587 7.951 2.671 ...
##   ..$ V5: num [1:10] 11.69 9.67 3.88 14.39 -0.37 ...
```


``` r
xy <- xy %>%
  transpose
str(xy)
```

```
## List of 5
##  $ V1:List of 2
##   ..$ x: num [1:10] 0.3023 0.5069 0.4507 0.2571 0.0841 ...
##   ..$ y: num [1:10] 1.3 1.51 1.45 1.26 1.08 ...
##  $ V2:List of 2
##   ..$ x: num [1:10] -0.00606 0.34345 -0.82974 -2.13689 1.16764 ...
##   ..$ y: num [1:10] 1.987 2.687 0.341 -2.273 4.334 ...
##  $ V3:List of 2
##   ..$ x: num [1:10] 0.668 1.37 -0.705 0.903 0.251 ...
##   ..$ y: num [1:10] 5.006 7.109 0.887 5.71 3.752 ...
##  $ V4:List of 2
##   ..$ x: num [1:10] -0.541 0.756 -1.147 0.988 -0.332 ...
##   ..$ y: num [1:10] 1.838 7.023 -0.587 7.951 2.671 ...
##  $ V5:List of 2
##   ..$ x: num [1:10] 1.338 0.935 -0.224 1.878 -1.074 ...
##   ..$ y: num [1:10] 11.69 9.67 3.88 14.39 -0.37 ...
```


``` r
xy %>% 
  map(function(dat) coef(lm(y~x, dat)))
```

```
## $V1
## (Intercept)           x 
##    1.000270    0.999616 
## 
## $V2
## (Intercept)           x 
##    1.999665    1.999740 
## 
## $V3
## (Intercept)           x 
##    3.000298    2.999580 
## 
## $V4
## (Intercept)           x 
##    4.000027    3.999754 
## 
## $V5
## (Intercept)           x 
##    5.000061    4.999921
```

This can also be done in two steps. At the end, we organize data a bit.



``` r
xy %>% 
  map(function(dat) lm(y~x, dat)) %>%
  map(coef) %>%
  as.data.frame %>%
  t
```

```
##    (Intercept)        x
## V1    1.000270 0.999616
## V2    1.999665 1.999740
## V3    3.000298 2.999580
## V4    4.000027 3.999754
## V5    5.000061 4.999921
```

## Redo with dplyr

Of course all the above can be done readily with `dplyr` and `tidyr` using `group_by` and `do`, as shown below. However, two things are useful to consider:

* While `summarize` works for single value operations, you must use `do` for multiple value operations. It is challenging to get `do` correct, as it must return a one-row data frame.
* The `purrr` verbs `map` and `transpose` do not require the lists to be the same length or configuration. Thus, they can be used in a variety of settings where `dplyr`, working on data frames, cannot.


``` r
xx <- x %>%
  gather(var, xval)
yy <- y %>%
  gather(var, yval)
xx$yval <- yy$yval
```



``` r
xx %>% 
  group_by(var) %>%
  do(
    as.data.frame(
    t(
      coef(
        lm(yval ~ xval, .)))))
```

```
## # A tibble: 5 × 3
## # Groups:   var [5]
##   var   `(Intercept)`  xval
##   <chr>         <dbl> <dbl>
## 1 V1             1.00 1.000
## 2 V2             2.00 2.00 
## 3 V3             3.00 3.00 
## 4 V4             4.00 4.00 
## 5 V5             5.00 5.00
```

## A more complicated example

This example can be found in the [hotspot.R](https://github.com/byandell/qtl2shiny/blob/master/R/hotspot.R) file of package [qtl2shiny](https://github.com/byandell/qtl2shiny).

We start with two objects -- `chr_pos` has positions within each chromosome, `peaks` has information about what traits have peaks where on each chromosome -- that are lists by chromosome. [The `peaks` object is turned into a list by use of `split`.] We transpose a "list of lists" so that `out_chr` is also a list by chromosome, having elements from the two objects.


``` r
out_chr <- purrr::transpose(list(pos = chr_pos, 
                                   peaks = split(peaks, peaks$chr)))
```

Now we create a new object `out_peaks` by counting peaks at each position along each chromosome. The `map` function acts across the list indexed by chromosome.  Notice that the call to `peaks_type`, done for each chromosome, uses elements `x$pos` and `x$peaks` from each element of `out_chr`. Recall the `pos` and `peaks` objects have rather different shapes.


``` r
out_peaks <- purrr::map(out_chr,
                        function(x, peak_window) 
                          peaks_type(x$pos, x$peaks, peak_window),
                        peak_window)
```

The routine `peaks_type` first `split`s the `peaks` by `pheno_type`, then `map`s a function `outer_window` (not shown here) for each element of `peaks_by_type`.


``` r
peaks_by_type <- split(peaks, peaks$pheno_type)
out <- purrr::map(peaks_by_type,
                  outer_window,
                  posi, peak_window)
```

Later on, `peaks_type` uses `map` again for another summary.

The point here is not to follow the details, but to notice how `map` can be used to isolate thinking about a particular task. Then you can concentrate on solving that task without worrying about a bunch of indexing and looping.
