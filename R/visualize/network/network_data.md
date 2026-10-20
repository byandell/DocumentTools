---
title: "Network Data Preparation"
parent: "Network Observatins in Connected Graphs"
grand_parent: "Visualize Data with R"
nav_order: 1
---

# Network Data Preparation

Examples pulled from **Network Visualization with R**, [Polnet 2016](http://www.kateto.net/polnet2016) by Katya Ognyanova.

## Pull in Polnet2016 data

The following step will download the data files and Katya's tutorial.


``` r
if(!file.exists("polnet2016.zip")) {
  download.file("http://kateto.net/wp-content/uploads/2016/06/polnet2016.zip",
              "polnet2016.zip")
}
if(!dir.exists("Data files")) {
  unzip("polnet2016.zip")
}
```


``` r
data_dir <- "Data files"
```



``` r
suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
})
```

#### Dataset 1: edgelist


``` r
(nodes <- 
   read_csv(file.path(data_dir,
                      "Dataset1-Media-Example-NODES.csv")))
```

```
## # A tibble: 17 × 5
##    id    media               media.type type.label audience.size
##    <chr> <chr>                    <dbl> <chr>              <dbl>
##  1 s01   NY Times                     1 Newspaper             20
##  2 s02   Washington Post              1 Newspaper             25
##  3 s03   Wall Street Journal          1 Newspaper             30
##  4 s04   USA Today                    1 Newspaper             32
##  5 s05   LA Times                     1 Newspaper             20
##  6 s06   New York Post                1 Newspaper             50
##  7 s07   CNN                          2 TV                    56
##  8 s08   MSNBC                        2 TV                    34
##  9 s09   FOX News                     2 TV                    60
## 10 s10   ABC                          2 TV                    23
## 11 s11   BBC                          2 TV                    34
## 12 s12   Yahoo News                   3 Online                33
## 13 s13   Google News                  3 Online                23
## 14 s14   Reuters.com                  3 Online                12
## 15 s15   NYTimes.com                  3 Online                24
## 16 s16   WashingtonPost.com           3 Online                28
## 17 s17   AOL.com                      3 Online                33
```


``` r
(links <- 
   read_csv(file.path(data_dir, 
                      "Dataset1-Media-Example-EDGES.csv")) %>%
   group_by(from,to,type) %>%
   summarize(weight = sum(weight)) %>%
   ungroup %>%
   arrange(from,to))
```

```
## # A tibble: 49 × 4
##    from  to    type      weight
##    <chr> <chr> <chr>      <dbl>
##  1 s01   s02   hyperlink     22
##  2 s01   s03   hyperlink     22
##  3 s01   s04   hyperlink     21
##  4 s01   s15   mention       20
##  5 s02   s01   hyperlink     23
##  6 s02   s03   hyperlink     21
##  7 s02   s09   hyperlink      1
##  8 s02   s10   hyperlink      5
##  9 s03   s01   hyperlink     21
## 10 s03   s04   hyperlink     22
## # ℹ 39 more rows
```

#### Dataset 2: matrix


``` r
(nodes2 <- read_csv(file.path(data_dir, 
                              "Dataset2-Media-User-Example-NODES.csv")))
```

```
## # A tibble: 30 × 5
##    id    media   media.type media.name audience.size
##    <chr> <chr>        <dbl> <chr>              <dbl>
##  1 s01   NYT              1 Newspaper             20
##  2 s02   WaPo             1 Newspaper             25
##  3 s03   WSJ              1 Newspaper             30
##  4 s04   USAT             1 Newspaper             32
##  5 s05   LATimes          1 Newspaper             20
##  6 s06   CNN              2 TV                    56
##  7 s07   MSNBC            2 TV                    34
##  8 s08   FOX              2 TV                    60
##  9 s09   ABC              2 TV                    23
## 10 s10   BBC              2 TV                    34
## # ℹ 20 more rows
```


``` r
## First row is names, so need to use read.csv.
(links2 <- read.csv(file.path(data_dir, 
                              "Dataset2-Media-User-Example-EDGES.csv"),
                    header = TRUE, 
                    row.names = 1))
```

```
##     U01 U02 U03 U04 U05 U06 U07 U08 U09 U10 U11 U12 U13 U14 U15 U16 U17 U18 U19 U20
## s01   1   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
## s02   0   0   0   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1
## s03   0   0   0   0   0   1   1   1   1   0   0   0   0   0   0   0   0   0   0   0
## s04   0   0   0   0   0   0   0   0   1   1   1   0   0   0   0   0   0   0   0   0
## s05   0   0   0   0   0   0   0   0   0   0   1   1   1   0   0   0   0   0   0   0
## s06   0   0   0   0   0   0   0   0   0   0   0   0   1   1   0   0   1   0   0   0
## s07   0   0   0   0   0   0   0   0   0   0   0   0   0   1   1   1   0   0   0   0
## s08   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   1   1   1   0
## s09   0   0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   1   1
## s10   1   0   0   0   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0   0
```

