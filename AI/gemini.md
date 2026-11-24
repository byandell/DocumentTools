---
title: "Google Gemini & Antigravity"
parent: "AI Environments"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 2
---

# Google Gemini and Antigravity

- [Overview](#overview)
- [References](#references)
- [Gemini 4 Models](#gemini-4-models)
- Additional Pages
  - [Recover Antigravity 1](gemini_recover.md)

## Overview

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

## References

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

## Gemini 4 Models

- [Side-by-Side Comparison](#side-by-side-comparison)
- [How to Choose](#how-to-choose)

Google's Gemini 4 lineup uses chemical element names—Neon, Carbon, Hydrogen, and Argon—to represent different points along a speed, cost, and reasoning-depth curve rather than a simple sequential ranking. Neon leads recent intelligence benchmarks while offering faster execution and lower task costs than Carbon, Hydrogen targets high-speed, cost-efficient execution, and Argon serves as the earlier frontier release.

[1] (<https://artificialanalysis.ai/models/comparisons/gemini-4-neon-vs-gemini-4-hydrogen>)  
[2] (<https://www.mindstudio.ai/blog/google-gemini-4-model-lineup>)
[3] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)  

For a broader walkthrough of how the lineup fits together, MindStudio breaks down the release progression and practical trade-offs, while Medium covers how teams route tasks across the four models.

[1] (<https://www.mindstudio.ai/blog/google-gemini-4-model-lineup>)  
[2] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)

## Side-by-Side Comparison

- Gemini 4 Neon (Balanced Frontier & Analytical Reasoning): Adapted from Carbon to deliver top-tier intelligence with stronger speed and cost efficiency. According to Artificial Analysis benchmark comparisons, Neon (Xhigh) reaches 61 on the Intelligence Index (and 60 at High), with faster task completion (3.7 minutes at Low vs. 29.3 minutes for Carbon at Medium) and lower per-task cost ($0.75 at Low vs. $6.59 for Carbon at Medium). It performs strongly across finance/accounting, legal, engineering, and multimodal workflows, and supports a 1M unified context window (up to 64K default synchronous output tokens or up to 1M via background long decode).

[1] (<https://artificialanalysis.ai/models/comparisons/gemini-4-neon-vs-gemini-4-carbon>)  
[2] (<https://deepmind.google/models/model-cards/gemini-4-neon/>)  
[3] (<https://www.mindstudio.ai/blog/google-gemini-4-model-lineup>)

- Gemini 4 Carbon (Deep Long-Horizon Specialist): Built for sustained agentic sessions, complex system architecture, difficult repository-wide debugging, and cybersecurity tasks where persisting through multi-step problems matters most. On Artificial Analysis evaluations, Carbon (High) scores 60 on the Intelligence Index (and 65.2 on Terminal-Bench 4.0). It often takes longer and costs more per task than Neon, making it best reserved for high-stakes, long-horizon reasoning.

[1] (<https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/>)  
[2] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)  
[3] (<https://artificialanalysis.ai/models/comparisons/gemini-4-neon-vs-gemini-4-carbon>)

- Gemini 4 Hydrogen (Fast Execution & High Volume): Designed for low latency, cost efficiency, and high-throughput tasks such as everyday coding, prototyping, document processing, and worker/verifier roles in multi-agent setups. According to Google and benchmark reports, Hydrogen supports four thinking effort tiers (low, medium, high, and Xhigh), scores 51 at default high and 54 at Xhigh on the Artificial Analysis Intelligence Index, runs roughly three times faster than Carbon (~200 vs. ~76 output tokens per second), and offers lower task latency and cost (1.5 minutes and $0.29 at Low).

[1] (<https://www.youtube.com/watch?v=d_CSS58yrxY&t=110>)  
[2] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)  
[3] (<https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/>)  
[4] (<https://artificialanalysis.ai/models/comparisons/gemini-4-neon-vs-gemini-4-carbon>)  
[5] (<https://artificialanalysis.ai/models/comparisons/gemini-4-neon-vs-gemini-4-hydrogen>)

- Gemini 4 Argon (Original Frontier Release): An earlier frontier model strong in multimodal generalization and enterprise knowledge work (noted by Google DeepMind for a 14% accuracy gain over Gemini 3.1 Pro on enterprise knowledge work and priced at $2/M input and $10/M output tokens on OpenRouter). Newer releases have shifted its role: Hydrogen beats Argon's 50 Intelligence Index score at high effort (reaching 51 at default high and 54 at Xhigh) at lower cost, while Neon and Carbon take the lead on deeper reasoning and newer workflows.

[1] (<https://openrouter.ai/compare/google/gemini-4-argon>)  
[2] (<https://deepmind.google/models/gemini/>)  
[3] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)  
[4] (<https://www.youtube.com/watch?v=d_CSS58yrxY&t=110>)  
[5] (<https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/>)

## How to Choose

- Use Hydrogen for high-volume requests, quick prototypes, fast turnaround, or sub-agent execution where latency and cost are primary constraints.

[1] (<https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/>)  
[2] (<https://www.mindstudio.ai/blog/google-gemini-4-model-lineup>)  
[3] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)

- Use Neon as a default for complex analytical work, finance/legal/engineering tasks, and production agents needing high capability without Carbon's time and cost overhead.

[1] (<https://artificialanalysis.ai/models/comparisons/gemini-4-neon-vs-gemini-4-carbon>)  
[2] (<https://www.mindstudio.ai/blog/google-gemini-4-model-lineup>)  
[3] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)

- Use Carbon for tough architectural design, long-horizon debugging, and high-stakes tasks where deep persistence outweighs runtime and cost.

[1] (<https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/>)  
[2] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)

- Pair models in agentic workflows (such as using a stronger coordinator model with Hydrogen worker agents) when balancing accuracy, speed, and quota usage.

[1] (<https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/>)  
[2] (<https://medium.com/data-science-in-your-pocket/gemini-4-neon-vs-carbon-vs-hydrogen-vs-argon-cd5377c1f812>)

If you share your primary use case (such as coding agents, document analysis, or high-volume API traffic) and latency or budget constraints, I can help narrow down which model or multi-model setup fits best.
