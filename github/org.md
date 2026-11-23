---
title: "Collaborate with GitHub Organizations"
parent: "Share Projects with GitHub"
nav_order: 1
---

# Collaborate with GitHub Organizations

- [References](#references)
- [My GitHub Organizations](#my-github-organizations)
- [Organization Profile README](#organization-profile-readme)
- [Organization Authorization (OAuth)](#organization-authorization-oauth)

A GitHub organization allows a team (or an individual like me)
to collaborate on related repositories.
The organization `owner`(s) manage `member`(s) and repositories (repos).
Each repo can be `public` or `private`, and members can have one of 5 `permission` levels
with increasing level of control/danger: read, triage, write, maintain or admin.
Organization and repo membership are managed, respectively,
with the `Settings` menu in the upper right-hand corner.

## References

- [How to Create a GitHub Organization From Scratch (GeeksforGeeks)](https://www.geeksforgeeks.org/git/how-to-create-github-organization-from-scratch/)
- [What Are GitHub Organizations and Should You Use One? (How-To Geek)](https://www.howtogeek.com/devops/what-are-github-organizations-and-should-you-use-one/)
- [GitHub Organizations and Teams Documentation (GitHub)](https://docs.github.com/organizations)
- [Managing an organization (git-scm.com)](https://git-scm.com/book/en/v2/GitHub-Managing-an-organization.html)

## My GitHub Organizations

I belong to a variety of
[GitHub Organizations](https://github.com/settings/organizations):

- My Organizations
  - [byandell-envsys](https://github.com/byandell-envsys)
  - [byandell-sysgen](https://github.com/byandell-sysgen)
- UW-Madison Organizations:
  - [UW-Madison Data Science Institut (DSI](https://github.com/UW-Madison-DSI)
  - [UW-Madison Data Science Hub](https://github.com/UW-Madison-DataScience)
- CU-Boulder Environmental Organizations:
  - [Environmental Data Science Innovation and Impact Lab (ESIIL)](https://github.com/cu-esiil)
  - [ESIIL Education](https://github.com/cu-esiil-edu)
  - [Earth Analytics Education Program (Earth Lab)](https://github.com/earthlab-education)
- Oglala Lakota College (OLC)
  - [OLC Geospatial Data Science Hub](https://github.com/olc-techsupport)

## Organization Profile README

An optional special repo in an organization, `.github`, can be used to provide an organization-level README and default settings.
I use mine to provide a brief introduction to an organization and links to its resources.
For instance, see the
`.github/README.md`
file in my
[byandell-envsys](https://github.com/byandell-envsys)
and
[byandell-sysgen](https://github.com/byandell-sysgen)
repositories.
The
[`envsys` README.md](https://github.com/byandell-envsys/.github/blob/main/profile/README.md)
is very simple, providing a one-paragraph intro and links to resources.
In contrast, the
[`sysgen` README.md](https://github.com/byandell-sysgen/.github/blob/main/profile/README.md)
has dropdown sections to help
organize multiple repos.
This is done with old style HTML code:

```
<details>
<summary>QTL Repos</summary>
<br>
...
</details>
```

## Organization Authorization (OAuth)

**Prompts:**

- Fix github sync issue: You don't have permissions to push to "byandell-sysgen/qtlnet" on GitHub. Would you like to create a fork and push to it instead?
- I don't see "Applications" on <https://github.com/organizations/byandell-sysgen/settings/profile>

**Responses:**

### Root Cause

- `byandell-sysgen/qtlnet` is hosted under a **GitHub Organization** (`byandell-sysgen`, active and not archived).
- Your local `origin` remote was configured with **HTTPS** (`https://github.com/byandell-sysgen/qtlnet.git`), which routes sync/push in the IDE through its GitHub OAuth app. GitHub organizations block unapproved third-party OAuth apps by default, causing the IDE to report no push permission and offer to fork.
- Meanwhile, your SSH key is already authenticated to GitHub as `byandell` (`ssh -T git@github.com` confirmed: `Hi byandell! You've successfully authenticated`).

### Repo Fix Applied

- Updated [`.git/config`](file:///Users/brianyandell/Documents/Research/byandell-sysgen/qtlnet/.git/config#L8-L10) to switch `origin` from HTTPS to SSH:

  ```text
  git@github.com:byandell-sysgen/qtlnet.git
  ```

- Verified read-only connectivity via `git ls-remote origin`, which resolved `refs/heads/master` cleanly over SSH.

You can now stage, commit, and sync/push directly to `byandell-sysgen/qtlnet` from the IDE or terminal (no fork needed).

Switching `origin` to SSH `git@github.com:byandell-sysgen/qtlnet.git` bypasses OAuth app restrictions, so `git push` / IDE sync should work without changing any GitHub web settings.

### Organization-level Fix

> **Optional (for other HTTPS repos in `byandell-sysgen`)**: If you also want HTTPS/OAuth syncing in the IDE to work for other repositories in the `byandell-sysgen` organization without switching each one to SSH, go to GitHub → **Settings → Applications → Authorized OAuth Apps** → select your IDE's GitHub OAuth app → click **Grant** next to `byandell-sysgen` (or adjust **Third-party access → OAuth application policy** in the `byandell-sysgen` organization settings).

**"Applications"** is in your **Personal** GitHub settings, not on the **Organization** settings page. Here are the two exact places:

#### Option 1 — Right on the `byandell-sysgen` Organization Settings page you have open

1. In the left sidebar under **Third-party Access**, click **OAuth app policy** (`https://github.com/organizations/byandell-sysgen/settings/oauth_application_policy`).
2. Approve any pending OAuth app requests (click **Review** → **Grant access**), or remove OAuth app access restrictions for the org if you prefer.

#### Option 2 — From your Personal GitHub Settings (to grant a specific IDE app)

1. Click your **profile avatar** (top-right corner of GitHub) → **Settings**.
2. In the left sidebar under **Integrations**, click **Applications** → open the **Authorized OAuth Apps** tab.
3. Click your IDE's OAuth app (e.g., **Visual Studio Code** / **GitHub for VS Code**) → under **Organization access**, click **Grant** next to `byandell-sysgen`.
