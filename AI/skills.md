---
title: "Create and Use AI Skills"
parent: "AI (Artificial Intelligence)"
nav_order: 7
---

# Create and Use AI Skills

A skill is an ability and/or set of knowledge.
AI agents can create or use skills to complete tasks.
Here are example prompts to create an AI skill
and determine where its files are stored.

**Prompts:**

- Create a skill as described in project rationale.
- Where do I find the products for this skill?

An example skill and process to create it is in
[Heureka/Projects/Skill4AttieData](https://github.com/AttieLab-Systems-Genetics/Heureka/tree/main/Projects/Skill4AttieData).

## Resources

- [Understanding Skills, Tools, and Apps](#understanding-skills-tools-and-apps)
- [Comparison of Agent Skills and AGENTS.md](#comparison-of-agent-skills-and-agentsmd)
  - [Agent Skills / SKILL.md (Actionable Capabilities)](#agent-skills--skillmd-actionable-capabilities)
  - [Summary of Differences](#summary-of-differences)
- [Gemini User-Level Skills](#gemini-user-level-skills)
- Related Links
  - [Skills for Scientific Discovery](https://heurekaskills.com/)
  - [Inside scientific benchmarks - Heureka Labs](https://www.heurekalabs.co/blog/inside-scientific-benchmarks/)
  - [lab-bench — Heureka Skills (harness info?)](https://heurekaskills.com/lab-bench/)
  - [Skills vs. Tools](https://thisvsthat.io/skills-vs-tools)
  - [Skill vs. Tool, MCP vs. API](https://taoproductleader.substack.com/p/skill-vs-tool-vs-mcp-vs-api)

## Understanding Skills, Tools, and Apps

Skills refer to the abilities and knowledge individuals possess, while tools are physical or software aids that help complete tasks. Apps, on the other hand, are specific software applications designed to perform particular functions, often utilizing both skills and tools to enhance user experience and productivity.
Each of these concepts plays a unique role in productivity and functionality.

- Skills — Skills encompass abilities like problem-solving and communication, which are essential for effective task execution.
- Tools — Tools are tangible or digital instruments, such as software programs or physical devices, that assist in completing tasks efficiently.
- Apps — Apps are specialized software applications designed for specific tasks, often integrating various tools and requiring user skills to operate effectively.
- Interrelation — Skills enhance the effective use of tools and apps, while tools and apps can facilitate the development of new skills.

### Skills, Tools, and Apps Examples

- Skills — Critical thinking, communication, and problem-solving abilities that enable effective task completion.
- Tools — Software programs like spreadsheet applications or project management tools that facilitate task execution.
- Apps — Mobile applications such as Slack or Asana, designed for specific tasks and integrating various tools and skills.

---

## Comparison of Agent Skills and AGENTS.md

Based on the technical paradigms for AI coding assistants (such as Claude Code, GitHub Copilot, Cursor, and Codex), **Agent Skills** (or `SKILL.md`) and
[**`AGENTS.md`**](agents.md)
are two complementary standards used to provide context and capabilities to AI agents.

A comparative breakdown highlights their distinct roles, structures, and intended use cases:

| Feature | `AGENTS.md` | Agent Skills (`SKILL.md`) |
| --- | --- | --- |
| **Primary Purpose** | Defines **repository-specific context** (tech stack, coding standards, project layout, architecture rules). | Packages **procedural knowledge** or actionable automation capabilities (how to deploy, audit, generate code, or test). |
| **Scope** | Bound to a specific codebase/repository (Static local context). | Portable across different repositories and platforms (Reusable "recipes"). |
| **Core Components** | A single Markdown file matching the [agents.md specification](https://agents.md). | A folder structure containing `SKILL.md` (frontmatter + rules) and optional automation scripts (Bash, Python, Node). |
| **Trigger Mechanism** | Loaded automatically when an agent begins working inside that repository. | Activated dynamically on-demand when the agent recognizes a relevant trigger phrase or task. |

---

### Agent Skills / `SKILL.md` (Actionable Capabilities)

Think of Agent Skills as a **toolbox or an app store** for the AI agent. Instead of general project guidelines, a skill teaches the agent how to execute a complex, multi-step workflow.

- **Target Audience:** The AI agent across _any_ project that requires this specific ability.
- **Content Focus:**
  - Strict step-by-step procedural workflows (e.g., `/spec`, `/plan`, `/review`).
  - Structural anti-rationalization tables (rules preventing the agent from cutting corners, like skipping unit tests).
  - Executable automation helpers (scripts located in a nested `scripts/` directory).
- **Structure Requirements:** Requires structured YAML frontmatter at the top:

```markdown
---
name: vercel-deploy
description: Deploy my web app to Vercel production.
---
# Deploy Skill
...

```

Comments gleaned from Gemini browser summary:

- Agent skills typically refer to the capabilities or functions an AI can perform.
- The context window includes the information the AI can reference during a conversation.
- Skills may influence the AI's responses but are not directly counted in the context window.
- The context window primarily consists of user inputs and previous exchanges.
- Skills can enhance the AI's ability to interpret and respond to context effectively.
- Understanding the distinction helps clarify how AI processes information during interactions.

### Summary of Differences

While **`AGENTS.md`** sets the **boundaries and context** of _where_ the agent is working, **Agent Skills** extend the **functional capability** of _what_ the agent can actually execute. For example, your `AGENTS.md` might dictate that you use Vitest for unit testing, but you would activate an `agent-skill` to execute a structured test-driven development workflow using those tools.

---

## Gemini User-Level Skills

**Prompts:**

- Where is `SKILL.md` that you used for this last response?
- You also used `ide.md`, `app.md`, `rules.md` and `cli.md`. Do I need to know about them?

### Built-in Skills

The previous response referenced two built-in skills and their documentation
located under `~/.gemini/antigravity/builtin/skills/`

1. **Antigravity Guide**:
   - `antigravity_guide/SKILL.md`
   - Accompanying editor reference
     - `antigravity_guide/references/ide.md`
     - _covers editor modalities: Tab Autocomplete vs. Inline Command <kbd>⌘</kbd>+<kbd>I</kbd>_

2. **Antigravity Customizations**:
   - `agy-customizations/SKILL.md`
   - Accompanying rules reference
     - `agy-customizations/docs/rules.md`
     - _covers discovery and hierarchy of global `AGENTS.md` rules_

### Other System Markdowns

**No, you don’t need to read, edit, or manage these files.**

They are read-only reference manuals bundled internally inside Antigravity's built-in skills directory (`~/.gemini/antigravity/builtin/skills/`).
The agent consults them as "user manuals" to look up how the platform works.
Here is a quick summary of what each covers
and whether the underlying concept matters to you.

| Reference File | What It Covers | Do You Need to Care? |
| :--- | :--- | :--- |
| `agy-customizations/` `docs/rules.md` | How the system discovers and prioritizes `AGENTS.md` and `GEMINI.md` files. | **Useful concept only**: You don't need to read this file, but knowing that your personal `~/.agents/AGENTS.md` automatically governs all projects lets you set system-wide preferences. |
| `antigravity_guide/` `references/ide.md` | The editor's three AI modes: Tab autocomplete, Inline Command (<kbd>⌘</kbd>+<kbd>I</kbd>), and Sidebar Chat. | **Optional**: Helpful if you want to know what editor shortcuts exist. |
| `antigravity_guide/` `references/app.md` | The desktop app UI (sidebar, chat canvas, permissions, and settings). | **No**: Just platform documentation. |
| `antigravity_guide/` `references/cli.md` | Terminal CLI flags and slash commands for `agy`. | **No** (unless you work from the command-line terminal using the `agy` CLI). |

In short: the only file you ever need to create or edit is your own `~/.agents/AGENTS.md` or local `.agents/` folders in your repositories. The `.md` files mentioned above are just internal references.
