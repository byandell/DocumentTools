---
title: "What is an AI Harness?"
parent: "AI Environments"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 1
---

# What is an AI Harness?

- [Origin of the term "harness"](#origin-of-the-term-harness)
- [Harness for Document Content Analysis](#harness-for-document-content-analysis)
- [Harness References](#references)

## Origin of the term "harness"

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

## Harness for Document Content Analysis

This section resulted from a conversation with Patrick Freeland
([ATNI Tribes](https://atnitribes.org/about/our-staff/),
[Liken Knowledge](https://www.likenknowledge.org/likeneers/patrick-freeland))
about the many projects he has been developing using Claude.
See
[ATNI Climate](https://github.com/atniclimate).
He framed the prompt below.

### Prompt

Let's describe the "harness" that the content analysis process is able to identify important information, make connections across the plans, etc. I am trying to explain our work to a colleague, and need help with a bit more articulation, how we are using subagents, skills, etc. and things Like the OCR core; if possible to create a "slide deck" on a web page

### Response

The harness we created is a local-first execution and assurance framework around the OCR engine. It
is broader than a test suite: it governs how documents enter the engine, how work is identified, how
outputs become durable, how interrupted jobs resume, and how every result can later be evaluated and
audited.

Its flow is roughly:

- Runtime diagnostics
- Read-only preflight
- Validated configuration + deterministic work key
- Native extraction / OCR pipeline
- Private artifact staging
- Checksum-verified publication + commit marker
- Manifest + optional SQLite persistence
- Progress, provenance, evaluation, and resume evidence

The main pieces are:

- Runtime harness: ocr-cli doctor resolves PDFium and Tesseract, checks versions and language packs,
and reports actionable failures without opening a document.
- Preflight harness: inventories a batch, checks source limits and runtime readiness, and reports
capabilities before processing. It does not invent duration estimates before local observations
exist.
- Deterministic execution harness: every reusable unit of work is keyed by source hash, validated
configuration, engine version, output schema, processing-contract version, and artifact selection.
Volatile details such as timestamps and run IDs cannot alter content artifacts.
- Transactional artifact harness: outputs are written to private staging, synced, published without
overwriting conflicting content, and finalized with a checksum-bearing commit marker. A manifest
success record is written only after this boundary is complete.
- Recovery and resume harness: interrupted or corrupted runs are detected through commit markers,
artifact inventories, and SHA-256 checksums. Matching work is skipped safely; incomplete or
conflicting work is retried or rejected.
- Resource and failure harness: source size, page count, rendered pixels, region count, artifact
size, and subprocess timeouts are enforced. Failures remain scoped as fatal, document, page,
region, or artifact failures rather than being misreported as empty content.
- Persistence harness: optional SQLite storage uses ordered transactional migrations, schema
validation, transactional document replacement, provenance event storage, and conservative
compatibility handling.
- Verification harness: Rust tests exercise deterministic output, injected failures, migration
rollback, timeout behavior, staged-publication recovery, corruption detection, and resume
semantics without processing real PDFs. The recorded F2 gate currently includes 327 Rust test
executions across its principal suites, plus clippy, formatting, Python parsing, schema parsing,
and source-network scans.
- Controlled runtime harness: real PDFium and Tesseract validation is kept separate from pure
verification and requires explicit authorization. Previous controlled evidence is recorded, but
normal tests do not open PDFs.
- Governed evaluation harness: committed JSON schemas define corpus governance, coverage dimensions,
visual adjudication, and measures such as CER, WER, reading order, layout F1, table structure,
visual preservation, silent loss, determinism, and recovery. Protected documents and results stay
in ignored local directories.
- Provenance harness: observational IEEE 2890-adapted schemas capture Data Actors, authorization,
custody, derivation, publication, and failures through a hash-chained local ledger and SQLite. It
supports disabled and observe; enforcement is deliberately unavailable.

The defining principle is that material content must not silently disappear. If the engine cannot
extract, preserve, classify, or publish something, the harness requires that outcome to remain
visible as failure or review evidence.

### Harness References

- [Anthropic courses](https://anthropic.skilljar.com/)
- [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills)
- [Harness design for long-running application development \ Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [Complete Guide to Agent Harness: What It Is and Why It Matters (Sarah Chen, Harness Engineering)](https://harness-engineering.ai/blog/agent-harness-complete-guide/)
- [What is Harness Engineering? (Emily Winks, atlan)](https://atlan.com/know/what-is-harness-engineering/)
- [AI Harnesses and CLIs, Explained (Grant Harvey, eero)](https://www.theneuron.ai/explainer-articles/ai-harnesses-and-clis-explained-the-real-reason-everyones-talking-about-infrastructure/)
- [What is a Harness? (Agentic Engineering, Jaymin West)](https://www.jayminwest.com/agentic-engineering-book/6-harnesses/1-what-is-a-harness)
- [What the Rapid Adoption of the “Harness” Metaphor in Artificial Intelligence Reveals About How We Conceptualize Human–AI Relations (Andrew Maynard)](https://andrewmaynard.net/what-the-rapid-adoption-of-the-harness-metaphor-in-artificial-intelligence-reveals-about-how-we-conceptualize-human-ai-relations/)
