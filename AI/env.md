---
title: "AI Environments"
parent: "AI (Artificial Intelligence)"
nav_order: 1
has_children: true
---

# AI Environments

We typically work with AI within an environment.
Most "traditional" tools are now flavored with AI suggestions,
including messaging and email apps
(which can be optionally turned off).
There are now innumerable AI tools for coding and analysis,
and this will not be a compendium.
Instead, I am trying to keep abreast of the landscape
that seems relevant to me,
and will add notes here as I learn more.

- [What is an AI Environment?](#what-is-an-ai-environment)
- [Integrated Development Environments (IDEs)](#integrated-development-environments-ides)
  - [Cloud-Based Research Environments](#cloud-based-research-environments)
  - [Google Gemini and Antigravity](#google-gemini-and-antigravity)
    - [Recovering Antigravity 1.x Conversations](recover_conversations.md)
  - [Other AI Environments](#other-ai-environments)
- [Agentic AI](#agentic-ai)
  - [SOUL.md](#soulmd)
  - [Agentic AI References](#agentic-ai-references)
- [Team Science Platforms](team.md)
- [Large Language Models (LLMs)](LLM.md)
- [What is an AI Harness?](#what-is-an-ai-harness)
  - [Harness Engineering References](#harness-engineering-references)

## What is an AI Environment?

An AI environment is a setting where artificial intelligence systems operate and interact with data and users.
It includes hardware, software, data, and algorithms that facilitate AI functions.
Environments can be physical (like robots) or virtual (like simulations or cloud platforms).
AI environments allow for real-time interaction and feedback between AI systems and their surroundings.
They often incorporate machine learning capabilities, enabling AI to adapt and improve over time.
Common applications include autonomous vehicles, smart homes, and virtual assistants.
([Google Gemini](https://gemini.google.com))

- [Types of Environments in AI (Geeks4Geeks)](https://www.geeksforgeeks.org/artificial-intelligence/types-of-environments-in-ai/)
- [What is an Environment in AI (Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2026/01/types-of-environments-in-ai/)
- [Environment in AI (ScholarHat)](https://www.scholarhat.com/tutorial/artificialintelligence/environment-in-ai)
- [What is Environment in AI: A Complete Guide (KeyGroup)](https://key-g.com/blog/what-is-environment-in-ai-types-of-environments-in-ai-a-complete-guide)

## Integrated Development Environments (IDEs)

Initially, it seemed important to understand
[Model context protocol (MCP)](https://modelcontextprotocol.io/),
the concept and protocol developed by Anthropic (and first available in
`Claude Code`). The revolutionary idea is that a large language model (LLM) is not just a text generator, but can interact with your other tools and data to get information and take actions.
However, this was quickly integrated into an
[integrated development environment (IDE)](https://www.geeksforgeeks.org/blogs/what-is-ide/)
building on
[Visual Studio Code (VScode or code)](https://code.visualstudio.com/)
so that one can edit code manually and/or interact with an LLM via
an AI agent in a side panel.
This AI agent uses MCP to connect with your data and code
under your guidance.
We need not be concerned about the MCP mechanics of LLM
communication with local (or cloud-based) tools and data.
Instead, we carry on conversations with an AI agent who,
with explicit permission from us,
changes local code or documents and creates reports.

### Cloud-Based Research Environments

Cloud-based research environments enable researchers,
including students and instructors,
to develop code, optionally with AI agent interactions,
without having to try to set up systems on their
own, idiosyncratic devices.

For those working directly in
[GitHub](../github/),
code generation within repos is improving with the nuanced integration of
[GitHub Copilot](https://github.com/features/copilot),
both for repo editing and for use in
[GitHub Codespaces](https://github.com/features/codespaces),
which is a cloud-based IDE optionally
integrated with each GitHub repo.
GitHub also has capabilities to publish
[GitHub Pages](../github/#github-pages),
such a personal or organization portfolios.

[Google Colab](https://colab.research.google.com/)
 provides a free and simple way to code in R and Python,
with optional AI support via
[Google Gemini](https://gemini.google/about/).

[CyVerse Discovery Environment](https://de.cyverse.org/)
is a cloud-based enviroment for data science and bioinformatics.
I have used this in conjunction with
[Environmental Science and Innovation & Impact Laboratory (ESIIL)](https://esiil.org/)
to catalyze instruction, research and tool development.
Recently, CyVerse DE added AI engines
[Roo and Cline](https://www.openxcell.com/blog/roo-code-vs-cline/)
to their VScode IDE environment.
(**NB: Roo and Cline seem to work best in a Chrome browser**.)
We can use LLM APIs from
[AI Verde](https://chat.cyverse.ai/)
to tunnel a variety of LLMs
into either CyVerse DE or other IDEs of our choice.
See
[AI-VERDE Manual & Resource Site](https://aiverde-docs.cyverse.ai/)
and
[AI Verde API](https://aiverde-docs.cyverse.ai/api/).

CyVerse and AI Verde use
[Jetstream2](https://jetstream-2.iu.edu) ⚠️
to host computing tools at scale.
Jetstream2 is part of the NSF-funded
[ACCESS](https://access-ci.org) ⚠️,
which provides free access to compute and AI resources at scale.
These resources also include
[HTCondor](https://htcondor.org)
and
[PATh](https://path-cc.io).
ACCESS resources typically require an educational account
and benefit from technical guidance.

### Google Gemini and Antigravity

Google Gemini has an enterprise contract with UW-Madison; hence I concentrate a bit on it here.
Much of this applies more broadly to other AI environments.
While Gemini is available via the browser, it is also being embedded
into a variety of tools.
These tools are evolving fast, due to competition as well as
tool advances through use of AI on the tool development process.

Google initially offered `Antigravity 1.0` as an extension of
[`VScode`](https://code.visualstudio.com/)
with a Gemini AI agent in the right panel.
On 19 May 2026, Google released
[`Antigravity 2.0`](https://antigravity.google/)
as a suite of 4 tools:

- `Antigravity 2.0`: full multi-agentic AI code development environment
- `Antigravity CLI`: command line interface (CLI), used in the terminal
- `Antigravity SDK`: software development kit (SDK), used by developers to build apps
- `Antigravity IDE`: integrated development environment (IDE), an updated version of the previous (`1.x`) IDE

Unfortunately, this release confused previous users.
The new tool, with the same name as the previous tool, presents
as a chat window without IDE-like features, and without clear indication
about how it differs from the prior tool, or how to get back
to the prior tool.
This will be a useful tool for
[vibe coding](https://vibe-coding.run/)
but not directly relevant to those of us developing code-based tools.
`Antigravity IDE` seems better suited for that task.
Again, unfortunately, the IDE did not carry any previous chat history
(known as `conversations`) over to 2.0.
See
[Recovering Antigravity Conversations](recover_conversations.md)
for a guide I wrote to recover them based on community response.

- [Google Gemini](https://gemini.google.com/)
  - [Generative AI Services at UW–Madison: Tools, Policies & Resources](https://kb.wisc.edu/ai/) ⚠️
  - [Prompt design strategies (Google AI for Developers)](https://ai.google.dev/gemini-api/docs/prompt-design) ⚠️
  - [File input methods (Google AI for Developers)](https://ai.google.dev/gemini-api/docs/file-inputs) ⚠️
  - [Import a GitHub repository & ask about it in the Gemini web app (UW-Madison)](https://kb.wisc.edu/ai/135575) ⚠️
  - [Connect Box (Google Cloud)](https://cloud.google.com/gemini-enterprise/docs/connect-box)
- [Antigravity](https://antigravity.google/)
  - [Google Antigravity Documentation](https://antigravity.google/docs/get-started)
  - [Getting Started with Google Antigravity (CodeLabs)](https://codelabs.developers.google.com/getting-started-google-antigravity)
  - [AI Recovering Antigravity 1.x Conversations](recover_conversations.md)

### Other AI Environments

`Antigravity` and many other IDEs began as forks of the
[VS Code](https://code.visualstudio.com/)
that integrate LLMs with collaboration on a user's local files and tools.
Some have evolved away from these roots toward standalone apps.

- [Anthropic's Claude Code](https://www.anthropic.com/product/code) ⚠️
- [Open AI's Codex](https://openai.com/index/openai-codex/)
- [Posit's Positron](https://posit.co/products/open-source/positron/) ⚠️
- [Cursor MCP Docs](https://docs.cursor.sh/mcp) ⚠️
- [Windsurf Review 2026: The AI IDE Redefining Coding Workflows (Second Talent)](https://secondtalent.com/insights/windsurf-review-2026-the-ai-ide-redefining-coding-workflows/) ⚠️

See caution in [Using R in VS Code with Radian](../R/radian.md)
about `radian` and AI environments.

## Agentic AI

There are concepts of "AI-native" and "agent-native" IDEs, but I am not sure I fully grasp the distinction.
It seems that "AI-native" concerns conversations with LLMs, while "agent-native" concerns the use of AI agents to do work.
Further, the straightforward use of conversations via prompt
and context engineering is often described (as below) in the
setting of using one AI agent at a time.

Nowadays (Spring 2026), sophisticated users of AI orchestrate multiple AI agents
to accomplish complex tasks.
[Claude](https://claude.com/solutions/agents),
[OpenAI ChatGPT][https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
and
[Google Antigravity](https://antigravity.google/)
have been evolving such capabilities quickly
in the commercial world.

### SOUL.md

There is an emerging concept of
[SOUL.md](https://soul.md/)
that defines each agent by the content
of a markdown file in a project folder.

- [SOUL Overview (Richard Weiss, Anthropic)](https://gist.github.com/Richard-Weiss/)
- [SOUL Template (OpenClaw)](https://docs.openclaw.ai/reference/templates/SOUL/)
- [SOUL Personality Guide (OpenClaw)](https://docs.openclaw.ai/concepts/soul)

This all takes time and practice
to build up both our ability
to understand and use multiple agents.
Selection and organization of appropriate agents for a task.
Further, multiple agents will likely require a larger monthly
fee, if using commercial agents.

### Agentic AI References

- [Agentic AI](https://tyson-swetnam.github.io/intro-gpt/agentic/)
- [Agent-Environment Interface in AI](https://www.geeksforgeeks.org/artificial-intelligence/agent-environment-interface-in-ai/)
- [Multi-Agent Orchestration Guide](https://www.agensi.io/learn/multi-agent-orchestration-guide)
- [Agentic Engineering (Jaymin West)](https://www.jayminwest.com/agentic-engineering-book/)
- [A multi-agent system for automating scientific discovery (Nature)](https://doi.org/10.1038/s41586-026-10652-y)

## What is an AI Harness?

According to
[Andrew Maynard](https://andrewmaynard.net/),
"the crystallizing moment came in early February 2026, when Mitchell Hashimoto — cofounder of HashiCorp and creator of
[Terraform](https://developer.hashicorp.com/terraform)
— published a blog post that gave the ... name ... “harness engineering”....
“It is the idea that anytime
you find an agent makes a mistake, you take the time to engineer a solution such that the agent
never makes that mistake again”
[(Hashimoto, 2026)]((https://mitchellh.com/writing/my-ai-adoption-journey)). ...
And on February 18, Ethan Mollick’s widely read guide to AI both popularized and started
the process of normalizing the term as it organized its entire framework around three concepts:
“Models, Apps, and Harnesses”
[(Mollick, 2026)](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the)."

As stated by Jaymin West,
"Ethan Mollick introduced the horse harness metaphor to explain why the term is well-chosen (Mollick, ~2026-Q1). A horse has raw physical capability — strength, speed, endurance. But raw capability cannot pull a plow, draw a carriage, or haul freight without a harness. The harness converts raw power into directed, controlled, useful work."
Sarah Chen stated,
"The Large Language Model (LLM) is a powerful horse, enormous raw capability, but no sense of direction, no understanding of boundaries, and no concept of “stop.” The harness is the bridle, reins, and saddle. It channels that power into controlled, useful work. Without it, the horse runs wherever it wants."

[Google Gemini](https://gemini.google.com)
attributed the horse metaphor for AI harness
to the late
[John McCarthy](http://jmc.stanford.edu/),
founder of the field of AI,
although I have not been able to find the term connected
with his name.
Interestingly, there is a horse photographer named
[Jon McCarthy](https://www.jonmccarthyphoto.com/),
and a (deceased) noted breeder of Irish Draft Horses named
[John McCarthy](https://chronofhorse.com/en/article/john-mccarthy/)
Perhaps Gemini conflated these?

- [My AI Adoption Journey (Mitchell Hashimoto)](https://mitchellh.com/writing/my-ai-adoption-journey)
- [A Guide to Which AI to Use in the Agentic Era (One Useful Thing, Ethan Mollick)](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the)

Here are some other analogies:

- "The model is commodity. The harness is moat.” (Sarah Chen)
- "The model is the engine. The harness is the car." (Grant Harvey)

According to [Google Gemini](https://gemini.google.com),
An AI harness is a framework designed to integrate AI capabilities into applications.
It provides tools and resources for developers to build and deploy AI models efficiently.
The harness often includes pre-built algorithms and data processing pipelines.
It facilitates the management of AI workflows, from training to deployment.
AI harnesses can enhance collaboration among data scientists and engineers.
They help streamline the process of scaling AI solutions across different environments.

### Harness Engineering References

- [Complete Guide to Agent Harness: What It Is and Why It Matters (Sarah Chen, Harness Engineering)](https://harness-engineering.ai/blog/agent-harness-complete-guide/)
- [What is Harness Engineering? (Emily Winks, atlan)](https://atlan.com/know/what-is-harness-engineering/)
- [AI Harnesses and CLIs, Explained (Grant Harvey, eero)](https://www.theneuron.ai/explainer-articles/ai-harnesses-and-clis-explained-the-real-reason-everyones-talking-about-infrastructure/)
- [What is a Harness? (Agentic Engineering, Jaymin West)](https://www.jayminwest.com/agentic-engineering-book/6-harnesses/1-what-is-a-harness)
- [What the Rapid Adoption of the “Harness” Metaphor in Artificial Intelligence Reveals About How We Conceptualize Human–AI Relations (Andrew Maynard)](https://andrewmaynard.net/what-the-rapid-adoption-of-the-harness-metaphor-in-artificial-intelligence-reveals-about-how-we-conceptualize-human-ai-relations/)
