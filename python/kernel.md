---
title: "Python Default Kernel for Quarto"
parent: "Python Language"
nav_order: 3
---

# Python Default Kernel for Quarto

To set the default Python kernel for Quarto, you have a few options depending on whether you want to set it globally, per-project, or per-document.

### Option 1: Set `QUARTO_PYTHON` globally (Recommended for a system-wide default)

The most reliable way to force Quarto to use a specific Python executable globally is by setting the `QUARTO_PYTHON` environment variable in your shell profile (e.g., `~/.zshrc` or `~/.bashrc`).

1. Find the path to the Python environment you want to use (e.g., your `earth-analytics-python` conda environment):

   ```bash
   conda activate earth-analytics-python
   which python
   ```

2. Add that path to your `~/.zshrc` file:

   ```bash
   export QUARTO_PYTHON="/path/to/your/earth-analytics-python/bin/python"
   ```

3. Restart your terminal or run `source ~/.zshrc`.

### Option 2: Specify the Kernel in the Document's YAML Header

If you want to ensure a specific Quarto document (`.qmd`) always uses the `earth-analytics-python` kernel, you can specify it directly in the YAML front matter of the document.

You'll need the exact Jupyter kernelspec name. You can list your available Jupyter kernels by running:

```bash
jupyter kernelspec list
```

Once you have the kernel name, add it to your `.qmd` file like this:

```yaml
---
title: "My Document"
jupyter:
  kernelspec:
    display_name: earth-analytics-python
    language: python
    name: earth-analytics-python  # Replace with the actual kernel name if different
---
```

### Option 3: Activate the Environment Before Rendering

By default, Quarto will automatically detect and use the Python interpreter that is currently active in your terminal. You can simply activate the environment before running your Quarto commands:

```bash
conda activate earth-analytics-python
quarto render your_document.qmd
```

_[byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools)_  
