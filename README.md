---
title: "Document Tools"
nav_order: 0
permalink: /
---

# [Document Tools](https://byandell.github.io/DocumentTools)

- [My Documentation Journey](#my-documentation-journey)
- [R Language](./R/) ([slides](./quarto/R.html))
- [Data Sciences](./datasci/) ([slides](./quarto/datasci.html))
- [Python Language](./python/) ([slides](./quarto/python.html))
- [GitHub](./github/) ([slides](./quarto/github.html))
- [Create Guides](guides.md)
- [Environmental Systems](./envsys/) ([slides](./quarto/envsys.html))
- [Shiny Apps](./shiny/) ([slides](./quarto/ShinyApps.html))
- [AI (Artificial Intelligence)](./AI/) ([slides](./quarto/AI.html))
  - [Prompt Examples](./prompts/) ([slides](./quarto/prompts.html))
- [Quarto Slides & References](./quarto/)

_[byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools)_
([GitHub](https://github.com/byandell/DocumentTools))

## My Documentation Journey

This repository is a collection of useful documentation and tutorials for various topics, mostly related to code languages and tools.
These were previously dispersed in various GitHub repositories and organizations, and have been consolidated here, with a few exceptions.
These reflect my ideas on how
[Data Evolve](https://byandell.github.io/Data-Evolve/) in concert with
the evolution of code-based tools and languages.
This historical collection has many broken links,
indicated by ⚠️ icons,
which I plan to fix over time.
See [Broken Links](./prompts/broken_links.md) for a summary.

- [R Language](#r-language)
- [Systems Genetics](#systems-genetics)
- [Environmental Systems](#environmental-systems)
- [Shiny Apps](#shiny-apps)
- [Learning about AI](#learning-about-ai)
- [Quarto Slides & References](#quarto-slides--references)
- [About These Pages](#about-these-pages)

### R Language

I first encountered `S` in the mid-1970's while at UC-Berkeley,
when David Brillinger brought a copy from Bell Labs.
Fellow student Ross Ihaka later went on to co-design `R`
(see
[Background R Material](R/learn/background.md)).
When I joined UW-Madison in 1982, I became friends with
[Doug Bates](https://www.stat.wisc.edu/~bates/)
who became (and still is) a key member of the core `R` development team.
I kept coming back to this system as it matured over coming decades.

My notes on [R](cran.r-project.org) were organized for a
2017
[COMBEE](https://hub.datascience.wisc.edu/communities/combee/)
short course in the
[UW-Madison Data Science Hub](https://hub.datascience.wisc.edu/), which remain in their
[UW-Madison-DataScience GitHub Organization](https://github.com/UW-Madison-DataScience/)
as the repository
[R_for_data_sciences](https://github.com/UW-Madison-DataScience/R_for_data_sciences).

### Systems Genetics

I have collaborated with System Genetics researchers for several decades,
with material gathered in my GitHub Organization
[byandell-sysgen](https://github.com/byandell-sysgen)
and in multiple publications
([see my CV](https://www.stat.wisc.edu/~yandell/vita.pdf)).
There is an evolution of code in the repositories of the `byandell-sysgen` organization.

### Environmental Systems

My exploration of earth data science (EDA) is in my GitHub Organization
[byandell-envsys](https://github.com/byandell-envsys).
This journey began with my introduction to the
[Environmental Data Science Innovation & Impact Lab (ESIIL)](https://esiil.org/).
I took some short courses on EDA through ESIIL, which led to my
[geospatial](https://github.com/byandell-envsys/geospatial) package;
with references now migrated to
[Environmental Systems](./envsys/).
I attended the ESIIL Innovation Summit in 2023 (and every year since),
which introduced me to many amazing people who have become friends.
An exciting mix of top-notch IT experts gather to share learning and access to state-of-the-art tools.
Through ESIIL I have gotten to know a collection of Tribal data scientists
with amazing skills and perspectives on knowledge, science, the earth and all our relatives.

My learning about environmental systems
spans technical, cultural and environmental spheres.
I have collaborated as part of the
[ESIIL Working Groups](https://esiil.org/working-groups)
for
[Maka Sitomniya (2024-2026)](https://github.com/byandell-envsys/Maka-Sitomniya)
(see
[ESIIL Data Library](https://cu-esiil.github.io/data-library/)
and
[datacube/notebooks](https://github.com/byandell-envsys/Maka-Sitomniya/tree/main/datacube/notebooks))
and
[Three Rivers (2025)](https://cu-esiil.github.io/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/).
The Maka Sitomniya working group led to an ongoing collaboration with the
[Sicangu Climate Center](https://sicangudata.org/) ⚠️.
Lately, I have joined the
[Wopasi Pazo ESIIL Working Group](https://esiil.org/working-groups/wopasi-pazo)

I began attending the Friday noon meetings of the
[Oglala Lakota College (OLC) Math, Science, and Technology Department](https://www.olc.edu/current-students/degree-programs-areas-of-study/math-science-tech/) ⚠️,
which has included a collaboration on Tribal boundary maps, gathered in the
[R](https://cran.r-project.org/) package
[landmapr](https://github.com/byandell-envsys/landmapr).
I was asked to be a senior advisor for the
[ESIIL Stars program](https://byandell.github.io/esiil-stars)
and am assisting with the OLC team.

The 2024-25
[CU Boulder EarthLab](https://earthlab.colorado.edu/) course
on [Earth Data Analytics](https://github.com/byandell-envsys/EarthDataAnalytics)
helped learn to organize
[Python](python/)
code and ideas.
I developed these into the
[landmapyr](https://github.com/byandell-envsys/landmapyr) package.
My notes on [Python](https://www.python.org/) and related topics developed during the course are in
[Python Language](python/) and [Environmental Systems](envsys/),
now gathered in this repository.

### Shiny Apps

I have been learning about [Shiny](https://shiny.posit.co/) since before I
attended the
[rstudio::conf(2017)](https://global.rstudio.com/resources/rstudioconf-2017/)
([slides](https://github.com/rstudio/rstudio-conf/tree/main/2017)).
Notes on my shiny apps are in
[Shiny Apps](./shiny/).
I created the
[geyser](https://github.com/byandell/geyser) repository
to help me consolidate my understanding of `Shiny` with concrete examples in `R` and `Python`.
This uses the
[Old Faithful shiny app](https://shiny.posit.co/r/gallery/start-simple/faithful)
where the data are included in the `R` system as `data(faithful)`,
and in the Python package
[seaborn](https://seaborn.pydata.org/) as `geyser`.

Developing the
[geyser](https://github.com/byandell/geyser) repo
gave me more experience with
[Quarto](https://quarto.org/)
for interactive slides and demos.
See
[Quarto Slides & References](./quarto/).

### Learning about AI

My learning about AI agents and tools continues to evolve.
Initial thoughts on so-called artifical intelligence are in my blog about
Jaron Lanier's
[There is no AI](https://byandell.github.io/Jaron-Lanier-There-is-no-AI/).
Ideas and notes on the concept and evolution of "AI" tools are in the
[AI ("Artificial Intelligence")](./AI/)
pages.

### About These Pages

_Migrated to GitHub Pages on 2026-06-16 with help of
[Convert Markdown to GitHub Pages](https://nicolas-van.github.io/easy-markdown-to-github-pages/)
by
[Nicolas Vanhoren](https://github.com/nicolas-van).
Modified theme in
[_config.yml](_config.yml)
to
[just-the-docs](prompts/justthedocs.md)._
