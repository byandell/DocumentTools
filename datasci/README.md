---
title: "Data Sciences"
parent: "Document Tools"
has_children: true
nav_order: 8
permalink: /datasci/
---

# Data Sciences

([slides](../quarto/datasci.html))

We often speak about data science, but recognize that our approaches to data
vary widely depending on context, discipline, background, goals, and available tools.
This page catalogues some of my interests and resources that I have found useful.
My background is pure math to stats to data science, learning how to code informally,
along the way.
Early on--decades ago, even while an undergraduate--I realized I enjoyed combining
math, biology and computers, and that I liked talking with people about their projects.
What began as consulting evolved into collaboration,
initially with colleagues in ecology, then agriculture, then animal models for human
health.
Lately, I have been interested in how communities learn to use data to understand
their environment and health to make decision.
All of these varied domains and interests have needs for data sciences insights.
This page is an effort to pull together some practical tools in the context
of my broader project to
[Document Tools](/).

Examining relationships in complex systems presents many challenges.
Many things are correlated, but not necessarily causally related.
Measures over time and space are typically (auto)correlated,
or correlated with each other.
Sytems studies involve examining many different types of measurements,
which raise issues of scaling, admixture or groupings,
and even the conundrum that we don't know what is useful to measure,
or whether what has been measured properly reflects underlying
processes.
Some of these ideas are examined (albeit incompletely) in
[Making Sense of Data](#making-sense-of-data)
and
[Significance and Importance](./signif.md).

There is a tension between data sovereignty, the inherent rights of peoples
to control access and use of their own data, and the open data movement.
Many communities are exploring ways to use open, notably public, data
to navigate local issues as well as more global challenges that impinge on their communities.
I feel honored to be engaged in some of these conversations.

- [What is Data Science?](#what-is-data-science)
- [Making Sense of Data](#making-sense-of-data)
- [Data Sovereignty](#data-sovereignty)
- [Open Data & Open Science](#open-data--open-science)
- Additional Pages
  - [Significance and Importance](signif.md)
    - [Scatter Plots to Relate Measurements](signif.md#scatter-plots-to-relate-measurements)
  - [Data Repositories](repositories.md)
  - [Big Data](bigdata.md)

## What is Data Science?

- [What is Data Science?](https://byandell.github.io/What-is-Data-Science/)
- [Data Evolve](https://byandell.github.io/Data-Evolve)
- [Data Science Collaboratory](https://byandell.github.io/Data-Sciences-Collaboratory/)
- [Data Science Across the Liberal Arts](https://byandell.github.io/Data-Science-across-the-Liberal-Arts/)
- [Strategic Planning: Data, Models and Statistics](https://byandell.github.io/Data-Models-and-Statistics/)
- [Data Science Quotes](https://byandell.github.io/Useful-Data-Science-Quotes/)

## Making Sense of Data

My background is statistics, where data visualization and rigorous thinking
about key questions and design are paramount.
Other pages in this body address the mechanics of data visualization.

Scatter plots are useful for investigating the relationship
among measurements.
A simple scatter plot is an XY-plot of two measurements, ideally augmented with color and trend lines and maybe even facets
to emphasize additional measurements.
Data scientists do this all the time in `R` with the
[ggplot2](https://ggplot2.tidyverse.org/) package,
which has a Python version as
[plotnine](https://plotnine.readthedocs.io/).

Here is a small repo with code for scatter plots in `R` and `Python` (hence the name `scattyr`).
It shows how to use color, symbol shape and facets to help reveal patterns in data.

- <https://byandell.github.io/scattyr/> (published report)
- <https://github.com/byandell/scattyr> (GitHub repo)

A question came up of how to relate rain and drought (or any other measures over time and space).
I figured out how to create the plot I suggested from cumulative rain and drought.
I used an example of two counties in SD, which are homes to Oglala Lakota (Pine Ridge in Oglala Lakota County)
and Sicangu (Rosebud in Todd County).
The published report
[SD Rain & Drought Analysis](https://byandell.github.io/rainDrought/)
uses `plotnine` in python.

I think it is much better to show data explicitly (and do it early in a report) rather than talk about the concept.
I also do not think correlation works well when considering processes over time and space,
where there is substantial auto-correlation built in and variability due to the scale of measures.
Cumulative measures are much better behaved for a variety of reasons.

- Books
  - [R for Data Science by Garrett Grolemund, Mine Çetinkaya-Rundel and Hadley Wickham (2nd Edition)](https://r4ds.hadley.nz/)
  - [Practical Data Analysis for Designed Experiments by Brian S. Yandell (1997)](https://www.stat.wisc.edu/~yandell/pda/)
  - [Visualizing Data by William S. Cleveland (1993)](https://archive.org/details/visualizingdata00will/)
- [Document Tools](/)
  - [Curate R Data](/R/curate/)
  - [Visualize Data with R](/R/visualize/)
  - [Analyze Data with R](/R/analyze/)

## Data Sovereignty

- [Data Sovereignty](https://byandell.github.io/Data-Sovereignty/)
- [Indigenous Data Science & Data Sovereignty](https://byandell.github.io/pages/indigenous/)
- [US Indigenous Data Network (USIDN)](https://usindigenousdatanetwork.org/)
- [Indigenous Data Alliance](https://indigenousdata.org/)
- [CARE Data Maturity Model (Indigenous DataLab)](https://indigenousdatalab.org/care-data-maturity-model/)
- [Tiered Sovereign Data Framework (Patrick Freeland)](https://atniclimate.github.io/TieredSovereignDataFramework/)
([source](https://github.com/atniclimate/TieredSovereignDataFramework))

## Open Data & Open Science

- [Open Source Program Office](https://dsi.wisc.edu/initiatives/ospo/)
  - [Open Awards](https://ospo.wisc.edu/open-awards/)
- [Open Source LLMs](/AI/LLM.md#open-source-llms)
- [Hugging Face](https://huggingface.co/): a repository for models and datasets
- [Kaggle](https://www.kaggle.com/): a platform for data science competitions and datasets
- [Data Repositories](repositories.md)
- [Big Data](bigdata.md)
