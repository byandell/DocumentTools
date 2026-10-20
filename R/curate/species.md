---
title: "Species Analysis with dplyr and purrr"
parent: "Curate R Data"
grand_parent: "R Language"
nav_order: 6
---

# Species Analysis with dplyr and purrr

We are going to use the species data from data carpentry to explore with the `dplyr`,
`tidyr` and `purrr` packages. The data are available at <http://kbroman.org/datacarp/portal_data_joined.csv>. Here we attach the packages we will use with the `library` command.


``` r
library(dplyr)
library(tidyr)
library(purrr)
library(readr)
```



``` r
surveys <- read_csv("../data/surveys.csv")
```

```
## Error:
## ! '../data/surveys.csv' does not exist in current working directory:
##   '/Users/brianyandell/Documents/GitHub/Documentation/R/curate'.
```


``` r
surveys %>%
  filter(!(is.na(hindfoot_length) & is.na(weight)),
         !is.na(sex)) %>%
  group_by(species_id, sex) %>%
  summarize(hflen = mean(hindfoot_length, na.rm = TRUE),
            wt = mean(weight, na.rm = TRUE))
```

```
## Error:
## ! object 'surveys' not found
```

Here is a spread table for one of the traits.


``` r
surveys %>%
  filter(!(is.na(hindfoot_length) & is.na(weight)),
         !is.na(sex)) %>%
  group_by(species_id, sex) %>%
  summarize(hflen = mean(hindfoot_length, na.rm = TRUE)) %>%
  spread(sex, hflen)
```

```
## Error:
## ! object 'surveys' not found
```

How would you do this for two traits? Turns out this is more challenging, and depends on what you want to compare. The simplest thing is to `arrange` or `subset` the earlier table by `sex`. If you want four columns on one line, for `sex` and the two traits, you will have to be creative. What you want to do is avoid typing the trait names or the sexes if you can. I don't have an easy solution!

The following gives us a list of 2-trait tables by sex. Notice the use of `map` from package `purrr` to act separately on each `sex`.


``` r
tmp <- surveys %>%
  filter(!(is.na(hindfoot_length) & is.na(weight)),
         !is.na(sex))
```

```
## Error:
## ! object 'surveys' not found
```

``` r
tmp <- split(tmp, tmp$sex)
```

```
## Error:
## ! object 'tmp' not found
```

``` r
tmp2 <- map(tmp, function(x) {
  x %>% 
    group_by(species_id, sex) %>%
    summarize(hflen = mean(hindfoot_length, na.rm = TRUE),
            wt = mean(weight, na.rm = TRUE))
})
```

```
## Error:
## ! object 'tmp' not found
```

``` r
tmp2
```

```
## Error:
## ! object 'tmp2' not found
```

What about this? It gives small tables by species. The challenge is that species that do not have records for both sexes will mess up any easy combining.


``` r
tmp <- surveys %>%
  filter(!(is.na(hindfoot_length) & is.na(weight)),
         !is.na(sex))
```

```
## Error:
## ! object 'surveys' not found
```

``` r
tmp <- split(tmp, tmp$species_id)
```

```
## Error:
## ! object 'tmp' not found
```

``` r
tmp2 <- map(tmp, function(x) {
  x %>% 
    select(-species_id) %>%
    group_by(sex) %>%
    summarize(hflen = mean(hindfoot_length, na.rm = TRUE),
            wt = mean(weight, na.rm = TRUE))
})
```

```
## Error:
## ! object 'tmp' not found
```

``` r
tmp2
```

```
## Error:
## ! object 'tmp2' not found
```


## Bringing in species information

Suppose you want to bring in taxonomic information from another file. While you can use `left_join(surveys, species)` to create a larger table, what can we do keeping the two tables separate? This can be useful if both tables are large, or if they are configured in different ways. Here 


``` r
species <- read_csv("../data/species.csv")
```

```
## Error:
## ! '../data/species.csv' does not exist in current working directory:
##   '/Users/brianyandell/Documents/GitHub/Documentation/R/curate'.
```

Here we want summaries by `genus`. Notice the use of `map_df` from `purrr` to get results as a data frame.


``` r
species_taxa <- split(species, species$genus)
```

```
## Error:
## ! object 'species' not found
```


``` r
map_df(species_taxa,
       function(x, surveys) {
         # Identify species in this taxa
         taxa_sp <- x$species_id
         surveys %>%
           filter(!(is.na(hindfoot_length) & is.na(weight)),
                  !is.na(sex),
           species_id %in% taxa_sp) %>%
           group_by(sex) %>%
           summarize(hflen = mean(hindfoot_length, na.rm = TRUE),
                     wt = mean(weight, na.rm = TRUE))
         },
       surveys,
       .id = "genus")
```

```
## Error:
## ! object 'species_taxa' not found
```

