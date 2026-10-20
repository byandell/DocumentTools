---
title: "Prompt Engineering"
parent: "AI (Artificial Intelligence)"
nav_order: 4
---

# Prompt Engineering

Prompt engineering is the process of designing prompts that elicit the desired output from an AI model. It is a general approach to using AI tools, and can be applied to a wide range of tasks. So far, my focus has been on prompt engineering of code, or at least GitHub repositories.
Below is a schema I am developing.

- [View Prompt Slides](https://byandell.github.io/DocumentTools/quarto/prompts.html)
- [What is Prompt Engineering?](#what-is-prompt-engineering)
- [Prompts to Organize Workflows](#prompts-to-organize-workflows)
- [Learning about prompts](#learning-about-prompts)
- [Prompt Engineering References](#prompt-engineering-references)
- [Sharing Prompts instead of Code](https://byandell.github.io/Gravity-and-Antigravity/#sharing-prompts-instead-of-code)
- [Prompt Examples](../prompts/)
- [Reproducible prompts (ESIIL IGNITE Data Analytics)](https://earthdatascience.org/notebooks/15-reproducible-prompts/reproducible-prompts.html)

## What is Prompt Engineering?

Prompt engineering is about laying a digital trail of prompts that guide the AI toward what one wants to investigate, gradually refining. These are embedded in conversations one develops. It is possible, and now done regularly by experts, to develop a set of AI agents that respond to their own prompts and do part of their work. I don’t yet know how to manage such agents.

Prompts, and
[prompt engineering](https://www.promptingguide.ai/introduction/what-is-prompt-engineering) ⚠️,
is a useful way to develop tools without having to directly write code.
A great guide is Tyson Swetnam's
[Getting Started with Prompts](https://tyson-swetnam.github.io/intro-gpt/prompts/#getting-started-basic-prompt-structure).
However, if you just use prompts and don't keep track of them, you are missing an opportunity to easily document your work flow.
That is, how will you later remember what you did and how? And how will you share your learning with others?

A simple way to begin is to ask your AI agent to save your prompts in a file, e.g. `prompts.md`.
If you do more work within the same conversation, ask the AI agent to update the file.
The next section shows how I used this approach to organize a somewhat complicated workflow.
For some of my examples, see
[Sharing Prompts instead of Code](https://byandell.github.io/Gravity-and-Antigravity/#sharing-prompts-instead-of-code)
and
[Prompt Examples](../prompts/).

### Prompts to Organize Workflows

Workflows can get rather complicated.
Often, it is helpful to organize them into human-size chunks to make them easier to manage and understand.

I experimented with developing a series of prompts to transform a workflow into its components. The functions do the work but need not be viewed in the workflow. The workflow should be a concise document that shows the steps and the results together. The following steps should begin with a workflow file, e.g. ​`workflow.R`.
The workflow prompt is included in
[AI Prompt Examples](./prompts/#organize-a-workflow).

- Place the functions in their own R file (`functions.R`). This file should retain the comments that organize them into the workflow steps.
- Organize the workflow into a Quarto document (`workflow.qmd`). This file should invoke (source) the `functions.R` and have its R code in chunks, with the comments turned into section delimiters and text blocks.
- Modify the workflow to display results, with options to save images and tables as PDF and CSV files, respectively.
- Present the workflow in source and rendered form to be readable by a human.

Later prompts would modify the workflow to have options to examine different datasets.
Once I had understood these steps, I saw how I could have one comprehensive prompt that would orchestrate the process. I asked the AI agent to create this.
These initial efforts are in the
[sysgenAnalysis](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis)
repository, with the
[Workflow Prompt](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-prompt)
based on step-by-step instructions in the
[Workflow Walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-walkthroughs)

### Learning about Prompts

I began learning about prompts from
[Tyson Swetnam](https://www.tysonswetnam.com/),
who demonstrated at the
[ESIIL Innovation Summit 2025](https://cu-esiil.github.io/Innovation-Summit-2025/)
how a natural language paragraph could become an AI prompt.
I adapted this with the
[Draft AI Task using Claude and MCP](https://github.com/CU-ESIIL/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/blob/main/documentation/group-notes.md#draft-ai-task-using-claude-and-mcp)
for the
[Three Rivers ESIIL working group](https://cu-esiil.github.io/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/),
which became the section on
[AI Prompt Engineering](https://github.com/CU-ESIIL/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/blob/main/docs/index.md#ai-prompt-engineering).
This exciting project is on hold but has great potential.

### Prompt Engineering References

Below are some references on prompt engineering quickly culled from the web:

- What is Prompt Engineering?
[Coursera](https://cloud.google.com/discover/what-is-prompt-engineering),
[GitHub](https://github.com/resources/articles/what-is-prompt-engineering),
[Google Cloud](https://cloud.google.com/discover/what-is-prompt-engineering),
[IBM](https://www.ibm.com/think/prompt-engineering),
[Microsoft](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering),
[Prompting Guide](https://www.promptingguide.ai/introduction/what-is-prompt-engineering) ⚠️
- [Generative AI & Prompt Engineering (Tyson Swetnam)](https://tyson-swetnam.github.io/intro-gpt/)
  - [Core Features of Today's AI Tools](https://tyson-swetnam.github.io/intro-gpt/prompts/#core-features-of-todays-ai-tools)
  - [Getting Started with Prompts](https://tyson-swetnam.github.io/intro-gpt/prompts/#getting-started-basic-prompt-structure)
- [Prompt engineering Guide (Prompting Guide)](https://www.promptingguide.ai/)
- [Prompt design strategies (Google Gemini API)](https://ai.google.dev/gemini-api/docs/prompt-design) ⚠️
- [Prompt Engineering Overview (Claude)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
