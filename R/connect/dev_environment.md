---
title: "Computing Environments: Linux, Bash, Docker, and Tooling"
parent: "Connect Data Tools Beyond `R`"
grand_parent: "R Language"
nav_order: 1
---

# Computing Environments: Linux, Bash, Docker, and Tooling

Effective data science in R often relies on Unix/Linux command-line environments, shell scripting (`bash`), text editors (`vi`, `emacs`), and containerized runtime environments (`Docker`, `Guix`).

---

## 1. Linux Operating System & bash Shell

Linux is the underlying operating system organizing compute clusters, servers, and cloud instances. Commands in Linux are executed via a "shell" language. The primary shell for Linux is the Bourne Again Shell (`bash`):

- **Shell Manuals & History**:
  - [Bourne Again Shell (bash) Wikipedia](http://en.wikipedia.org/wiki/Bash_(Unix_shell))
  - [GNU bash Manual](https://www.gnu.org/software/bash/manual)
  - [Chet Ramey: Usenix Article on bash](http://tiswww.case.edu/php/chet/bash/article.pdf)
- **Tutorials & Reference Guides**:
  - [Linux.org Beginner Tutorials](http://www.linux.org/forums/beginner-tutorials.53/) ⚠️
  - [Wikipedia History of Linux](http://en.wikipedia.org/wiki/Linux)
  - [The Linux Documentation Project (TLDP)](http://www.tldp.org/guides.html) ⚠️
  - [University of Surrey Unix/Linux Tutorial for Beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/)
- **Video Overviews**:
  - [The Origins of Linux (Linus Torvalds)](http://www.youtube.com/watch?v=WVTWCPoUt8w)
  - [Basic Linux Tasks](http://www.youtube.com/watch?v=OnSUX2otYos)

---

## 2. Containerized Environments: Docker & GNU Guix

[Docker](https://www.docker.com/) and [GNU Guix](https://www.gnu.org/s/guix) ⚠️ provide mechanisms for building, running, and sharing isolated software "containers". They eliminate "works on my machine" discrepancies and enable reproducible compute pipelines.

### Docker
- Multiplatform containerization engine.
- [A Hands-On Introduction to Docker](http://angus.readthedocs.io/en/2016/week3/CTB_docker.html)
- [AntiSMASH Biological Container](http://antismash.secondarymetabolites.org/)

### GNU Guix ⚠️
- Purely functional package manager and system distribution that does not require root permissions for user installs.
- Offers transactional upgrades, roll-backs, and per-user profiles.
- [Guix Notes (Pjotr Prins)](https://github.com/pjotrp/guix-notes)
- [Reproducible Software Environments in HPC with Guix (Courtès & Wurmus)](https://arxiv.org/abs/1506.02822)
- [GNU Guix in an HPC Environment (Ricardo Wurmus)](http://elephly.net/posts/2015-04-17-gnu-guix.html)

---

## 3. Editors & Historical Statistical Software Tools

- **Command-Line Editors**:
  - [GNU Emacs](http://www.emacs.org/) ⚠️
  - [Vim / vi Visual Editor](http://weber.u.washington.edu/~rells/R110/) ⚠️
- **Document Rendering & Typesetting**:
  - [LaTeX Document Preparation](reproducible_publishing.md)
  - Utilities for DVI and PostScript viewing: `xdvi`, `dvips`, `ghostview`.
- **Statistical Software Directories**:
  - [ASA Statistical Software Guide](http://www.amstat.org/profession/index.cfm?fuseaction=software) ⚠️
  - [Statistical Reporting with S/R (Frank Harrell)](http://biostat.mc.vanderbilt.edu/twiki/bin/view/Main/StatReport) ⚠️
