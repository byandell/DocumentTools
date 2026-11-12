---
title: "Context Engineering"
parent: "AI (Artificial Intelligence)"
nav_order: 5
---

# Context Engineering

- [What is Context Engineering?](#what-is-context-engineering)
- [Context Engineering References](#context-engineering-references)
- Additional Pages
  - [Agents and Workspace Rules](agents.md)
  - [Skills](skills.md)

## What is Context Engineering?

A conversation with an AI agent involves a chain of prompts and their responses,
which over time fill up an agent's limited attention budget,
otherwise known as the `context window`.
At some point the AI agent runs out of gas and
either cannot proceed or starts hallucinating,
and we might consider moving to a new conversation.
Curating the material passed to an AI agent, including prompts
and shared documents, is known as `context engineering`.

Simply put, we should design our conversations
so that they are sufficiently focused to achieve our goal.
For instance, limit unnecessary background information, and limit the size of documents we
ask the AI agent to ingest.
It is better to ask an AI agent to summarize a document
than to have it read and retained,
and then perhaps save that summary
for use in subsequent conversations.

Another trick is to use `agent skills` located
in one or more `skills` folders, each containing a `SKILL.md` file.
These are reusable packages of knowledge that extend what an agent
can do to handle different aspects of a project.
Typically, these are all housed in a project-level folder like `.agents/skills/`.
See also
[Agents and Workspace Rules](agents.md).

## Context Engineering References

- [Agent Skills for Context Engineering (Murat Cankoylan)](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Antigravity Agent Skills](https://antigravity.google/docs/skills)
- [Antigravity Skills (CodeLabs)](https://codelabs.developers.google.com/getting-started-google-antigravity#8)
- [Claude Skills](https://claude.com/skills)
- [Anthropic Skills](https://github.com/anthropics/skills)
& [Anthropic Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- [AgentSkills.io](https://agentskills.io/home)
- [GitHub Topics: agent-skills](https://github.com/topics/agent-skills)
