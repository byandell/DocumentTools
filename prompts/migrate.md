---
title: "Migrate Documentation from DSHub"
parent: "Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 8
---

# Migrate Documentation from DSHub

In 2017 I gathered together material on R and other tools that I had been accumulating
and created
[R for Teams in the Data Sciences](https://github.com/UW-Madison-DataScience/R_for_data_sciences).
Unfortunately, the title is close to Hadley Wickham et al's
[R for Data Science](https://github.com/hadley/r4ds) book,
originally published in 2023.
Further, the material goes beyond `R` and is now somewhat date.

The goal is to migrate and update documentation
into this current local `Documentation` repository.
It should maintain the integrity of the existing documentation,
while incorporating new material.

## Initial Organization

The original organization is as follows.  Use this as a guide to determine where
to place material in this repo, as you migrate it.

<details>
<summary>Top Level Directories</summary>

```
R_for_data_sciences/
├── 2017Fall/
├── analyze/
├── connect/
├── curate/
├── organize/
├── profile/
├── R/
├── skills/
└── visualize/
```

</details>

<details>
<summary>Top-Level Files</summary>

```
R_for_data_sciences/
├── Bates.md
├── LICENSE
├── README.md
├── background.md
├── bash.sh
├── curate.md
├── learnR.md
├── migrate.md
├── overview.md
├── reference.md
├── repositories.md
└── syllabus.md
```

</details>

<details>
<summary>analyze</summary>

```
├── analyze/
│   ├── Formulas.Rmd
│   ├── README.md
│   ├── correlate.Rmd
│   ├── covary.Rmd
│   ├── linear_model.Rmd
│   └── sysgen.md
```

</details>

<details>
<summary>connect</summary>

```
├── connect/
│   ├── README.md
│   ├── beyondR.md
│   ├── docker.md
│   ├── latex.md
│   ├── linux.md
│   ├── reproducible.md
│   └── scaling_up.md
```

</details>

<details>
<summary>curate</summary>

```
├── curate/
│   ├── README.md
│   ├── applyExample.Rmd
│   ├── data_tables.Rmd
│   ├── file.Rmd
│   ├── intro_dplyr.Rmd
│   ├── purrr.Rmd
│   ├── regex.Rmd
│   ├── species.Rmd
│   ├── string.Rmd
│   ├── tidyverse.Rmd
│   └── x.txt
```

</details>

<details>
<summary>organize</summary>

```
├── organize/
│   ├── BatesNotes.Rmd
│   ├── README.md
│   ├── Rmarkdown.md
│   ├── RmarkdownExample.Rmd
│   ├── SQLiteDplyr.Rmd
│   ├── database.md
│   ├── function.Rmd
│   ├── github.md
│   ├── package.Rmd
│   └── writing.md
```

</details>

<details>
<summary>profile</summary>

```
├── profile/
│   ├── README.md
│   ├── lineprof.Rmd
│   ├── profile.Rmd
│   └── simulate.Rmd
```

</details>

<details>
<summary>R</summary>

```
├── R/
│   ├── rmd_ask.R
│   └── surveys_ggplot.R
```

</details>

<details>
<summary>skills</summary>

```
├── skills/
│   ├── README.md
│   ├── bigdata.md
│   ├── blended_online.md
│   ├── nontrad.md
│   ├── profSkills.md
│   ├── programs.md
│   ├── software.md
│   └── stat692notes.md
```

</details>

<details>
<summary>visualize</summary>

```
└── visualize/
    ├── README.md
    ├── ggplot2.Rmd
    ├── graphics.md
    ├── network/
    │   ├── Data files/
    │   │   ├── Dataset1-Media-Example-EDGES.csv
    │   │   ├── Dataset1-Media-Example-NODES.csv
    │   │   ├── Dataset2-Media-User-Example-EDGES.csv
    │   │   ├── Dataset2-Media-User-Example-NODES.csv
    │   │   ├── Dataset3-Airlines-EDGES.csv
    │   │   ├── Dataset3-Airlines-NODES.csv
    │   │   └── Images/
    │   │       ├── news.png
    │   │       ├── puppy.png
    │   │       └── user.png
    │   ├── Polnet 2016 R Network Visualization Workshop.R
    │   ├── README.md
    │   ├── network2_igraph.Rmd
    │   ├── network_data.Rmd
    │   ├── network_igraph.Rmd
    │   └── network_visNetwork.Rmd
    ├── shiny/
    │   ├── app.R
    │   ├── server.R
    │   └── ui.R
    ├── shiny.Rmd
    └── visualize.md
```

</details>

## Manual Migration

Repo was cloned to `~/Documents/GitHub/R_for_data_sciences`
and copied into this repo into the following places:

- `organize/github.md` to `./github/organize.md`
- create `./data/`
- `repositories.md` to `./data/`
- `connect` to `./connect/`
- `organize/writing.md` to `./connect/`
- `skills/bigdata.md` to `./data/`
- `skills/` to `./connect/`
- create `learn` under `./R/`
- `README.md` to `./connect/plan.md`
- `reference.md`, `syllabus.md`, `Bates.md`, `learnR.md`, `background.md`, `overview.md` to `./R/learn/`
- `analyze`, `curate`, `organize`, `profile`, `visualize` to `./R/`

## Reorganize New Content

### Review Contents in `./github/` folder

- rename `organize.md` to `version.md`
- add TOC and update content in `version.md`
- update `README.md`

### Review Contents in `./R/` folder

- reorg `./R/learn/` material

### Review Contents in `.connect/` folder

The `connect/` folder is a mix of a few different things.
Use the organization structure gleaned in the slides `quarto/R.qmd`

## Review Contents in `./data/` folder

## Update Links Throughout

Internal links should be updated to reflect the new location of the files.
External links should be reviewed and updated if necessary.
