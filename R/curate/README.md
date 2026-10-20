---
title: "Curate R Data"
parent: "R Language"
author: "Brian S. Yandell"
date: 2017-06-29
nav_order: 2
has_children: true
permalink: /R/curate/
---

# Curate R Data

This and other lessons assume users already have some experience with R, for instance through a [Data Carpentry](http://kbroman.org/datacarpentry_R_2017-01-10/) workshop. See [References](reference.md) for useful introductory and advanced material.

> ## Learning Objectives
>
> After completing this section, an individual will be able to curate data in `R`.
>
> * read, manipulate and display data summaries in concise tables
> * work with data frames using [tidyverse](http://tidyverse.org/) tools
> * use character string operations to clean data
> * create functions to collapse repeated steps into one-line "verbs"
> * save cleaned up data tables in external files

------------

## Read, Manipulate and Display Data

* [Working with data tables in R](data_tables.md)
* [Examples using `for` and `apply`](applyExample.md)

## Work with Data Frames using Tidyverse tools

* [sub_lesson recasting data.frame examples](intro_dplyr.md)
* [Tidyverse split-apply-combine example](tidyverse.md)
* [purrr example using `map` & `transpose`](purrr.md)
* [more tidyverse on `portal_mammals` data](species.md)

## Character String Operations to Clean Data

* [characters and strings](string.md)
* [regular expressions (regex)](regex.md)

## Create Functions to Collapse Steps

* [examples of functions](../organize/function.md)

## Save Cleaned up Data to External Files

* [read and write files](file.md)

---

## Condensed Format

**Learning Objectives:** After completing this material, an individual will be able to
curate data in `R`.

* read, manipulate and display data summaries in concise tables
* work with data frames using [tidyverse](http://tidyverse.org/) tools
* write cleaned up data table out in CSV format

file | contents
---- | --------
[data_tables](data_tables.md) | Working with data tables in R
[applyExample](applyExample.md) | Examples using `for` and `apply`
[intro_dplyr](intro_dplyr.md) | sub_lesson recasting data.frame examples
[tidyverse](tidyverse.md) | Tidyverse split-apply-combine example
[purrr](purrr.md) | another example using `map` & `transpose`
[species](species.md) | `dplyr`, `tidyr` and `purrr` ideas with `portal_mammals` data
[string](string.md) | characters and strings
[regex](regex.md) | regular expressions
[file](file.md) | read and write files
