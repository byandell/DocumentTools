---
title: "Working with Data in R"
parent: "Curate R Data"
grand_parent: "R Language"
nav_order: 1
---

# Working with Data in R

## Data Structures in R

There are many good introductions to data structures in `R`.
Basically, `R` can act as a calculator, and has built in functions such as `log(10)` and `sqrt(4)`,
but can do so much more. See examples in the links below.

The basic structure in `R` is a vector, here is a vector of the numbers 1 through 5:


``` r
1:5
```

```
[1] 1 2 3 4 5
```

> ## Challenge
>
> Go through the Data Carpentry or Jenny Bryan introduction to learn more about data basics.
> Read through Doug Bates notes to fill in further gaps.

- [R Introduction from Data Carpentry](http://kbroman.org/datacarpentry_R_2017-01-10/01-intro-to-R.html)
- [R basics from Jenny Bryan](http://stat545.com/block002_hello-r-workspace-wd-project.html)
- [Data frames, examining structure from Doug Bates](https://github.com/dmbates/stat692/blob/master/Data.Rmd)

## Side story on data wrangling

Jenny Bryan expounds on data science.
GapMinder was an early innovation in data exploration.
The GapMinder data is used throughout Jenny Bryan's course,
and can now be found as the [gapminder](https://cran.r-project.org/web/packages/gapminder/) `R` package.
Hans Rosling, originator of GapMinder, has passed, but his tools and ideas persist.

- [Jenny Bryan Deep Thoughts](https://www.slideshare.net/jenniferbryan5811/cm002-deep-thoughts)
- <http://gapminder.org> | [GapMinder World](http://www.gapminder.org/world) | [GapMinderDev](https://www.gapminderdev.org/) | [Hans Rosling TED Talk](http://www.gapminder.org/videos/ted-us-state-department/)

## Data Wrangling

It is often more useful to think of `R` as mostly operating on rectangular tables, which have many of the characteristics of spreadsheets. Tables, known in `R` as data frames, have observations (individuals or cases) in rows and variables (fields) in columns. The variables might be of different types, say numeric or character or logical. We might want to operate on the whole table, or on a row or column, or on some rectangular subset of the table.

The [tidyverse](http://tidyverse.org) provides a useful set of tools to organize work around tables. See the [tidyverse style guide](http://style.tidyverse.org/) for detail. See also the data pages from various sources:

- [Introduction to the Tidyverse (nee Hadleyverse) (Doug Bates)](https://github.com/dmbates/stat692/blob/master/Hadleyverse.Rmd)
- [Aggregating and analyzing data with dplyr (Data Carpentry)](http://kbroman.org/datacarpentry_R_2017-01-10/02-dplyr.html)
- [Data analysis 1 (Jenny Bryan)](http://stat545.com/topics.html) ⚠️ (see links under this topic)

Right here would like to go through an example using `for/while/repeat`  loops, then base `apply` suite, then `dplyr` and `tidyr`, then `purrr`. The point would be that while the old way gets the job done, the newer tidyverse provides more compact ways of organizing the task that are more intuitive, once one overcomes the new way of thinking about the problem. 

Here is the basic idea. It might seem best to go a row and column at a time and do operations, but if we can think about the whole object, the entire table, and what we want to do with it, then a more elegant solution might emerge.

### base R: `for` vs. `apply`

- [apply examples](applyExample.Rmd)
- [Apply and For Loops in R by Elizabeth McDaniel](http://rpubs.com/lizilla93/258391) ([Rmd source](https://github.com/lizilla1993/ComBEE-UW-Madison/blob/master/Spring2017/R/ComBEE-R-Apply-Session.Rmd) ⚠️)

To answer the frequently asked question, 'How can I avoid this loop or make it faster?': Try to use simple vectorized operations; use the family of apply functions if appropriate; initialize objects to full length when using loops; and do not repeat calculations many times if performing them just once is sufficient. Measure execution time before making changes to code, and only make changes if the efficiency gain really matters. It is better to have readable code that is free of bugs than to waste hours optimizing code to gain a fraction of a second. Sometimes, in fact, a loop will provide a clear and efficient solution to a problem (considering both time and memory use). 
(from <https://www.r-project.org/doc/Rnews/Rnews_2008-1.pdf>, p. 49)

- [apply vs. for (Karl Broman)](https://kbroman.wordpress.com/2013/04/02/apply-vs-for/)
- [Repeating things: looping and the apply family](http://nicercode.github.io/guides/repeating-things/) ⚠️
- [why to vectorize: using apply vs for](http://www.noamross.net/blog/2014/4/16/vectorization-in-r--why.html)
- [What you’re doing is rather desperate](https://nsaunders.wordpress.com/2010/08/20/a-brief-introduction-to-apply-in-r/)
- [Guess who wins apply vs for](http://www.r-bloggers.com/guess-who-wins-apply-versus-for-loops-in-r/ )

- [Another comprehensive list of all the apply functions](http://seananderson.ca/courses/12-plyr/plyr_2012.pdf) ⚠️
- [apply for Dummies](http://www.dummies.com/how-to/content/how-to-use-the-apply-family-of-functions-in-r.html) ⚠️ (towards the bottom)

- [Parallel apply (mclapply)](http://www.rforge.net/doc/packages/multicore/mclapply.html) ⚠️

### plyr

There is a package called [plyr](https://github.com/hadley/plyr), which seems to be retained for historical reasons and compatibility with other packages. Best to skip this package and go right to `dplyr`. These two packages have different syntax and approach problems somewhat differently.

- [split-apply-combine strategy paper by Hadley Wickham](http://vita.had.co.nz/papers/plyr.html)

### dplyr

The `dplyr` package allows us to filter by rows and select columns, and to do tasks in groups organized by levels of columns. Further, these steps can be strung together using `pipes` as a coherent operation on a table, to create a new table. This new table may be stored, or might be used in another operation without ever being saved as a new object. See notes linked above, and the following.

- [Intro to R Adapted to dplyr](R_intro_dplyr.html)
- [Data Wrangling in R by Elizabeth McDaniel](http://rpubs.com/lizilla93/data-wrangling-dplyr) ([Rmd source](https://github.com/lizilla1993/ComBEE-UW-Madison/blob/master/Spring2017/R/Data-Wrangling.Rmd) ⚠️)
- [dplyr on tidyverse](http://dplyr.tidyverse.org/)
- [Data Transformation with dplyr](https://www.rstudio.com/resources/cheatsheets/) (scroll down)

The latest release of `dplyr` (0.7.0) in its basic form appears unchanged. However, there is a new philosophy of "tidy evaluation" that will have a profound effect on how we use `dplyr` tools within functional programming. That is, the straightforward way to use `dplyr` is to reference table columns by name, which works great in an interactive setting. If the column names might change from table to table, and you want to create tools that leverage that, it will be important to learn about tidy evaluation.

- [dplyr 0.7.0 release announcement](https://blog.rstudio.org/2017/06/13/dplyr-0-7-0/)
- [tidy evaluation](http://rlang.tidyverse.org/articles/tidy-evaluation.html) ⚠️
- [RStudio Webinars](https://www.rstudio.com/resources/webinars/) (see What's new in dplyr 0.7.0?)

### tidyr

The package [tidyr](http://tidyr.tidyverse.org/) is a companion to `dplyr`, with tools to rearrange tables. It is not covered in Data Carpentry.

- [tidyr] | [blog intro](https://blog.rstudio.org/2014/07/22/introducing-tidyr/)
- [tidyr tutorial by JV 
Casillas](http://www.jvcasillas.com/tidyr_tutorial/)
- [tidyr tutorial by U VA Library](http://data.library.virginia.edu/a-tidyr-tutorial/)
- [Data Wrangling Rpubs by Bradley Boehmke](https://rpubs.com/bradleyboehmke/data_wrangling)
- [Tidy data article by Hadley Wickham](https://www.jstatsoft.org/article/view/v059i10)
- [Data Import CheatSheet](https://www.rstudio.com/resources/cheatsheets/) (scroll down; )

Note: There used to be one Data Wrangling CheatSheet for `dplyr` and `tidyr`. It has been replaced by the Data Transformation and Data Input CheatSheets.

Some use the older [reshape2](https://github.com/hadley/reshape), which includes some column aggregations features that are not easily done in `tidyr`. See for instance:

- [How to reshape data in R: tidyr vs reshape2](https://www.r-bloggers.com/how-to-reshape-data-in-r-tidyr-vs-reshape2/).
- [An Introduction to reshape2](http://seananderson.ca/2013/10/19/reshape.html) ⚠️

### purrr

- [purrr example using `map` & `transpose`](purrr.html)
- [more tidyverse on `portal_mammals` data](species.html)
- [purrr Tutorial by Jenny Bryan](https://jennybc.github.io/purrr-tutorial/) | [github](https://github.com/jennybc/purrr-tutorial) | [repurrsive](https://github.com/jennybc/repurrrsive)
- [purrr](http://purrr.tidyverse.org/) | [blog entry](https://blog.rstudio.org/2016/01/06/purrr-0-2-0/) | [bloggers entry](https://www.r-bloggers.com/using-purrr-with-dplyr/)
- [Iteration chapter of R for Data Science](http://r4ds.had.co.nz/iteration.html)
- [Solving iteration problems using functional programming](https://www.rstudio.com/resources/videos/happy-r-users-purrr-tutorial/)

## Prettying up tables

- matrix vs data frame vs [tibble](http://tibble.tidyverse.org/)
- [knitr figures and tables (Karl Broman)](http://kbroman.org/knitr_knutshell/pages/figs_tables.html) (kable, pander, xtable)
- [printr](https://yihui.name/printr/) package

## Everything in R is a vector

If you are new to programming, this subsection might be skipped. Experienced programmers who are new to `R` might find this useful. The basic argument: everything in R is a vector (no scalars!). See also

- [Data analysis 2: vectors and files](http://stat545.com/topics.html) ⚠️ (scroll down to this topic)


Atomic vectors include integers, double-precision, strings (character), logical and a few others. 


``` r
(v <- 1:6)
```

```
[1] 1 2 3 4 5 6
```

A list is a vector of objects that don’t have to share relationships (but can).
Here we do something silly, turning a vector of six numbers into a list, which is a vector of six objects, each of which is a vector with one number.



``` r
(as.list(v <- 1:6))
```

```
[[1]]
[1] 1

[[2]]
[1] 2

[[3]]
[1] 3

[[4]]
[1] 4

[[5]]
[1] 5

[[6]]
[1] 6
```

### Attributes

Attributes can be attached to objects


``` r
v <- 1:6
attributes(v) <- list(message = "hello world")
v
```

```
[1] 1 2 3 4 5 6
attr(,"message")
[1] "hello world"
```

Attributes can turn a vector into a matrix


``` r
v <- 1:6
attributes(v) <- list(dim= c(3,2))
v
```

```
     [,1] [,2]
[1,]    1    4
[2,]    2    5
[3,]    3    6
```

This is equivalent to


``` r
(x <- matrix(1:6, ncol=2))
```

```
     [,1] [,2]
[1,]    1    4
[2,]    2    5
[3,]    3    6
```

Note that while `v` (and `x`) is a matrix, it is still a vector of six numbers:


``` r
attributes(v)
```

```
$dim
[1] 3 2
```


``` r
length(v)
```

```
[1] 6
```


``` r
v[4]
```

```
[1] 4
```

A matrix can be turned into a data frame:


``` r
(x <- as.data.frame(x))
```

```
  V1 V2
1  1  4
2  2  5
3  3  6
```

Now `x` as a data frame is a vector (actually a list) of length 2, with each element of the list being a vector of numbers:


``` r
x[[2]]
```

```
[1] 4 5 6
```

### Subsetting and Accessing

Subset using positive integers:


``` r
v[c(3,4,6,6)]
```

```
[1] 3 4 6 6
```


``` r
v[1:3]
```

```
[1] 1 2 3
```

Subset using logical


``` r
v[c(FALSE, FALSE, TRUE)]
```

```
[1] 3 6
```

This takes some explaining, the vector `c(FALSE, FALSE, TRUE)` is cycled through the indices of `v` (here `1:6`). Try this one:


``` r
v[c(TRUE, TRUE, FALSE, FALSE)]
```

```
[1] 1 2 5 6
```

Logical with normal dist example:


``` r
(r <- rnorm(6, 0, 1))
```

```
[1] -0.9484028 -1.4914093 -0.8712361  0.3532766 -0.7783914 -1.7886133
```

``` r
v[r>0]
```

```
[1] 4
```


``` r
(r <- rnorm(15, 0, 1))
```

```
 [1] -1.15859082  1.38298980  1.65264961 -0.23520223 -0.55574794 -0.82232772
 [7] -2.52986697  0.23639498  0.09033381 -1.45070642 -1.34537308  0.32079647
[13] -0.03517850 -0.27326153  0.35862242
```

``` r
v[r>0]
```

```
[1]  2  3 NA NA NA NA
```

Notice that in this case some of the indices are beyond the data and return missing values.

Use negative numbers to exclude some indices. You cannot mix positive and negative numbers.


``` r
v[-(1:3)]
```

```
[1] 4 5 6
```

Zero (0) is skipped. Works with positive or negative numbers. This is useful for instance with the `match()` function if you set `nomatch = 0`.


``` r
v[c(0,2,4)]
```

```
[1] 2 4
```



``` r
v[c(0,-2,-4)]
```

```
[1] 1 3 5 6
```


``` r
v[0]
```

```
integer(0)
```

Note that if all indices to a vector are 0, then a vector of length 0 is returned. This also happens with `NULL`:


``` r
v[NULL]
```

```
integer(0)
```



``` r
(r <- sample(letters, 15))
```

```
 [1] "f" "k" "h" "j" "r" "d" "u" "v" "b" "e" "g" "w" "x" "c" "o"
```

``` r
(m <- match(c("a","c","e"), r, nomatch = 0))
```

```
[1]  0 14 10
```

``` r
v[m]
```

```
[1] NA NA
```

Elements of a vector can be identified by name


``` r
v <- c(v)
names(v) <- letters[seq_along(v)]
v
```

```
a b c d e f 
1 2 3 4 5 6 
```


``` r
v["c"]
```

```
c 
3 
```

For lists, you can use `[[]]` or `$`. Double brackets (special for lists) pull out components; `$` is a shorthand that works for proper names.


``` r
l <- as.list(v)
(l[["c"]])
```

```
[1] 3
```

``` r
(l$c)
```

```
[1] 3
```

We saw recycling of logical indices above. Here is another form of recycling:



``` r
v + c(1,2)
```

```
a b c d e f 
2 4 4 6 6 8 
```

will return 2, 4, 4, 6, 6, etc.

#### Logical

While `T` and `F` work for `TRUE` and `FALSE`, don't use them. Always spell out the full word. Avoid bizarre circumstances. And avoid using these as names of objects.

Logical expressions can use the shorter or longer form of AND (`&` vs `&&`) or OR (`|` vs `||`). See the `help(&)` page or [R bloggers](https://www.r-bloggers.com/logical-operators-in-r/) for full details.
The shorter form performs elementwise comparisons in much the same way as arithmetic operators. The longer form evaluates left to right examining only the first element of each vector. Evaluation proceeds only until the result is determined. The longer form is appropriate for programming control-flow and typically preferred in if clauses.

