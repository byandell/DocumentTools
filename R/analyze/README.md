---
title: "Analyze Data"
parent: "R Language"
author: "Brian S. Yandell"
date: 2017-06-29
permalink: /R/analyze/
nav_order: 5
has_children: true
---

# Analyze Data

- [Analyze data with linear and other models](#analyze-data-with-linear-and-other-models)
- [Systems Genetics](sysgen.md)

## Analyze data with linear and other models

This material is in a very early stage. It is not clear how complete this will be,
as the focus of this material is to provide advanced access to R as an interactive
environment, rather than focus on statistical methods. See some of the
[references](../learn/reference.md) for links to more complete material.

**Learning Objectives:** After completing this material, an individual will be able to
do first steps to analyze data in `R`.

- correlate measurements and compare across groups using linear models
- develop annotated plots that reflect project design
- organize linear model results with [broom](https://github.com/tidyverse/broom), [car](https://cran.r-project.org/web/packages/car/index.html), or [lsmeans](https://github.com/rvlenth/lsmeans) packages
- clustering and trees, building networks
- models that are not linear: generalized linear models, non-linear models
- [formulas](Formulas.md)

file | contents
---- | --------
[correlate](correlate.md) | co-relate variables (columns) of data
[covary](covary.md) | how do columns co-vary together
[linear_model](linear_model.md) | linear models
[Formulas](Formulas.md) | formulas for linear models

### Douglas Bates Reference Notes

- [Formulas.Rmd](https://github.com/dmbates/stat692/blob/master/Formulas.Rmd)
- [formulas.Rnw](https://github.com/dmbates/stat692/blob/master/formulas.Rnw) and [formulas.pdf](https://github.com/dmbates/stat692/blob/master/formulas.pdf)

---

## Systems Genetics in R

Systems genetics explores Quantitative Trait Loci (QTL), mediation, and multi-omic data integration. Key repositories and research tools include:

- **R Packages & Organizations**:
  - [byandell-sysgen GitHub Organization](https://github.com/byandell-sysgen)
  - [R/qtl](http://rqtl.org): High-density genetic mapping
  - [R/qtl2](http://kbroman.org/qtl2/): Genetic analysis in multi-parent populations
- **Collaborative Research Centers**:
  - [Systems Genetics Resource (UCLA)](https://systems.genetics.ucla.edu/)
  - [Churchill Lab at The Jackson Laboratory](http://churchill-lab.jax.org/)
  - [Collaborative Cross (UNC)](http://www.csbio.unc.edu/CCstatus/)
  - [Yandell Notes from Jackson Labs Talks](http://pages.stat.wisc.edu/~yandell/talk/jax/)

