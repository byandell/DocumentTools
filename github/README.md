---
title: "Share Projects with GitHub"
parent: "Document Tools"
nav_order: 3
has_children: true
permalink: /github/
---

# Share Projects with GitHub

- [View GitHub Slides](https://byandell.github.io/DocumentTools/quarto/github.html)
- [General GitHub and Git Information](#general-github-and-git-information)
- [Connect with GitHub](#connect-with-github)
- Additional Pages
  - [Collaborate with GitHub Organizations](org.md)
  - [Use CodeSpaces within GitHub](codespace.md)
  - [Publish GitHub Pages](pages.md)
    - [Deploy with GitHub Actions](actions.md)
    - [Shinylive Performance Tradeoffs](shinylive.md)
    - [Use `pkgdown` to Auto-Build GitHub Website](pkgdown.md)
    - [Build and Launch a Serverless Interactive Website](serverless.md)
  - [Version GitHub Docs](version.md)
  - [Prompt Examples](../prompts/)
    - [Create Developer Guides (Blueprint)](../prompts/devel_guide.md)
      - [Create Developer Guide to `qtl2shiny` (Reference Case Study)](../prompts/devel_guide_qtl2shiny.md)
    - [Create Shiny App Gallery](../prompts/gallery.md)
    - [Version GitHub Docs Prompt](../prompts/github.md)

## General GitHub and Git Information

- [GitHub Links (UW-Madison-DataScience)](https://github.com/UW-Madison-DataScience/R_for_data_sciences/blob/master/organize/github.md)
- [Get started with GitHub (Happy Git with R)](https://happygitwithr.com/usage-intro#usage-intro)
- [Git and GitHub Troubleshooting](https://happygitwithr.com/troubleshooting)
- [Install Git for Windows (Git-SCM)](https://git-scm.com/install/windows)
- [Install Git (Git Guides)](https://github.com/git-guides/install-git)

## Connect with GitHub

Posit's Connect is a platform for sharing resources such as R shiny apps, Quarto documents,
and python apps.

- [Posit Connect](https://posit.co/products/enterprise/connect/)

Deployment of apps using GitHub repos to a Connect server can be tricky, as Connect relies on the
`renv` package to create reproducible environments for your R projects.
A message like
**Deployment error: unknown package source**
indicates that the `renv` package does not recognize where a package was installed,
for instance if one uses `devtools::install_github()`.
`renv` cannot track the source well enough to reproduce it, and it refuses to bundle the app as a result.
The fix is to reinstall the package using `renv::install()` instead, which records the GitHub source in a way that `renv` can reproduce:

```r
renv::install("github_user/package_name")
renv::snapshot()
```

After running those two lines, retry the deployment. The snapshot validator should pass and the bundle should reach the server cleanly.
If for any reason that does not work, you can also try explicitly recording the source before deploying:

```r
renv::record("github_user/package_name")
```

- [renv](https://rstudio.github.io/renv/)
- [Manage dependencies with renv](https://www.r-bloggers.com/2021/03/new-on-techguides-manage-dependencies-with-renv/)
- [Using renv with Posit Connect](https://pkgs.rstudio.com/renv/articles/rsconnect.html)
- [R Package Management](https://docs.posit.co/connect/admin/r/package-management/)
