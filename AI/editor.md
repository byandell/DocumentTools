---
title: "Editor Controls"
parent: "AI (Artificial Intelligence)"
nav_order: 8
---

## Prompts

- How do I tone down AI in the file editing mode? Suggestions are too often not vetted (hallucinated URLs, text off base). I would rather be more in charge. Tell me how to change it so that it affects all projects.
- Clarify location of `settings.json`.
- Clarify how to modify settings in Antigravity IDE.

## Responses

To tone down AI file editing across all projects and regain full control, you can make changes at two levels: **disabling the passive in-editor autocomplete** (which generates ghost text and fabricated URLs while typing) and **enforcing strict global guardrails** for agent-driven edits.

---

### 1. Disable or Restrict In-Editor Autocomplete (Ghost Text & Supercomplete)

By default, the editor proactively suggests completions and multi-line edits as you type, which frequently hallucinates URLs and inserts unvetted text.

#### Option A: Toggle via the Status Bar (Fastest)

1. In the **bottom-right status bar** of your editor window, click the **Tab / Copilot** status indicator.
2. Toggle **Suggestions in Editor** to **Off**.

#### Option B: Global Settings (`settings.json`)

[For Antigravity IDE on macOS, this file is in
`~/Library/Application Support/Antigravity/User/settings.json`.]
Open your global User Settings (<kbd>⌘</kbd>+<kbd>,</kbd>) or add these directly to your global `settings.json` (accessible via <kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> → *Preferences: Open User Settings (JSON)*):

```json
{
  // Disable automatic ghost-text suggestions while typing
  "editor.inlineSuggest.enabled": false,

  // Tone down speculative multi-line replacements (Supercomplete)
  "antigravity.tab.supercomplete": false
}
```

#### Shift to On-Demand Editing

With passive autocomplete turned off, you remain in charge. When you *do* want AI assistance on a specific snippet:

- Highlight the exact text block and press <kbd>⌘</kbd>+<kbd>I</kbd> (*Instructive Inline Edit*).
- Enter a specific prompt (e.g., *"clean up markdown formatting"* or *"document this function"*). The AI will modify **only** what you highlighted.

---

### 2. Add Guardrails to Your Global Rules (`~/.agents/AGENTS.md`)

Because your global instructions file at `~/.agents/AGENTS.md` automatically applies across **all repositories and workspaces**, you can enforce strict verification rules for any agent-generated file edits.

Add a section like the following to your `~/.agents/AGENTS.md`:

```markdown
## Strict File Editing & Verification Rules

- **Zero Hallucinated URLs**: NEVER invent, infer, or speculate external URLs, DOI links, or documentation URLs. Only use URLs explicitly provided in the prompt, existing in the repository, or empirically verified via tool searches. If a URL is unknown, use a clear placeholder (e.g., `<URL>`) or ask.
- **Conservative & Targeted Edits**: Touch only the specific lines or functions requested. Do not add unsolicited boilerplate, stylistic rewrites, or speculative content beyond the prompt.
- **Ask Before Speculating**: If context, links, or facts are ambiguous or unverified, state the ambiguity and ask for clarification rather than generating plausible-sounding text.
```

---

### 3. Require Explicit Review for Agent Changes

In the Antigravity desktop application / IDE settings (gear icon → **Settings**):

- **Artifact Review Mode**: Set to `asks-for-review` or `strict` so the agent must present proposed file modifications for your review before writing them.
- **Tool Execution Policy**: Ensure review is requested on file-write tools if you want full manual approval before files on disk are touched.

## More Detail on Antigravity Agent UI Settings (step 3)

**Prompt:**
I am confused by the step 3 of `editor.md`. Unclear where to set these.

**Response:**

The confusion in **Step 3** comes from the fact that those settings are in the **Antigravity Agent UI**, not the standard VS Code text editor preferences.

Here is exactly where they live, what they do, and whether you actually need them:

---

### Where to Find Them in the UI

1. Look at the **far left-hand sidebar** of the Antigravity window (the vertical bar with icons for Conversations, Projects, etc.).
2. At the bottom of that sidebar, click **Settings** (the gear icon ⚙️).
3. In the Settings view, look under **Global Settings** (or the **Permissions / Execution** section).
4. You will see dropdowns for:
   - **Artifact Review Mode**: Change this from *Agent Decides* or *Always Proceed* to **`Asks for Review`** (or `Strict`).
   - **Tool Execution Policy** (or *Auto-Execution*): Change this to **`Request Review`** if you want the agent to ask permission before executing actions.

### What These Two Settings Do

- **Artifact Review Mode**: When an agent generates a multi-step plan or structured artifact to edit files, setting this to `Asks for Review` forces the agent to show you a review button/diff and pause for your explicit approval before applying the changes.
- **Tool Execution Policy**: By default, the agent runs safe commands or file-writing tools automatically in a sandbox. Setting this to `Request Review` prompts you with an "Approve / Deny" dialog whenever the agent wants to run a tool.

### Do You Really Need Step 3?

**Probably not, unless you want manual click-to-approve prompts.**

- **Step 1** (`editor.inlineSuggest.enabled: false`) is what stops the annoying ghost text, unprompted suggestions, and hallucinated URLs while you are typing.
- **Step 2** (`~/.agents/AGENTS.md`) is what forces the AI to be conservative, factual, and strictly vetted whenever you ask it to edit or write code.
- **Step 3** is only necessary if you want a formal **"Approve / Reject" confirmation dialog** every time the AI attempts to touch a file during a conversation. If you find extra dialog boxes tedious, you can leave Step 3 alone.

---

**Prompt:**
I see "Global Permissions" and under that "Tool Permissions" and other stuff.

**Response:**
You found the exact right screen! Here is what those settings mean and how to set them depending on how much control you want:

### What’s on that Screen

Under **Global Permissions** → **Tool Permissions**, you will typically see:

1. **File Modifications (`write_file`, `edit_file`) / File Access**:
   - **`Allow in workspace`** *(Default)*: The agent directly edits files within the open project when you ask it to.
   - **`Ask` / `Request Review`**: The agent stops and displays an **"Approve / Deny"** prompt with the file path before it is allowed to write or edit any file.

2. **Terminal / Command Execution**:
   - **`Proceed in sandbox`** *(Default)*: Runs safe read/build/test commands automatically in the local sandbox.
   - **`Request review` / `Strict`**: Asks you before running terminal commands.

3. **Artifact Review Mode**:
   - **`Asks for review`**: Whenever the agent produces a multi-step plan or structured artifact, it displays a **Proceed** button and waits for your OK before continuing.

---

### Which Setting Should You Choose?

- **If you want full veto power over every file touch**:
  Set file modifications / tools to **`Ask`** (or **`Request Review`**). The agent will never touch a file on disk without you clicking "Allow".

- **If you just wanted to stop unwanted, hallucinated text while typing**:
  You can leave these permissions on their **defaults**!
  
Turning off autocomplete in `settings.json` (**Step 1**) and adding the anti-hallucination rules to `~/.agents/AGENTS.md` (**Step 2**) already solved the unvetted text issue without forcing you to click an approval box on every single chat action.
