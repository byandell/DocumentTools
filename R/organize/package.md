---
title: "R Packages"
parent: "Organize Data & Docs"
grand_parent: "R Language"
nav_order: 4
---

# R Packages

The `R` computing environment uses packages to organize objects into discrete sets. A package may have a combination of functions and datasets. The `base` package has the basic `R` tools.

Packages are collections of R functions, data, and compiled code in a well-defined format. Packages are installed onto your computer with `install.packages()`, which is done once. Packages are updated with `update.packages()`. Both these operations can be done within Rstudio from the `Packages` tab in the bottom-right pane of Rstudio.

The directory where packages are stored on your computer is called the library. Packages are attached from the library to your current workspace using the command `library()`. For more information see [packages vs. libraries](https://www.r-bloggers.com/packages-v-libraries-in-r/) and links therein.

To see what packages are attached, use


``` r
sessionInfo()
```

```
## R version 4.6.0 (2026-04-24)
## Platform: aarch64-apple-darwin23
## Running under: macOS Tahoe 26.6.2
## 
## Matrix products: default
## BLAS:   /Library/Frameworks/R.framework/Versions/4.6/Resources/lib/libRblas.0.dylib 
## LAPACK: /Library/Frameworks/R.framework/Versions/4.6/Resources/lib/libRlapack.dylib;  LAPACK version 3.12.1
## 
## locale:
## [1] C.UTF-8/C.UTF-8/C.UTF-8/C/C.UTF-8/C.UTF-8
## 
## time zone: America/Chicago
## tzcode source: internal
## 
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets  methods   base     
## 
## other attached packages:
## [1] ggplot2_4.0.3  purrr_1.2.2    tidyr_1.3.2    dplyr_1.2.1    readr_2.2.0   
## [6] rmarkdown_2.32 knitr_1.52    
## 
## loaded via a namespace (and not attached):
##  [1] Matrix_1.7-6       bit_4.6.0          gtable_0.3.6       compiler_4.6.0    
##  [5] crayon_1.5.3       tidyselect_1.2.1   dichromat_2.0-1    parallel_4.6.0    
##  [9] splines_4.6.0      scales_1.4.0       fastmap_1.2.0      lattice_0.23-1    
## [13] mime_0.13          R6_2.6.1           labeling_0.4.3     generics_0.1.4    
## [17] curl_8.0.0         backports_1.5.1    tibble_3.3.1       pillar_1.11.1     
## [21] RColorBrewer_1.1-3 tzdb_0.5.0         rlang_1.3.0        utf8_1.2.6        
## [25] broom_1.0.13       xfun_0.61          S7_0.2.2           bit64_4.8.6       
## [29] otel_0.2.0         cli_3.6.6          mgcv_1.9-4         withr_3.0.3       
## [33] magrittr_2.0.5     digest_0.6.39      grid_4.6.0         vroom_1.7.1       
## [37] hms_1.1.4          nlme_3.1-171       lifecycle_1.0.5    vctrs_0.7.3       
## [41] evaluate_1.0.5     glue_1.8.1         farver_2.1.2       tools_4.6.0       
## [45] pkgconfig_2.0.3    htmltools_0.5.9
```

The other packages automatically loaded are usually `stats` and `graphics`, and some other more arkane helpers, `grDevices`, `utils`, and `methods`.
Note that a number of packages may be `loaded via a namespace (and not attached)`, which means they are used indirectly by some other attached package. Each package has appended its version number after `-`.

## The `datasets` package

All `R` distributions provide the `datasets` packages which only contains sample datasets.
In an interactive session `help` will bring up the index of help pages for the `datasets` package.

This is a collection of datasets, each organized in the basic tabular data structure (rows correspond to observations, columns to variables) called a `data.frame` in `R`.


``` r
help(package = "datasets")
```

An alternative is to list the names of objects in a package. Here we use the `pattern` to just show datasets beginning with `a`.


``` r
ls("package:datasets", pattern = "^a")
```

```
## [1] "ability.cov" "airmiles"    "airquality"  "anscombe"    "attenu"      "attitude"   
## [7] "austres"
```

Often of more interest, list the names and a brief description of the structure


``` r
ls.str("package:datasets", pattern = "^a")
```

```
## ability.cov : List of 3
##  $ cov   : num [1:6, 1:6] 24.64 5.99 33.52 6.02 20.75 ...
##  $ center: num [1:6] 0 0 0 0 0 0
##  $ n.obs : num 112
## airmiles :  Time-Series [1:24] from 1937 to 1960: 412 480 683 1052 1385 ...
## airquality : 'data.frame':	153 obs. of  6 variables:
##  $ Ozone  : int  41 36 12 18 NA 28 23 19 8 NA ...
##  $ Solar.R: int  190 118 149 313 NA NA 299 99 19 194 ...
##  $ Wind   : num  7.4 8 12.6 11.5 14.3 14.9 8.6 13.8 20.1 8.6 ...
##  $ Temp   : int  67 72 74 62 56 66 65 59 61 69 ...
##  $ Month  : int  5 5 5 5 5 5 5 5 5 5 ...
##  $ Day    : int  1 2 3 4 5 6 7 8 9 10 ...
## anscombe : 'data.frame':	11 obs. of  8 variables:
##  $ x1: num  10 8 13 9 11 14 6 4 12 7 ...
##  $ x2: num  10 8 13 9 11 14 6 4 12 7 ...
##  $ x3: num  10 8 13 9 11 14 6 4 12 7 ...
##  $ x4: num  8 8 8 8 8 8 8 19 8 8 ...
##  $ y1: num  8.04 6.95 7.58 8.81 8.33 ...
##  $ y2: num  9.14 8.14 8.74 8.77 9.26 8.1 6.13 3.1 9.13 7.26 ...
##  $ y3: num  7.46 6.77 12.74 7.11 7.81 ...
##  $ y4: num  6.58 5.76 7.71 8.84 8.47 7.04 5.25 12.5 5.56 7.91 ...
## attenu : 'data.frame':	182 obs. of  5 variables:
##  $ event  : num  1 2 2 2 2 2 2 2 2 2 ...
##  $ mag    : num  7 7.4 7.4 7.4 7.4 7.4 7.4 7.4 7.4 7.4 ...
##  $ station: Factor w/ 117 levels "1008","1011",..: 24 13 15 68 39 74 22 1 8 55 ...
##  $ dist   : num  12 148 42 85 107 109 156 224 293 359 ...
##  $ accel  : num  0.359 0.014 0.196 0.135 0.062 0.054 0.014 0.018 0.01 0.004 ...
## attitude : 'data.frame':	30 obs. of  7 variables:
##  $ rating    : num  43 63 71 61 81 43 58 71 72 67 ...
##  $ complaints: num  51 64 70 63 78 55 67 75 82 61 ...
##  $ privileges: num  30 51 68 45 56 49 42 50 72 45 ...
##  $ learning  : num  39 54 69 47 66 44 56 55 67 47 ...
##  $ raises    : num  61 63 76 54 71 54 66 70 71 62 ...
##  $ critical  : num  92 73 86 84 83 49 68 66 83 80 ...
##  $ advance   : num  45 47 48 35 47 34 35 41 31 41 ...
## austres :  Time-Series [1:89] from 1971 to 1993: 13067 13130 13198 13254 13304 ...
```

When examining a new `R` package, `ls.str` is a useful way to learn about what objects are in a package. It will list both datasets and functions. However, it can still be rather verbose; it is often better to use the `Packages` tab in the bottom-right pane of Rstudio. You will find a list of objects with one-line descriptions, and help page for each object by clicking on its name. Often, packages have overview documentation toward the top.

Note that in the calls to `ls` and `ls.str` the package name is given as a character string `"package:datasets"`.  This convention is also used in describing which packages are attached in a session. 

## Namespaces and Indirect Access to Packages

Most packages have a [namespace](http://r-pkgs.had.co.nz/namespace.html), which identifies which objects are visible to users. This is a rather arkane topic, but is important to understand for those going on to develop their own packages.

Normally, one attaches a package using the `library` command, which gives direct access to all objects identified in the namespace of that package. It is possible to access objects in a package _without_ attaching the package by using the convention `packagename::objectname`. For instance, the following makes explicit reference to the package `datasets` to examine the structure of `ToothGrowth`.


``` r
str(datasets::ToothGrowth)
```

```
## 'data.frame':	60 obs. of  3 variables:
##  $ len : num  4.2 11.5 7.3 5.8 6.4 10 11.2 11.2 5.2 7 ...
##  $ supp: Factor w/ 2 levels "OJ","VC": 2 2 2 2 2 2 2 2 2 2 ...
##  $ dose: num  0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 ...
```

This is not necessary for already attached packages (such as `datasets`), but can be helpful to document the source of objects. It is generally used in packages that may use a few functions or datasets from another package. For instance, attaching the `dplyr` package makes the `magrittr` pipe (`%>%`) available, without explicitly requiring the loading of this secondary package.

## Miscellaneous Notes

motivation for creating packages

- Fritz Leisch, Kurt Hornik: [CRAN](https://cran.r-project.org/), package format
- built on [CPAN](http://www.cpan.org/), [CTAN](https://www.ctan.org/?lang=en)
- CRAN mirrors


R source package contents

- `DESCRIPTION` text file
- folders: `R`, `man`, `data`
- optional folders for added documentation: `inst`, `vignettes`
    + `inst` typically has sub-folder `doc` with `Rmd` files, etc.
- optional files: `NAMESPACE`
- `README.md`
- Rstudio project file: `myname.Rproj`
- `LICENSE`

R installed package contents

- takes source and moves to another place

##  R package references

- Karl Broman: [R Package Primer](http://kbroman.org/pkg_primer/)
    + [Package Examples](https://github.com/kbroman/pkg_primer/tree/gh-pages/example)
- Hadley Wickham: [R Packages from O’Reilly](http://r-pkgs.had.co.nz/)
- Hilary Parker: [R Package Tutorial](http://hilaryparker.com/2014/04/29/writing-an-r-package-from-scratch/)
- Writing Documentation
    + Karl Broman: [Writing documentation with Roxygen2](http://kbroman.org/pkg_primer/pages/docs.html)
    + Josh Paulson: [Writing Package Documentation](https://support.rstudio.com/hc/en-us/articles/200532317-Writing-Package-Documentation)
- CRAN: [Writing R Extensions](https://cran.r-project.org/doc/manuals/r-release/R-exts.html)
- Jenny Bryan: [Writing your own R package](http://stat545-ubc.github.io/packages00_index.html) ⚠️

-   [Writing R
    Extensions](http://cran.r-project.org/doc/manuals/R-exts.pdf)
    +   [Creating R Packages: A
        Tutorial](http://blog.revolutionanalytics.com/2009/08/creating-r-packages-a-tutorial-draft.html) ⚠️
    +   [Freidrich Leisch (2008): Creating R Packages: A
        Tutorial](http://epub.ub.uni-muenchen.de/6175/)
    +   [Brian Yandell's Demo
        Package](http://www.stat.wisc.edu/~yandell/mypackage)
        ([mydemo.R](http://www.stat.wisc.edu/~yandell/mypackage/inst/mynotes/mydemo.R)
        &
        [mypackage\_0.5-1.tar.gz](http://www.stat.wisc.edu/~yandell/mypackage_0.5-1.tar.gz)
        tarball)
-   Building R Packages for Windows
    +   [Windows R Tools Official Page (Murdoch
        Sutherland)](http://www.murdoch-sutherland.com/Rtools/) ⚠️
    +   [Karl Broman's Windows Package
        Info](http://www.biostat.wisc.edu/~kbroman/Rintro/Rwinpack.html)
    +   [Windows Toolset (R Admin
        Manual)](http://cran.r-project.org/doc/manuals/R-admin.html#The-Windows-toolset)
    +   An alternative for your own packages is to submit the package to
        the http://win-builder.R-project.org site. It will build the
        package and run the package checks then send email to whoever is
        listed in the DESCRIPTION file as the maintainer with a link to
        the results. Especially for those of us who don't use Windows
        and find the steps required under Windows to be unnecessarily it
        is wonderful. If you have the fortunes package installed you
        should check

```
            > fortune("installing")
```
