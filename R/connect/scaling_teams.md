---
title: "Scaling R & Data Science Teams"
parent: "Connect Data Tools Beyond `R`"
grand_parent: "R Language"
nav_order: 3
---

# Scaling R & Data Science Teams

Modern data science demands scaling computation beyond single machines and coordinating analysis workflows across multidisciplinary teams.

---

## 1. Scaling the Split-Apply-Combine Paradigm


The [split-apply-combine philosophy for data tables](../curate/data_tables.Rmd) scales up to much larger problems. Sometimes the tables themselves grow too big for one computer (or CPU); other times the tables may be reasonably sized, but the tasks are numerous. This split-apply-combine at scale has been called map-reduce, hadoop and high throughput computing.
The idea is to take a big task; split it into many (1000s or millions) small tasks; send each of those to a separate CPU; and combine the results back together (reduce) once all are completed. These projects typically take 1000s of compute hours, and in some cases millions.

This works best when tasks are "parallel" -- can be done independently of each other, such as separate simulations from the same model system. Unfortunately, some loosely coupled tasks depend on each other and require more complicated arrangements, perhaps even needing high performance computing such as graphical CPUs, or GPUs.

- [MapReduce](https://en.wikipedia.org/wiki/MapReduce)
- [Hadoop](https://hadoop.apache.org/)
- [Berkeley Spark]() | [sparlyr package](https://blog.rstudio.org/2016/09/27/sparklyr-r-interface-for-apache-spark/)
- [HTCondor](https://research.cs.wisc.edu/htcondor/)
- [DeltaRho](http://deltarho.org/)

## High Throughput & High Performance Computing

- [R/parallel](http://www.rparallel.org/) ⚠️
- [Parallel R book (Q. Ethan McCallum, Stephen Weston, 2011, O'Reilly
    Pub.)](http://shop.oreilly.com/product/0636920021421.do)
- [Vaughan LK, Srinivasasainagendra V (2013) Where in the genome are
    we? A cautionary tale of database use in genomics research. Front.
    Genet. 4:38.](http://dx.doi.org/10.3389/fgene.2013.00038)
- [Data-Intensive
    Science](http://www.delsaglobal.org/news/publications/item/download/20_b530f9de17aca08b4fcee1d8bd78ea32) ⚠️
    think-piece from [Data-Enabled Life Science Research
    (DELSA)](http://www.delsaglobal.org/) ⚠️
- [Cloud Computing
    (Wikipedia)](http://en.wikipedia.org/wiki/Cloud_computing)
- [Grid Computing (Wikipedia: see list of national
    projects](http://en.wikipedia.org/wiki/Grid_computing)
- [Open Science
    Grid](http://www.openscienhttp://en.wikipedia.org/wiki/Cloud_computingxucegrid.org) ⚠️
- [HTCondor Project](http://research.cs.wisc.edu/htcondor/) | [Center
    for High Throughput Computing, UW-Madison](http://chtc.cs.wisc.edu/)
- [IEEE High Performance Computing
    Conference](http://www.hipc.org/hipc2012/index.php)
- [NVIDIA High Performance
    Computing](http://www.nvidia.com/object/tesla-supercomputing-solutions.html)
- [Simulation Based Engineering Lab,
    UW-Madison](http://sbel.wisc.edu/)
- [TurnKeyLinux.org](http://www.turnkeylinux.org/) |
    [OwnCloud.org](http://owncloud.org/)
- [OpenData Exchange](opendata.stackexchange.com) | [OpenData
    Foundation](opendatafoundation.org)
- [Algorithms, Machines, People (AMP Lab,
    UC-Berkeley)](http://amplab.cs.berkeley.edu/)
- [BIGDATA: White House Initiative](http://www.stat.wisc.edu/bigdata) ⚠️
- [BackBlaze Online Backup](http://www.backblaze.com) ([BackBlaze
    Storage Pod
    Details](http://blog.backblaze.com/2011/07/20/petabytes-on-a-budget-v2-0revealing-more-secrets/))
- [Dremel: Interactive Analysis of Web-Scale Datasets
    (Google)](http://research.google.com/pubs/pub36632.html)

---

## 2. Statistical Computing Beyond R

R is one of many languages and other electronic tools of value to
staticians.

- [General References](#general-references)
- Additional Pages
  - [R Language Tips & Tricks](/R/learn/learnR.md)
  - [Reproducible Research Tools](reproducible.md)

## General References

- [Statistical Computing Courses by Karl
    Broman](http://www.biostat.wisc.edu/~kbroman/teaching/) ⚠️
  - [Tools for Reproducible Research
        (2014)](http://kbroman.github.io/Tools4RR/)
  - [Notes for a Statistical Programming Course
        (2012)](http://kbroman.wordpress.com/2012/05/25/a-course-in-statistical-programming/)
  - [Advanced Statistical Computing (Karl Broman 2001
        Course)](http://www.biostat.wisc.edu/~kbroman/teaching/statcomp) ⚠️
- [UW ACI Data- and Software-Carpentry
    Workshops](http://aci.wisc.edu/data-carpentry-and-software-carpentry-workshops/) ⚠️
    ([Software-Carpentry.org](http://software-carpentry.org) &
    [Data-Carpentry.org](http://www.datacarpentry.org))
- [Statistical Computing](http://www.stat.cmu.edu/~cshalizi/statcomp/)
    & [Advanced Data Analysis](http://www.stat.cmu.edu/~cshalizi/uADA/)
    (Cosma Shalizi)
- [Statistical Computing Software (Mark Irwin,
    2005)](http://www.markirwin.net/stat135/)
- [Julia Language (distribute-enabled language that is similar to,
    faster than, younger than R)](http://julialang.org/)
  - [Julia: a new language for technical computing (Revolution
        Analytics)](http://blog.revolutionanalytics.com/2012/04/julia-a-new-language-for-technical-computing.html) ⚠️
  - [Doug Bates's empirical CDF in Rcpp &
        Julia](https://github.com/dmbates/ecdfExample)
  - [Gist regarding handling large data sets for genome-wide
        association studies using Julia vs R (Doug
        Bates)](https://gist.github.com/dmbates/5681368)
  - [Julia Workshop (Doub
        Bates)](http://nbviewer.ipython.org/github/dmbates/JuliaWorkshop/tree/master/)
  - [Julia Language
        Documentation](http://media.readthedocs.org/pdf/julia/latest/julia.pdf) ⚠️
- [GitHub](http://github.org)
  - [How GitHub uses GitHub to Build
        GitHub](https://speakerdeck.com/holman/how-github-uses-github-to-build-github)
  - [GitHub Tutorial (Karl
        Broman)](http://kbroman.github.io/github_tutorial)
- [GNU Make Tutorial (Karl
    Broman)](http://kbroman.github.io/minimal_make)
- [Information on SAS](http://www.stat.wisc.edu/~yandell/software/sas/)
- [Software Packages & Languages
    Information](http://www.stat.wisc.edu/~yandell/software/software.html)
- [StackOverflow Tags](http://stackoverflow.com/tags)
- [ElasticSearch](https://www.elastic.co/products/elasticsearch)

---

## 3. Team Science Workflows & Curriculum Organization

The project is for individuals in teams who are using, or planning to use, [R](http://r-project.org) to address problems in the data sciences. This assumes a first course in [Data Carpentry](http://datacarpentry.org) or some similar introduction to working with data using computer tools. However, for those who have not had that, links to appropriate material will be provided along the way.

This is not fully laid out as a course, although it could be used as such. Much of the material has been tried out in various courses and training venues. There are many references out to course and research material of others so that teams can build on their experience. That, in fact, is how any science progresses. A web version is at
<http://www.stat.wisc.edu/~yandell/R_for_data_sciences>. This material is being used in Fall 2017 for the [COMBEE R Study Group](https://github.com/ComBEE-UW-Madison/RStudyGroup#combee-r-study-group--uw-madison) at UW-Madison.

The [syllabus](../learn/syllabus.md) provides the broad organization. Material is organized into verb folders roughly based on this syllabus.

- [curate](../curate/) data structures
- [visualize](../visualize/) data relationships
- [organize](../organize/) data methods and documentation
- [analyze](../analyze/) data with linear and other models
- [profile](../profile/) code for efficiency and error checking
- [connect](./) with other data science tools beyond R

## Other material in this directory

item          | contents
------------- | -----------------
[overview](../learn/README.md) | Overview of R Material
[reference](../learn/reference.md) | list of references
[repositories](../../datasci/repositories.md) | list of data repositories
[learnR](../learn/learnR.md) | R Language Tips & Tricks
[history](../learn/history.md) | background material on `R` and Douglas Bates

Many people contributed to this material. Thanks to [Douglas Bates](https://github.com/dmbates/) for his coteaching and help in Fall 2014 and 2015. The [COMBEE R Study Group](https://github.com/ComBEE-UW-Madison/RStudyGroup#combee-r-study-group--uw-madison) kindly shared their study material, and are allowing me to use the R Study Group in Fall 2017 to test out this.

---

## 4. Professional Skills for Data Science

These materials are for statisticians at all levels who want to learn
more about modern network and computing tools for statistics. The course
for Fall 2015 is: Stat 627 Professional Skills for Data Science (1-2 cr,
Thursdays 1-2:15pm, 1010 MSC). [This is NOT the Stat 327 "Data Analysis
with R" course.] This is recommended for all new graduate students. It
will emphasize training in best practices with R, focusing on how to
organize your work (using Rstudio), how to build excellent graphics
(using ggplot2) and how to document your work (using R markdown), among
other things. This is being led by Brian Yandell and Doug Bates in Fall
2015; see [moodle
site](https://ay15-16.moodle.wisc.edu/prod/local/wiscservices/login/index.php) ⚠️,
[Stat 627 Syllabus](http://www.stat.wisc.edu/~yandell/data_science/Stat627Syllabus.pdf) and
[Jenny Bryan's Stat 545 at UBC](http://stat545-ubc.github.io) ⚠️. The
course covers

- installation of the RStudio application on personal computers and
    use of RStudio on departmental computers.
- Representation of data in R, including factors and data frames.
- Manipulation and display of data in R.
- Visualization of data with the ggplot2 package for R.
- The "R Markdown" language for literate programming and reproducible
    research.
- The R formula language and its use for fitting linear models and
    generalized linear models.
- Contrast specifications for factors and their impact on
    interpretation of coefficient estimates.

The raw material for Fall 2014 was at <https://github.com/dmbates/stat692>
with more material in [Yandell's Stat 692
Notes](/network-skills/stat692-notes) related to Bates's talks.

Much of the material below was added for Fall 2013. We used the
following network tools to deliver information:
[drupal](/network-skills) (open access web pages--this page);
[box](https://uwmadison.app.box.com/files/0/f/1134810127/Stat_692_Network_Skills_for_Statisticians)
(drop box for collaboration); and
[moodle](https://courses.moodle.wisc.edu/prod/course/view.php?id=1758) ⚠️
(course collaboration environment).

## Resource Topics and Useful Links

- [Communication & Writing](./reproducible_publishing.md)
- [Visualization & Graphics](../visualize/ggplot2.md)
- [Linux Operating System & bash Shell](./dev_environment.md)
- [R Language Tips & Tricks](../learn/learnR.md)
- [Going Beyond R](./scaling_teams.md)
- [High Throughput & High Performance Computing](./dev_environment.md)
    (distribute work across multiple processors)
- [Reproducible Research](./reproducible_publishing.md) (workflows, exact
    reproduction of work)
- [Big Data](../../datasci/bigdata.md) (going beyond the laptop)
- [Programs in Data Science](./academic_programs.md) (discovery & communication of patterns in
    data)
- Online Courses (learning & teaching tools)
- [Data Repositories](../../datasci/repositories.md)

We are in the age of [big data](../../datasci/bigdata.md), when it is not enough to
think of what you can do with the computer on your desk or lap. Further,
statistics as a field is being transformed by [analytics](./academic_programs.md),
the process of discovery and communication of meaningful patterns in
data. Today, statisticians of all flavors--from the most pragmatic to
the most theoretical--need a variety of computational tools, and we need
access to vast resources across computer networks. While many of us work
in closed shops, behind proprietary walls, the world of open source is
core to sharing methods and information. Thus, it is important to
understand the power and role of the [linux](http://www.linux.org)
operating system and of the [R](http://www.r-project.org) language.
However, these only the beginning. While we focus on computational
skills, communication is key to the field of statistics, and to science
in general. And visualization is at the core of communicating complex
ideas, providing a window of insight into the world of data. Today, much
communication is online, and we must learn how to leverage online data
and network tools to advance in the field, and to do our work
effectively.
