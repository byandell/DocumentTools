---
title: "Prompt Examples"
parent: "Prompt Engineering"
permalink: /prompts/
---

# Prompt Examples

How will you later remember how you used
[Artificial Intelligence (AI)](../AI/) to advance your projects?
And how will you share your learning with others?
Here are some examples of prompts that I have used with AI agents to help me,
and teams in interacting with projects.
They illustrate a few principles along the way.

- [View Prompt Slides](https://byandell.github.io/DocumentTools/quarto/prompts.html)
- [Prompt Engineering](../AI/prompt.md)
- [Saving Prompts and Walkthroughs](#saving-prompts-and-walkthroughs)
  - [Sharing Prompts instead of Code](https://byandell.github.io/Gravity-and-Antigravity/#sharing-prompts-instead-of-code)
- [AI Agent Conversation](#ai-agent-conversation)
  - [System Instructions](#system-instructions)
  - [Prompt CRAFTs](#prompt-crafts)
  - [Conversations and Projects](#conversations-and-projects)
- [Several Prompt Examples](#several-prompt-examples  )
  - [Create a `README.md` for a Folder](#create-a-readmemd-for-a-folder)
  - [Create a Table of Contents for a File](#create-a-table-of-contents-for-a-file)
  - [Convert DOCX files to Markdown](#convert-docx-files-to-markdown)
  - [Assemble a Powerpoint Presentation](#assemble-a-powerpoint-presentation)
  - [Use GitHub Effectively](#use-github-effectively)
  - [Organize a Workflow](#organize-a-workflow)
  - [Document Folders in ResearchDrive](#document-folders-in-researchdrive)
- More detailed Prompt examples
  - [Version GitHub Docs](./github.md)
  - [Assemble Powerpoint](./powerpoint.md)
  - [Create Quarto Slides](./quarto.md)
  - [Refactor Workflows](./workflow.md)
  - [Configure Just-the-Docs](./justthedocs.md)
  - [Create Developer Guides (Blueprint)](./devel_guide.md)
    - [Create Developer Guide to `qtl2shiny` (Reference Case Study)](./devel_guide_qtl2shiny.md)
  - [Create Shiny App Gallery](./gallery.md)
  - [Plotly Debouncer & Iframe Embedding](./debouncer.md)
  - [Prepare to Move a GitHub Repo](./move_repo.md)
  - [Render R Markdown to GitHub Pages](./render_rmd.md)
  - [Create an `AGENTS.md` for a Project](#create-an-agentsmd-for-a-project)
    - [Global Agents Template](./global_agents_template.md)
    - [Agents CRAFT Templates](./agents_craft_templates.md)
  - [Check External Links](./check_links.md)
    - [Broken Links](./broken_links.md)
- Additional Pages
  - [Use `pkgdown` to Auto-Build GitHub Website](./github/pkgdown.md)

## Saving Prompts and Walkthroughs

If you just use prompts and don't keep track of them, you are missing an opportunity to easily document your work flow.
Not only that, saved prompts and walkthroughs can be used to reproduce your work
(see [Sharing Prompts Instead of Code](https://byandell.github.io/Gravity-and-Antigravity/#sharing-prompts-instead-of-code)).
A simple way to begin is to ask your AI agent to save your prompts in a file, e.g. `prompts.md`;
alternatively, or in addition, save the Walkthrough artifact that the AI agent creates into
a separate `walkthrough.md` file.
If you do more work within the same conversation, ask the AI agent to update these files.
Below are examples of prompts I have been developing.

**Prompts:**

- "save the prompts used in this conversation to `prompts.md`"
- "save the walkthrough to `walkthrough.md`"

You can do this at the beginning or end of a conversation.
You can do it by clicking the `Save` button in the top right corner of the conversation window, and the `Export` button on a walkthrough panel.
You can also (by hand or by prompt to AI) update or append to these files.

**Examples:**

- [sysgenAnalysis workflow walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-walkthroughs)
- [mkeller3Projects2: how I created this file and repo](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/tree/master#how-i-created-this-file-and-repo)
- [sysgenDO1200 prompts](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200/blob/main/prompts.md)

## AI Agent Conversation

A user interacts with an AI agent in a "conversation" or "chat session",
which involves a chain of prompts, often starting with a system instruction
and moving from a broad framing prompt to specific refinement prompts.
See
[Tyson's Advanced Techniques](https://tyson-swetnam.github.io/intro-gpt/prompts/#advanced-techniques).

### System Instructions

System instructions are prior prompts, entered before specific prompts.
They are meant to act as global rule to subsequent prompt chaining
in an AI conversation.
Tyson Swetnam has a nice example that I expand below for python _and_ R:

```
Please set up the following system instruction:
# Project Context
I'm a data scientist working on machine learning projects.
For Python code, always provide examples using `scikit-learn` and `pandas`.
For R code, always provide examples using `tidyverse`.
Include `docstrings` (python) or `roxygen2` (R) and type hints in all code.

# Response Preferences
- Be concise but thorough
- Explain complex concepts with analogies
- Always cite sources when making factual claims
```

- [System Instructions Intro](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instruction-introduction)
- [System Instructions Use](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions)
- [Agent Skills](../AI/context.md#agent-skills--skillmd-actionable-capabilities)

### Prompt CRAFTs

A prompt for a complicated task can have improved focus with the
[CRAFT](https://tyson-swetnam.github.io/intro-gpt/prompts/#the-craft-framework)
framework.
To illustrate, here is Tyson's example for a grant proposal.
Note that this focuses on the "draft introduction" rather than the whole proposal.

```
Context: I'm preparing a grant proposal for NSF funding on AI in education  
Role: Act as an experienced grant writer and education researcher  
Action: Review my draft introduction and suggest improvements  
Format: Provide feedback as tracked changes with explanations  
Tone: Professional, constructive, and encouraging
```

Here is one for beginning to build a set of `python` notebooks:

```
Context: I'm preparing a set of `python` notebooks to document flooding impact  
Role: Act as an experienced python programmer and software project manager  
Action: Review my draft plan for building the setup notebook  
Format: Provide feedback as tracked changes with explanations  
Tone: Professional, constructive, and encouraging
```

Subsequent "chained" prompts would refine the `Action` framing
to build the first notebook,
then move on to build related notebooks.

### Conversations and Projects

There could be several different conversations within a project,
with a project usually in its own folder or set of folders.
Best practices include saving projects as GitHub repos
to both share with others and evolve the project over time
through edits documented through
[version control](https://github.com/resources/articles/what-is-version-control).
Of course, saving prompts for those conversation with a project
will help with later recall of how the project developed.

---

## Several Prompt Examples

### Create a `README.md` for a Folder

**Prompts:**

- "create a `README.md` document that concisely summarizes contents of this folder at a high level"
- "update `README.md` with any additional files, obeying restrictions in `.gitignore`"

**Example:**

- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)
- [sysgenDO1200](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200/blob/main/README.md) has various examples

### Create an `AGENTS.md` for a Project

An
[AGENTS.md](https://agents.md/)
file serves as an onboarding handbook and operating contract for AI agents working in a repository.
Pairing a global `~/.agents/AGENTS.md` (System Instructions, see
[Global Agents Template](global_agents_template.md))
with a project-level `AGENTS.md` organized via the
[CRAFT framework](../AI/agents.md#structuring-project-rules-with-the-craft-framework) keeps token counts low and instructions sharp.

**Prompts:**

- "create `AGENTS.md` for this project following the CRAFT framework (Context, Role, Action, Format, Tone)"
- "make a condensed version of `AGENTS.md` tailored for small LLMs"

**Examples:**

- [Document Digital Tools `AGENTS.md`](https://github.com/byandell/DocumentTools/blob/main/AGENTS.md)
- [Agents and Workspace Rules Guide](../AI/agents.md)
- [`byandell.github.io` file `AGENTS.md`](https://github.com/byandell/byandell.github.io/blob/master/AGENTS.md)

### Create a Table of Contents for a File

Just as you can create a `README.md` for a folder, you can create a table of contents for that `README.md` (or any markdown) file.

**Prompts:**

- "create TOC for `README.md`"
- "update TOC for `README.md`"

**Example:**

- [README for this repo](../)
- [Table of Contents for this file](#table-of-contents)
- [Pipelines in mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md#pipelines)

Once you have these and establish a "culture" of updating them, the AI will sometimes make the changes on the fly as you evolve your material.

### Convert DOCX files to Markdown

This prompt use
[pandoc](https://pandoc.org/) to convert `docx` files to `md` files.
This app needs to be installed once on a laptop to use.

**Prompt:** "find `docx` files and use pandoc to convert them to `md` versions"

**Example:**

- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)

### Assemble a Powerpoint Presentation

**Prompt:**

- "Use Quarto to automatically generate a PowerPoint deck (`.pptx`) embedding all of the outputted PNG figures."
- "Add a table of contents slide to the presentation."

This prompt assumes that you have installed
[Quarto](https://quarto.org/) (only need to do once)
and have already generated the PNG figures using the workflow prompt.
It could be part of a more involved prompt that also generates the figures.
The AI will likely include a title slide; you can also ask AI to add other material such as references or overview of experiment.

**Example:**

- [powerpoint.md](./powerpoint.md)

This prompt was used to create the powerpoint presentation for a GTT project.
For more detail, see
[Sharing  Prompts instead of Code](https://byandell.github.io/Gravity-and-Antigravity/#sharing-prompts-instead-of-code).
The saved file includes Alan and Diana's versions of the prompt . For details on how the prompt evolved, click on `Blame` (top left) or `History` (top right).
The displayed version is the most recent (Diana's);
the same file contains
[Alan's earlier version](https://github.com/byandell/DocumentTools/commit/6bf9b23a9a2441bd8c60cd18d88bcbc4a00c6ae7#diff-0a4691c74dedbcb4de422d849e3ff48d756dfcc06d20f0253ef5315dbaf9d912).

Another user could create a prompt that cites this prompt file and directs AI to
substitute different data and code files.
However, the prompt as written is rather specific to GTT for DO founder mice,
and in particular to NZO and B6 strains.
A user could further specify to replace step 2 with their own version of instructions.

### Use GitHub Effectively

These prompts interact with Git and set up files to be pushed to GitHub.
To use these, a GitHub account and working knowledge of how Git and GitHub work is assumed.

- [Commit to GitHub multiple versions of an R file](#commit-to-github-multiple-versions-of-an-r-file)
- [Resolve Git Hell Conflicts](#resolve-git-hell-conflicts)
- Additional Pages
  - [Version GitHub Docs](./github.md)
  - [Refactor Workflows](./workflow.md)
  - [GitHub](../github/)

#### Commit to GitHub multiple versions of an R file

**Prompt:**
Find files ending in `[ _]v[0-9]+.R$`
that have the same name before this version.
If there is more than one set, do the following steps for each set.
Denote by `[basename]` the part of the filename before the version number.

1. If there is not a `v1` version but there is the `[basename]`
without a version, copy `[basename].R` to
`[basename] v1.R` or `[basename]_v1.R` as appropriate.
If there is already a `[basename] v1.R` or `[basename]_v1.R`,
do not overwrite it,
but instead copy the `v1` version to `[basename].R` for this set.
2. Commit `[basename].R` with message `v1` and the date this file was created.
(Be careful with files that have implicit `v1`.)
3. For subsequent versions, copy the next highest version number
to `[basename].R` and commit
with the next version number and the date this file was created.
Continue until all versions are committed.
4. Do not include the singleton files such as `source*v2.R`.
5. Make sure to keep the versioned files intact.

***

The above prompt is a great task for an AI or an automated script. The original prompt is logically sound but can be streamlined to be more "instructional" and clear about the desired state.
The file
[Version GitHub Docs](./github.md) has an improved, more concise version of the prompt.

***

**Examples:**

- [Version GitHub Docs](./github.md)
- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)

For details of versions, see for instance
[MafA_SNP_DEG_Integration.R](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/MafA_SNP_DEG_Integration.R)
and click on `Blame` (top left) or `History` (top right).

#### Resolve Git Hell Conflicts

**Prompt:** "i messed up and forgot to do `git pull` before commiting new files. Now I am in git hell. See the message with `git status`. `Walk me through how to fix this.`"

**Example:**

This was used on the Multiple Versions prompt above.
The first time, I forgot to `git pull` changes I made on `GitHub` before starting. I tried to solve by myself and got lost. AI sorted it out.
See [GitHub](./github/) for more information.

### Organize a Workflow

This complicated prompt requires various tools on one's laptop,
notably
[devtools](https://devtools.r-lib.org/)
and
[roxygen2](https://roxygen2.r-lib.org/)
in `R`.
Installing the standalone app
[Quarto](https://quarto.org/)
gives one a markdown engine that can render markdown files to html, docx, pdf, and other formats.
Other `R` packages will likely be needed along the way.

**Prompt:** "build a concise prompt that captures the essence of the walkthroughs in `inst/doc/walkthrough.md`"

**Examples:**

- [workflow.md](./workflow.md)
- [workflow prompt](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-prompt)
- [workflow walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-walkthroughs)

The
[workflow.md](./workflow.md)
is a refinement of the workflow developed for
[sysgenAnalysis](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/).
This particular prompt, which is described conceptually in
[Prompts to Organize Workflows](../AI/prompt.md#prompts-to-organize-workflows),
transforms an R workflow into functions in an R package,
including a function to run the workflow and another function to explore the results.

This workflow for organizing workflows (!) was developed organically.
Each day, I advanced the project through a series of prompts;
at the end of the session, I asked the AI agent to save the
[workflow walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-walkthroughs),
including the date of that step.
At some point, I asked AI the above prompt, which resulted in a comprehensive
[workflow prompt](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-prompt).
I later asked the AI agent to modify the workflow prompt as I added subsequent workflow steps.

### Document Folders in ResearchDrive

Several of the prompts shown earlier concern building documentation for data and code kept in folders in the
[ResearchDrive (RD)](https://it.wisc.edu/services/researchdrive/).
While the RD is secure and private, I have made public versions of some code and documentation via the
[Attie Lab Systems Genetics GitHub](https://github.com/AttieLab-Systems-Genetics).
Having these public allows us to share ideas with others and to use them as a reference for future projects,
while still keeping research data secure.

- Data and Scripts in folder `mkeller3/General/main_directory`
  - Added
    [README.md](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200/blob/main/README.md)
    for this folder and some sub-folders
  - Created GitHub repo with these READMEs for version control at
    [AttieLab-Systems-Genetics/sysgenDO1200](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200)
  - See info at top of this file for how I did this
- Code in folder `mkeller3/General/Projects2/R scripts`
  - Added
    [README.md](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)
    for this folder
  - Created GitHub repo for version control at
    [AttieLab-Systems-Genetics/mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2)
  - Used version control to keep track of multiple versions of the same analysis (see
  [Improved Multiple Versions Prompt](#improved-multiple-versions-prompt))
