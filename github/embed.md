---
title: "Embed Objects in GitHub Pages"
parent: "Publish GitHub Pages"
grand_parent: "Organize Projects with GitHub"
nav_order: 1
---

# Embed Objects in GitHub Pages

The way to link an object file, such as a image, PDF, or dynamic HTML,
is to save it in a portfolio repo that is rendered via GitHub pages,
such as using a `[homepage].github.io`.
HTML files (ending in `.html`) do not display well in GitHub,
but will display via GitHub Pages.
This can be done using the `![ ]( )` markdown syntax
or an HTML
[iframe tag](https://www.w3schools.com/TAGS/tag_iframe.asp).
(Note that the HTML tag `embed` is deprecated and should not be used.)

- [Display an Image](#display-an-image)
- [Link and Embed PDFs](#link-and-embed-pdfs)
- [Link a Dynamic HTML Page](#link-a-dynamic-html-page)
- [Embed a Dynamic HTML Page](#embed-a-dynamic-html-page)

## Display an Image

An image stored for GitHub Pages use is displayed using
`![QR Code](../images/adobe-express-qr-code.png)`
as shown with

![QR Code](../images/adobe-express-qr-code.png)

Simply linking to the image file
`[QR Code](../images/adobe-express-qr-code.png)`
will display it in another page when clicked.

[QR Code](../images/adobe-express-qr-code.png)

This is my profile QR Code.
See
[QR Codes for Github Pages](pages.md#qr-codes-for-github-pages)
for explanation.

## Link and Embed PDFs

Use the following HTML code to link to the PDF in your webpage:

```
<a href="path/to/yourfile.pdf" target="_blank">View PDF</a>
```

Optionally, embed the PDF directly,
with options to adjust size and appearance,
using an
[iframe tag](https://www.w3schools.com/TAGS/tag_iframe.asp):

```
<iframe src="path/to/yourfile.pdf" title="Title for the PDF" width="100%" height="600px"></iframe>
```

## Link a Dynamic HTML Page

We use Western Meadowlark (_Tasiyagnunpa_) migration from
[cu-esiil-edu/stars-03-migration-template](https://github.com/cu-esiil-edu/stars-03-migration-template)
to explore access a dynamic HTML object.
We try to display the remote file,
then using GitHub Pages rendering the locally stored in this repo.
The
[local copy](tasiyagnunpa_migration.html)
does not display well in github, preview mode, or on the portfolio page.

Here are 2 versions of the same HTML file with an explicit link.
The latter does display as it is located in a GitHub repo rather than
published via GitHub Pages.

- [portfolio page](https://byandell.github.io/DocumentTools/images/tasiyagnunpa_migration.html) (renders in separate page)
- [portfolio repo](https://github.com/byandell/DocumentTools/blob/main/images/tasiyagnunpa_migration.html) (does not display on page)

## Embed a Dynamic HTML Page

Here we embed the dynamic HTML page in this page using an
[iframe tag](https://www.w3schools.com/TAGS/tag_iframe.asp):

```
<iframe src="../images/tasiyagnunpa_migration.html"
 title="Tasiyagnunpa Migration"
 width="100%" height="600px"></iframe>
```

Note the `width` and `height`, which can be tweeked.
The `title` option is useful if for some reason the page does not render.

<iframe src="../images/tasiyagnunpa_migration.html"
 title="Tasiyagnunpa Migration"
 width="100%" height="600px"></iframe>

**Note:**
This image will not display properly in `Preview` mode or in the GitHub repo,
but it will display on the published page
<https://byandell.github.io/DocumentTools/github/embed.html>
once the edits are committed to GitHub.

---

## Shinylive WebAssembly Embedding & Performance Tradeoffs

The trade-offs of embedding WebAssembly-powered **Shinylive** apps directly into GitHub Pages center around **RAM consumption** and **CPU initialization overhead**.

### 1. The Core Performance Trade-Off

| Factor | Client-Side (Shinylive / Wasm) | Server-Side (Shinyapps.io / Posit Connect) |
| :--- | :--- | :--- |
| **Initial Load** | **Slow** (Downloads 20–40MB Wasm runtimes + packages). | **Fast** (Standard HTML/JS payload). |
| **Browser RAM** | **High** (~150MB–300MB per running app instance). | **Low** (Under ~20MB; server does all the heavy lifting). |
| **Server Cost** | **Zero** ($0 static hosting via GitHub Pages). | **Variable** (Requires running R/Python server). |
| **Scaling** | **Unlimited** (Scale to millions of users instantly). | **Limited** (Restricted by server core/memory limits). |

### 2. What Triggers High Browser Memory Usage?

- **Multiple WebAssembly Workers**: Each `{shinylive-r}` or `{shinylive-python}` block initializes a separate virtual R (WebR) or Python (Pyodide) session in the browser. If a single page embeds 3 separate interactive blocks, the browser spins up 3 distinct virtual runtimes, consuming 600MB–1GB of RAM.
- **Heavy Package Imports**: When importing packages like `ggplot2`, `dplyr`, or `DT`, WebAssembly must download, parse, and load binary packages into memory.
- **Service Worker Caching**: Shinylive uses Service Workers to cache compiled assets locally. Subsequent visits load instantly from disk cache, but runtime RAM consumption remains unchanged once the virtual session starts.

### 3. Mitigating Client Memory Overhead

1. **Isolation**: Place independent interactive demos in separate HTML files (e.g., in a `demos/` directory). When a visitor opens a demo, the browser boots exactly one Wasm thread.
2. **Automatic Garbage Collection**: When the user navigates back to the main documentation index, the browser terminates the worker thread and immediately reclaims ~250MB RAM.
3. **Avoid Multi-App Pages**: Never embed multiple standalone `{shinylive}` chunks on a single page. If you need multiple modules, compose them into a **single multi-module Shiny app** sharing one WebR worker.
4. **Static Fallbacks**: For resource-intensive dashboards, display a static preview screenshot with a "Launch Interactive WebAssembly Demo" link so workers spin up only on demand.

