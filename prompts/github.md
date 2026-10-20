---
title: "Version GitHub Docs"
parent: "Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 1
---

# Version GitHub Docs

**Challenge**:
As code (or other documents) evolve, it is too easy to just save another version.
Here we assume that is done as `[basename]_.R`, `[basename]_v1.R`, `[basename]_v2.R` and so on.
GitHub version control enables one to have just one file, `[basename].R`, and still have the history of all versions.

**Use**:
Be sure you are working in a folder where you want the new package components to live,
and that you have set this up as a git repository.
Type the following prompt into AI; it will find all files with multiple versions ending in `_v[0-9]+.R` or `v[0-9]+.R`.

**Prompt**:
"Run the
[Version GitHub Docs Prompt](#version-github-docs-prompt) in the current folder. Ask for `[basename]`."

## Version GitHub Docs Prompt

"**Reconstruct Git history for versioned R scripts** matching `[basename][ _]v[0-9]+.R`.

1. **Make sure to do a `git pull` first.**

For each set of files:

1. **Initialize v1**: If a `v1` file is missing but `[basename].R` exists, copy `[basename].R` to create the `v1` version. If `v1` already exists, overwrite `[basename].R` with its content to start the history.
2. **Commit Sequence**: For each version ($N = 1, 2, 3...$) in order:
    - Overwrite `[basename].R` with the content of version `vN`.
    - Commit `[basename].R` with message `vN`, using the file's original creation date as the commit timestamp.
3. **Safety Rules**:
    - Ignore singleton files (e.g., `source*v2.R`).
    - Keep all original versioned files (`v1`, `v2`, etc.) intact; do not delete them."

***

## Key Improvements Made

- **Logical Grouping**: Instead of listing steps as separate actions, it frames them as a single "Workflow for each set," which is easier for an AI to parse.

- **Clearer Conditional**: The "v1" logic is simplified into a "normalization" step that ensures the git history starts correctly regardless of whether the first version was named with a suffix or not.
- **Punchy Directives**: Uses bold headers (**Initialize**, **Commit Sequence**, **Safety Rules**) to make the constraints stand out.
- **Timestamp Clarity**: Explicitly mentions using the creation date as the "commit timestamp," which is the specific instruction needed for Git-based history reconstruction.

**Would you like me to help you execute this workflow on your current files?** I can see you have several matching sets like `MafA_SNP_DEG_Integration` and `Shiny app prototype for Mafa SNP DEG analysis`.
