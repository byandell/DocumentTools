---
title: "Publish GitHub Pages"
parent: "Organize Projects with GitHub"
nav_order: 1
has_children: true
---

# Publish GitHub Pages

Publishing web-based materials is easy with
[GitHub Pages](https://docs.github.com/en/pages),
a free service for hosting static websites
useful for project documentation and personal portfolios.
The personal portfolio is typically built using a repo
with the name `[username].github.io`.
Subpages are built using `[username].github.io/[reponame]`
where `[reponame]` can is the name of a repo owned by
`[username]`.
The `[username]` can also be a
[GitHub Organization](#collaborating-with-github-organizations).

The resources below cover the basics of GitHub Pages
and provide links to my published pages and
more detailed guides and tutorials.

- [My GitHub Pages](#my-github-pages)
  - [My Documentation GitHub Pages](#my-documentation-github-pages)
  - [QR Codes for Github Pages](#qr-codes-for-github-pages)
- [GitHub Pages References](#github-pages-references)
- Additional Pages
  - [Embed Objects in GitHub Pages](embed.md)
  - [Automate with GitHub Actions](actions.md)

## My GitHub Pages

My main GitHub Page
[byandell.github.io](https://byandell.github.io),
with source at
<https://github.com/byandell/byandell.github.io>,
was modeled on (forked from)
<https://github.com/barryclark/jekyll-now>.
This has cool features like blog pages.

In addition to my main GitHub Page, I have several subpages
that are built separately in different GitHub repos.
Note that the `landmapyr` page is built within
the `byandell-envsys`
[GitHub organization](#collaborating-with-github-organizations),
which I created to organize my environment systems research projects.

- [byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools)
([source](https://github.com/byandell/DocumentTools)):
Documentation of Digital Tools (whole repo)
- [byandell.github.io/geyser](https://byandell.github.io/geyser/)
([source](https://github.com/byandell/geyser)):
Geyser Shiny App with Modules (`docs/` folder)
- [byandell-envsys.github.io/landmapyr](https://byandell-envsys.github.io/landmapyr/)
([source](https://github.com/byandell-envsys/landmapyr)):
Land Mapping Package (`docs/` folder)
- [byandell.github.io/esiil-stars](https://byandell.github.io/esiil-stars)
([source](https://github.com/byandell/esiil-stars)):
ESIIL Stars Training Notes (whole repo)
- [byandell.github.io/ESIIL](https://byandell.github.io/ESIIL)
([source](https://github.com/byandell/ESIIL)):
ESIIL Research (`docs/` folder using
[MkDocs](https://www.mkdocs.org/))

### My Documentation GitHub Pages

I developed
[Document Tools](https://byandell.github.io/DocumentTools)
to serve as a reference for the Digital Tools I use.
In the process, I learned how to use
[Just-the-Docs](../prompts/justthedocs.md)
as the theme, which includes many useful navigation features.
It interprets `README.md` files in folders
as top-level pages, with the `README.md` in the top-most
folder displayed as the homepage.
One mistake I made was that putting YAML front matter
in a `README.md`
such as for navigation order (`nav_order`),
requires adding a `permalink`,
which forces Jekyll to use that page as the top-level `index` page.
The corrected front matter, say for the top
[README.md](https://github.com/byandell/DocumentTools/blob/main/README.md):

```
---
title: "Document Tools"
nav_order: 0
permalink: /
---
```

I also learned that using `title:` and `parent:`
was a useful way to create a navigation hierarchy.

### QR Codes for Github Pages

I generated a
[QR Code](https://github.com/byandell/byandell.github.io/blob/master/images/adobe-express-qr-code.png)
that points to my profile page
<https://byandell.github.io>
using
[Adobe Express](https://www.adobe.com/express/feature/image/qr-code-generator) ⚠️.

![QR Code](../images/adobe-express-qr-code.png)

**Warning:**
Be careful generating QR codes. Do you really need more than one?
I only have one, and make sure that relevant links to my material
are easily findable from my profile page.

You cannot add an image directly to your wallet, but you can use third party
apps to create a pass that is added to your wallet.
I used
[Pass4Wallet](https://apps.apple.com/us/app/pass4wallet-store-cards/id1423106610).
other choices include

- [Add a QR code to Apple Wallet (QRCG)](https://www.qr-code-generator.com/blog/add-qr-code-to-apple-wallet/)
- [How to add a QR code to Apple Wallet (qrcodedynamic)](https://qrcodedynamic.com/blog/how-to-add-a-qr-code-to-apple-wallet/)

## GitHub Pages References

- [ESIIL Data Short Course: Create your own portfolio webpage](https://cu-esiil-edu.github.io/esiil-learning-portal/shortcourse/pages/03-git-github/03-github-portfolio/01-create-portfolio-website.html)
- [The Least You Need to Know About GitHub Pages](https://tomcam.github.io/least-github-pages/set-github-pages-master-branch.html)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Publish Your Project Documentation with GitHub Pages](https://github.blog/developer-skills/github/publish-your-project-documentation-with-github-pages/)
- [GitHub Page Themes](https://pages.github.com/themes/)
- [Jekyll Now](https://github.com/barryclark/jekyll-now)
  - [Build A Blog With Jekyll And GitHub Pages](https://www.smashingmagazine.com/2014/08/build-blog-jekyll-github-pages/)
  - [Other forkable themes](https://github.com/barryclark/jekyll-now/#other-forkable-themes)
- [GitHub Actions](https://docs.github.com/en/actions)
- [MkDocs](https://github.com/mkdocs/mkdocs/tree/master) (advanced topic)
  - [Materials for MkDocs: Publishing your site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)
  - [Deploying your docs](https://www.mkdocs.org/user-guide/deploying-your-docs/)
- [Resolving Git Push for CI/CD Workflows (TutorialPedia)](https://www.tutorialpedia.org/blog/how-to-resolve-refusing-to-allow-an-oauth-app-to-create-or-update-workflow-on-git-push/)
