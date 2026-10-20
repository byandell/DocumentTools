---
title: "Recovering Antigravity 1.x Conversations"
parent: "AI Environments"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 1
---

# Recovering Antigravity 1.x Conversations

`Antigravity IDE 2.0` is an improvement over `Antigravity 1.x`,
but it lost contact with any previously created conversations.
Google did not provide an easy path to migrate conversations,
leaving that to the frustrated community.
Below is my conversation with Antigravity IDE 2.0 about recovering those conversations.

**Table of Contents**

- [Relevant links](#relevant-links)
- [Why do they not appear on list of past conversations?](#why-do-they-not-appear-on-list-of-past-conversations)
- [Recovery using CLI Tool](#recovery-using-cli-tool)
- [Result of Recovery](#result-of-recovery)
- [Other Methods to Recover Some Conversations](#other-methods-to-recover-some-conversations)

_[byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools)_  

**Prompt:**
Use [Method 1: Antigravity History CLI Tool](#method-1-antigravity-history-cli-tool)
to recover my lost conversations.

## Relevant links

- [Antigravity 2.0 Explained (OFOX)](https://ofox.ai/blog/google-antigravity-2-explained-gemini-desktop-agent-platform-2026/)
- [Antigravity 2.0 Complete Guide (AIMadeTools)](https://www.aimadetools.com/blog/antigravity-2-complete-guide/)
- [Google Antigravity 2.0 Explained (AgentUpdate)](https://www.agentupdate.ai/blog/google-antigravity-2-0-explained/)
- [Google Antigravity 1.0 to 2.0/IDE Quick Migration Guide (Dev)](https://dev.to/gde/google-antigravity-10-to-20ide-quick-migration-guide-35p5)
- [Chat History Recovery Guide](https://discuss.ai.google.dev/t/chat-history-recovery-guide-recovered-26-missing-sessions-using-pb-injection/136496)
([README](https://github.com/keisksw/antigravity-chat-recovery))

## Why do they not appear on list of past conversations?

The reason your past conversations do not appear in your Antigravity IDE sidebar is due to a known indexing issue that occurs during system updates (like the transition from Antigravity 1.x to 2.x):

1. **How the Sidebar Works:** The IDE sidebar displays past conversations by reading an index file or local metadata store (like `state.vscdb` or a `trajectorySummaries` index).
2. **Index Reset/Desync:** When the IDE updates, this index file is frequently reset, cleared, or changes format, making the IDE "forget" that these past sessions exist.
3. **Data is Safe:** Although the index was cleared, your actual chat logs—stored as protobuf (`.pb`) files in `~/.gemini/antigravity-ide/conversations`—remain entirely intact on your hard drive. They are just no longer referenced by the IDE's active index.

### How to Recover Them

Use the community guides and tools developed
(see links at top of this page) to solve this:

- **Manual ".pb Injection":** A workaround where you create a new "dummy" chat session in the IDE (which registers a new entry in the index), then rename your old `.pb` file to replace the dummy file. When the IDE restarts, it loads the old content under the new index registration.
- **Automated Scripts:** Tools like the `Resurrect` toolkit or the community [antigravity-chat-recovery](https://github.com/keisksw/antigravity-chat-recovery) script automate this injection/re-indexing process.

_Note: If you decide to try recovering them, make sure to back up your entire `~/.gemini/antigravity-ide/conversations` folder first to prevent accidental data loss._

## Why can't antigravity fix this itself?

There are two parts to why this isn't fixed automatically—one regarding me (your AI agent) and the other regarding the Antigravity IDE application itself:

### 1. Why I (the AI Agent) cannot fix it

- **System Sandboxing and Security Rules:** To protect your active sessions and data integrity, my environment is strictly sandboxed. I am explicitly denied write access to your conversation files (`write_file(~/.gemini/antigravity-ide/conversations) : denied`). Because of this, I cannot rename files or edit the internal database index on your behalf.

### 2. Why the Antigravity application itself doesn't fix it

- **Architectural Rebuild (1.0 vs 2.0):** The transition to Antigravity 2.0 was a complete rewrite from a VS Code-forked IDE (which stored local state in VS Code's standard configuration directories) to a standalone desktop application. Because they are separate applications, 2.0 does not automatically scan or share 1.0's configurations.
- **Database Format Migration:** Antigravity 1.0 stored chat sessions as individual Protocol Buffer (`.pb`) files. Antigravity 2.0 migrated history indexing to a SQLite database (`.db`). The development team did not build an automatic legacy migration tool to parse and ingest old `.pb` histories into the new SQLite database schema.

## Recovery using CLI Tool

### Possible Methods

- **Method 1:** Use the `antigravity-history` CLI Tool (Recommended).
- **Method 2:** Manual ".pb Injection" (For Specific Chats)
if you only need to restore one or two specific conversations directly into the IDE interface.
- **Method 3:** Quick Python Text Extractor Script
if you do not want to install external CLI packages and simply want to extract raw text prompts/replies.

See [Other Methods to Recover Some Conversations](#other-methods-to-recover-some-conversations) for more information
on methods 2 and 3. Below is Method 1.

### Method 1: Antigravity History CLI Tool

The developer community has created a CLI tool called `antigravity-history` specifically to extract and recover these unindexed conversations.
See [antigravity-chat-recovery](https://github.com/keisksw/antigravity-chat-recovery).

#### Step 1: Install the tool

Open your terminal and install the tool via `pip`:

```bash
pip install antigravity-history
```

#### Step 2: Export your history to Markdown

You can convert all your old `.pb` files into readable Markdown documents using the `export` command.

1. Create a target directory for your exports (e.g., `~/Desktop/Antigravity_Backup`):

   ```bash
   mkdir -p ~/Desktop/Antigravity_Backup
   ```

2. Run the tool to export the files:

   ```bash
   aghistory export --output ~/Desktop/Antigravity_Backup
   ```

This will generate standard `.md` files for every past conversation, preserving your prompts, the AI's responses, and code blocks.

#### Step 3: Re-index into the IDE

To attempt restoring them directly into the IDE sidebar:

```bash
aghistory recover
```

_(Note: Close the Antigravity IDE application before running this command.)_

## Result of Recovery

Searched for "~/.gemini/antigravity"
Edited cli.py
Ran command: `aghistory export --output ~/Desktop/Antigravity_Backup`

I am waiting for the `aghistory export` process to complete and write the Markdown/JSON backups to your Desktop.

Ran command: `aghistory recover`

I am waiting for the `aghistory recover` process to complete indexing the 81 conversations in your active IDE session.

Ran command: `aghistory list -n 10`

I am waiting for `aghistory list` to display the active conversations list.

All **81 conversations** (totaling **4,392 messages**) have been successfully backed up and fully re-indexed into your Antigravity IDE!

### Summary of what was done

1. **Fixed Library Bugs:**
   - Patched a `ValueError` in the `antigravity-history` CLI tool where it expected 2 values instead of 3 when calling `get_all_trajectories_merged`.
   - Modified the hardcoded conversation path in the library (`cli.py`) to fallback to the correct `-ide` directory: `/Users/brianyandell/.gemini/antigravity-ide/conversations`.
2. **Exported Backups:**
   - Exported all 81 conversations into readable Markdown and JSON formats.
   - Saved them to a new backup folder on your Desktop at `/Users/brianyandell/Desktop/Antigravity_Backup`.
3. **Re-Indexed in IDE:**
   - Triggered the recovery/activation process with the local LanguageServer API.
   - All 81 sessions are now fully registered in your IDE session, complete with their original titles, step counts, and modification timestamps (e.g. _"Reviewing Environmental Data Science Papers"_, _"Identifying Landmapy Spatial Dependencies"_, _"Analyzing Hsp90 GTT Data"_).

Your chat history sidebar in the IDE should now display all these restored conversations!

## Other Methods to Recover Some Conversations

These were not used to recover my conversations because I used the `antigravity-history` CLI tool above (Method 1) to do it.

## Method 2: Manual ".pb Injection" (For Specific Chats)

If you only need to restore one or two specific conversations directly into the IDE interface, you can do this manually:

1. **Back up your files:**

   ```bash
   cp -r ~/.gemini/antigravity-ide/conversations ~/Desktop/conversations_backup
   ```

2. **Open Antigravity IDE** and create a **new, blank chat**.
3. **Close Antigravity IDE** completely.
4. Open the conversations directory in your terminal:

   ```bash
   cd ~/.gemini/antigravity-ide/conversations
   ```

5. List the files sorted by modification time to find the ID of the new dummy chat you just created:

   ```bash
   ls -lt
   ```

   _Identify the latest `.pb` file (e.g., `NEW_DUMMY_ID.pb`)._
6. Copy that filename, delete the new `.pb` file, and rename the **old** `.pb` file you want to recover to match that name exactly:

   ```bash
   mv OLD_CONVERSATION_ID.pb NEW_DUMMY_ID.pb
   ```

7. **Relaunch Antigravity IDE.** The sidebar will load the dummy chat name, but clicking it will display your recovered past conversation history.

---

## Method 3: Quick Python Text Extractor Script

If you do not want to install external CLI packages and simply want to extract raw text prompts/replies from the binary `.pb` files, you can use the script below.

Save the code below as `extract_history.py` in your terminal and run it:

```python
import os
import re

CONV_DIR = os.path.expanduser("~/.gemini/antigravity-ide/conversations")
OUTPUT_DIR = os.path.expanduser("~/Desktop/Antigravity_Extracted")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Regex to pull readable ASCII/UTF-8 sentences from binary protocol buffers
# Matches sequences of readable printable characters
text_pattern = re.compile(rb'[\x20-\x7E\x0A\x0D\xC0-\xFF]{4,}')

print(f"Scanning {CONV_DIR}...")

for filename in os.listdir(CONV_DIR):
    if filename.endswith(".pb"):
        filepath = os.path.join(CONV_DIR, filename)
        
        with open(filepath, 'rb') as f:
            data = f.read()
            
        # Extract readable string chunks
        chunks = text_pattern.findall(data)
        decoded_chunks = []
        for chunk in chunks:
            try:
                text = chunk.decode('utf-8', errors='ignore').strip()
                # Filter out system tags, metadata tokens, and very short noise
                if len(text) > 8 and not text.startswith(('antigravity', 'system', 'default_api')):
                    decoded_chunks.append(text)
            except:
                pass
                
        if decoded_chunks:
            output_file = os.path.join(OUTPUT_DIR, f"{filename[:-3]}.md")
            with open(output_file, 'w', encoding='utf-8') as out:
                out.write(f"# Recovered Chat ({filename[:-3]})\n\n")
                for chunk in decoded_chunks:
                    out.write(f"{chunk}\n\n---\n\n")
            print(f"Extracted {filename} -> {os.path.basename(output_file)}")

print(f"\nDone! Extracted conversations saved to {OUTPUT_DIR}")
```
