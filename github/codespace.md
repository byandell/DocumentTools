---
title: "CodeSpaces within GitHub"
parent: "Organize Projects with GitHub"
nav_order: 2
---

# CodeSpaces within GitHub

GitHub repos can initiate a GitHub Codespace, which is a development environment that runs in the cloud. It is based on Docker and uses Visual Studio Code as the editor.
These used to be free but now require payment.
I have used these in the context of activities with
[Environmental Data Science Innovation & Impact Lab (ESIIL)](https://esiil.org).

**Always stop a codespace when done to save resources!**

- [What is `devcontainer.json`](#what-is-devcontainerjson)
- Addition Pages
  - [GitHub Codespaces overview](https://docs.github.com/en/codespaces/overview),
[QuickStart](https://docs.github.com/en/codespaces/getting-started/quickstart) &
[Documentation](https://docs.github.com/en/codespaces)
  - [GitHub Codespaces (Visual Studio Code)](https://code.visualstudio.com/docs/remote/codespaces)
  - [Stopping and starting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#stopping-a-codespace)
  - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

## What is `devcontainer.json`?

The `devcontainer.json` file is a configuration file that defines a structured, reproducible development environment inside a Docker container. It serves as the primary configuration file for the Development Container Specification. [1, 2, 3, 4]  
Instead of configuring your local operating system, this file tells compatible tools exactly how to spin up a dedicated container equipped with all the specific tools, libraries, runtimes, and editor extensions required to work on a codebase. This entirely eliminates the classic "it works on my machine" problem across development teams. [1, 5, 6, 7]  

### File Location

The file is checked directly into your project's version control (like Git). Supporting tools look for it in one of two places:

- At the root of your project as  
- Inside a dedicated folder as  (Most common) [1, 8]  

### What You Can Configure

The file is formatted as JSON with Comments (JSONC). It allows you to automate the setup of several distinct layers of your workspace:

- The Environment Layer: You can point directly to an existing Docker image, reference a local , or leverage a  file to orchestrate multi-container setups.
- The Tooling Layer ("Features"): You can easily pull in pre-packaged, standardized tools (like the Azure CLI, Go, or Docker-in-Docker) without manually scripting their installation.
- The Editor Layer ("Customizations"): You can force the editor to automatically install specific extensions (e.g., Python linters or Prettier) and inject default workspace settings directly into the container.
- The Network & Automation Layer: You can automate port forwarding so web servers running inside the container are accessible on your host machine, and trigger  scripts to automate tasks like running  or  automatically. [1, 14, 17]  

### Basic Code Example

Here is the `devcontainer.json` file used for the
[ESIIL Stars](https://esiil.org/esiil-stars) program: [14, 15, 17]  

```
{
    "name": "ESIIL Stars Container",
    "image": "registry.hub.docker.com/earthlab/first-map:latest",
    "workspaceFolder": "/workspaces",
    "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter",
        // Use black to format code (right click)
        "ms-python.black-formatter",
    ],
    "settings": {
        // Display line length guides
        "editor.rulers": [72, 79],
        // Turn off annoying overzealous autocomplete
        "editor.acceptSuggestionOnEnter": "off",
        // Formatting tools
        "editor.defaultFormatter": "ms-python.black-formatter",
        "python.formatting.blackArgs": [
            "--line-length=79",
            "--experimental-string-processing"
        ],        
        // Set the default python to the conda install
        "python.defaultInterpreterPath": "/opt/conda/bin/python"
    },
}
```

### Supporting Tools

While originally created by Microsoft for Visual Studio Code, the format is an open standard utilized by various platforms across the industry:

- IDEs & Editors:  VS Code Dev Containers extension , GitHub Codespaces, and JetBrains IDEs.
- Local Workspace Managers: Open-source tools like DevPod and Coder.
- Automation: The Dev Container CLI which allows you to build, test, and validate these environments within Continuous Integration (CI/CD) pipelines. [3, 7, 8, 18, 23, 24]  

### References cited

[1] [Create a dev container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
[2] [Specification](https://containers.dev/implementors/spec/)
[3] [Overview](https://containers.dev/overview.html)
[4] [Windows](https://learn.microsoft.com/en-us/windows/dev-environment/docker/dev-containers)
[5] [devcontainer.json](https://www.ssp.sh/brain/devcontainers-devcontainer.json/)
[6] [marvelous-mlops](https://medium.com/marvelous-mlops/how-to-start-with-dev-containers-1e92bf0e0f78)
[7] [coder.com](https://coder.com/docs/admin/integrations/devcontainers)
[8] [GitHub](https://docs.github.com/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers)
[9] [Docker](https://www.docker.com/blog/streamlining-local-development-with-dev-containers-and-testcontainers-cloud/)
[10] [JSON reference](https://containers.dev/implementors/json_reference/)
[11] [Features](https://containers.dev/implementors/features/)
[12] [Features blog](https://code.visualstudio.com/blogs/2022/09/15/dev-container-features)
[13] [YouTube](https://www.youtube.com/watch?v=iCopdmuabBM)
[14] [Tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)
[15] [Supporting](https://containers.dev/supporting)
[16] [dxdissected](https://dxdissected.com/p/the-dx-evolution-from-local-setup-to-the-cloud)
[17] [n2x.io](https://n2x.io/blog/what-are-devcontainers)
[18] [Visual Studio Code](https://code.visualstudio.com/docs/devcontainers/containers)
[19] [devclass](https://www.devclass.com/containers/2022/06/20/microsofts-devcontainerjson-just-for-vs-code-or-an-evolving-standard/1618537)
[20] [devpod.sh](https://devpod.sh/docs/developing-in-workspaces/devcontainer-json)
[21] [marcogerber.ch](https://marcogerber.ch/dev-containers-develop-inside-a-container/)
[22] [vscode-remote-release](https://github.com/microsoft/vscode-remote-release/issues/2067)
[23] [devpod.sh](https://devpod.sh/docs/developing-in-workspaces/devcontainer-json)
[24] [containers.dev](https://containers.dev/implementors/reference/)
