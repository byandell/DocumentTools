---
title: "Tidyverse Split-Apply-Combine Example"
parent: "Curate R Data"
grand_parent: "R Language"
nav_order: 4
---

# Tidyverse Split-Apply-Combine Example

``` r
surveys <- read.csv("http://kbroman.org/datacarp/portal_data_joined.csv",
                    stringsAsFactors = FALSE)
```

### Split-apply-combine using dplyr


``` r
library(dplyr)    ## load the package
```


``` r
surveys %>%
  filter(taxa == "Rodent",
         !is.na(weight)) %>%
  group_by(sex,genus) %>%
  summarize(mean_weight = mean(weight))
```

```
## # A tibble: 28 × 3
## # Groups:   sex [3]
##    sex   genus           mean_weight
##    <chr> <chr>                 <dbl>
##  1 ""    Chaetodipus           19.8 
##  2 ""    Dipodomys             81.4 
##  3 ""    Neotoma              168.  
##  4 ""    Onychomys             23.4 
##  5 ""    Perognathus            6   
##  6 ""    Peromyscus            19.9 
##  7 ""    Reithrodontomys       11.1 
##  8 ""    Sigmodon              70.3 
##  9 "F"   Baiomys                9.16
## 10 "F"   Chaetodipus           23.8 
## # ℹ 18 more rows
```

### Split-apply-combine using dplyr and tidyr


``` r
library(tidyr)
```

Here we use `spread()` from the `tidyr` package. This gives a more compact, if wider,
table summary.


``` r
surveys %>%
  filter(taxa == "Rodent",
         !is.na(weight)) %>%
  group_by(sex,genus) %>%
  summarize(mean_weight = mean(weight)) %>%
  spread(sex, mean_weight)
```

```
## # A tibble: 10 × 4
##    genus              V1      F      M
##    <chr>           <dbl>  <dbl>  <dbl>
##  1 Baiomys          NA     9.16   7.36
##  2 Chaetodipus      19.8  23.8   24.7 
##  3 Dipodomys        81.4  55.2   56.2 
##  4 Neotoma         168.  154.   166.  
##  5 Onychomys        23.4  26.8   26.2 
##  6 Perognathus       6     8.57   8.20
##  7 Peromyscus       19.9  22.5   20.6 
##  8 Reithrodontomys  11.1  11.2   10.2 
##  9 Sigmodon         70.3  71.7   61.3 
## 10 Spermophilus     NA    57    130
```

Here is a simpler tidy example to just count how many records with weigth by genus and sex.


``` r
surveys %>%
  filter(taxa == "Rodent",
         !is.na(weight)) %>%
  count(sex, genus) %>%
  spread(sex, n)
```

```
##              genus V1    F    M
## 1          Baiomys NA   31   14
## 2      Chaetodipus 16 3201 2627
## 3        Dipodomys 35 6826 8649
## 4          Neotoma 16  652  484
## 5        Onychomys  7 1502 1627
## 6      Perognathus  4  762  813
## 7       Peromyscus  8  958 1206
## 8  Reithrodontomys 12 1245 1363
## 9         Sigmodon  3  125   95
## 10    Spermophilus NA    1    1
```

### Split-apply-combine using split, purrr and tidyr

The `purrr` package works on lists (which includes data frames), giving great generality to what objects might be in the lists. Below we show two examples.


``` r
library(purrr)
```

In the first example, for each genus, we fit a linear model with `lm()` and extract the `"r.squared"` element from the `summary()` of the fit. Note the use of `split()` to split the data frame into a list of data frames, one per genus. The `map()` function from `purrr` returns a list, while the `map_dbl()` function returns a vector.


``` r
surveys %>%
  filter(taxa == "Rodent",
         !is.na(weight)) %>%
  select(genus,weight,sex) %>%
  split(.$genus) %>%
  map(~ lm(weight ~ sex, data=.)) %>%
  map(summary) %>%
  map_dbl("r.squared")
```

```
##         Baiomys     Chaetodipus       Dipodomys         Neotoma       Onychomys 
##     0.164529171     0.003305788     0.001992282     0.016659203     0.002306456 
##     Perognathus      Peromyscus Reithrodontomys        Sigmodon    Spermophilus 
##     0.003560761     0.042744223     0.054463691     0.038990704     1.000000000
```

Note that for `Spermophilus`, the $R^2$ of 1 reflects that there are only two records, one male and one female (see table above in `tidyr` section).

There were three calls to `purrr` functions. The first `map(~ lm())` call creates a list of `"lm"` objects; the second `map(summary)` call creates a list of `"summary.lm"` objects; the third `map_dbl()` creates a vector of double-precision values.

The following more complicated example takes the `coef()` of the `lm()` fits to get the estimates of coefficients. These coefficients have to be converted into a data frame,
and then the data frames are bound together using `bind_rows()`.


``` r
surveys %>%
  filter(taxa == "Rodent",
         !is.na(weight)) %>%
  select(genus,weight,sex) %>%
  split(list(.$genus)) %>%
  map(~ lm(weight ~ sex, data=.)) %>%
  map(coef) %>%
  map(function(x) data.frame(level = names(x), estimate = x,
                             stringsAsFactors = FALSE)) %>%
  bind_rows(.id = "genus")
```

```
##                            genus       level    estimate
## (Intercept)...1          Baiomys (Intercept)   9.1612903
## sexM...2                 Baiomys        sexM  -1.8041475
## (Intercept)...3      Chaetodipus (Intercept)  19.8125000
## sexF...4             Chaetodipus        sexF   3.9513238
## sexM...5             Chaetodipus        sexM   4.8997193
## (Intercept)...6        Dipodomys (Intercept)  81.3714286
## sexF...7               Dipodomys        sexF -26.1270688
## sexM...8               Dipodomys        sexM -25.1283947
## (Intercept)...9          Neotoma (Intercept) 167.6875000
## sexF...10                Neotoma        sexF -13.4052914
## sexM...11                Neotoma        sexM  -2.0346074
## (Intercept)...12       Onychomys (Intercept)  23.4285714
## sexF...13              Onychomys        sexF   3.3523873
## sexM...14              Onychomys        sexM   2.8178945
## (Intercept)...15     Perognathus (Intercept)   6.0000000
## sexF...16            Perognathus        sexF   2.5748031
## sexM...17            Perognathus        sexM   2.2041820
## (Intercept)...18      Peromyscus (Intercept)  19.8750000
## sexF...19             Peromyscus        sexF   2.6166493
## sexM...20             Peromyscus        sexM   0.7692786
## (Intercept)...21 Reithrodontomys (Intercept)  11.0833333
## sexF...22        Reithrodontomys        sexF   0.1367470
## sexM...23        Reithrodontomys        sexM  -0.9233920
## (Intercept)...24        Sigmodon (Intercept)  70.3333333
## sexF...25               Sigmodon        sexF   1.3626667
## sexM...26               Sigmodon        sexM  -8.9964912
## (Intercept)...27    Spermophilus (Intercept)  57.0000000
## sexM...28           Spermophilus        sexM  73.0000000
```

The following is the same idea as above, but using `summary()` rather than `coef()`. We also `spread()` the data for a more compact table.


``` r
surveys %>%
  filter(taxa == "Rodent",
         !is.na(weight)) %>%
  select(genus,weight,sex) %>%
  split(list(.$genus)) %>%
  map(~ lm(weight ~ sex, data=.)) %>%
  map(summary) %>%
  map(function(x) {
    out <- as.data.frame(x$coefficients[,1, drop = FALSE])
    out$level <- row.names(out)
    out[, 2:1]
    }) %>%
  bind_rows(.id = "genus") %>%
  spread(level, Estimate)
```

```
##              genus (Intercept)       sexF        sexM
## 1          Baiomys     9.16129         NA  -1.8041475
## 2      Chaetodipus    19.81250   3.951324   4.8997193
## 3        Dipodomys    81.37143 -26.127069 -25.1283947
## 4          Neotoma   167.68750 -13.405291  -2.0346074
## 5        Onychomys    23.42857   3.352387   2.8178945
## 6      Perognathus     6.00000   2.574803   2.2041820
## 7       Peromyscus    19.87500   2.616649   0.7692786
## 8  Reithrodontomys    11.08333   0.136747  -0.9233920
## 9         Sigmodon    70.33333   1.362667  -8.9964912
## 10    Spermophilus    57.00000         NA  73.0000000
```

