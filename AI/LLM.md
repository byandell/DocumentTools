---
title: "Large Language Models (LLMs)"
parent: "AI (Artificial Intelligence)"
nav_order: 2
---

# Large Language Models (LLMs)

- [What are large language models (LLMs)?](#what-are-large-language-models-llms)
- [What are AI tokens and embeddings?](#what-are-ai-tokens-and-embeddings)
- [What is a Mixture of Experts (MoE)?](#what-is-a-mixture-of-experts-moe)
- [Open Source LLMs](#open-source-llms)
  - [verde_models.csv](https://github.com/byandell/DocumentTools/blob/main/verde_models.csv) (Verde Model Spec Catalog)
- [Team Science Platforms](team.md)
  - [Geospatial Harmonization with LLMs (CU-ESIIL)](https://cu-esiil.github.io/LLM_lesson_exemplar/)

## What are large language models (LLMs)?

Large language models (LLMs) are basically big transformer networks,
with nodes joined by edges that have weights based on the
strength of connection.
The nodes and edges (connections) for a particular LLM
are fixed, but the weights on the edges can be adjusted
based on data.
The nodes are representations (tokens) of (parts of) words,
or images or audio or other snippets of data.
Often this is described as learning patterns to predict
the next token in a sequence.
At scale, with billions or trillions of nodes,
these LLMs are able to quickly string together useful
responses to prompts to address a surprising range
of tasks.
I am a novice on this, so appeal to others
through links below to find good explanations.

- [IBM](https://www.ibm.com/think/topics/large-language-models)
- [GeeksforGeeks](https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/)
- [AWS](https://aws.amazon.com/what-is/large-language-model/)

## What are AI tokens and embeddings?

LLMs work by encoding text into numerical representations (tokens), then decoding them back into text.
According to
[Google Gemini](https://gemini.google.com)
AI tokens are units of data used in natural language processing models to represent words or phrases.
Tokenization is the method of breaking down text into smaller components (tokens) for easier analysis and understanding.
Encoding converts text into tokens that the AI model can understand.
Tokens can be words or subwords (or images or audio snippets, etc.),
which are converted into numerical representations (embeddings) that capture their meanings.
Token embeddings can carry contextual meanings, allowing models to understand nuances in language.
The model processes (contextualizes) embeddings through multiple layers to understand context and relationships among tokens.

The model generates output tokens based on the processed information, predicting the next token in the sequence.
Decoding reverses the process, transforming tokens back into human-readable form.
AI tokens are used in various applications, including chatbots, translation services, and content generation.
Each model has a maximum token limit, which can affect the amount of text processed at once.
The choice of tokenization method can significantly impact the performance and accuracy of AI models.
The model can be further trained on specific tasks to improve its performance in generating relevant responses.

- [Understanding Encoder-Only and Decoder-Only Transformer Models (Sebastian Raschka)](https://magazine.sebastianraschka.com/p/understanding-encoder-and-decoder)
- [What Are AI Tokens? (NVIDIA)](https://blogs.nvidia.com/blog/ai-tokens-explained/)
- [What Are AI Tokens? How Models Read Text, Images & Code (Aiinsights)](https://aiinsightsnews.net/what-are-tokens-in-ai/)
- [Tokens Explained: The New Currency of Generative AI (Sentisight)](https://www.sentisight.ai/tokens-explained-new-currency-of-generative-ai/)
- [The Invisible Building Blocks of AI: What You Need to Know About Tokenization (Medium: Data Science Collective)](https://medium.com/data-science-collective/the-invisible-building-blocks-of-ai-what-you-need-to-know-about-tokenization-acadd86a63ba)
- [gpt-tokenizer playground](https://gpt-tokenizer.dev/)
- [What is embedding? (IBM)](https://www.ibm.com/think/topics/embedding)
- [What are embeddings in ML? (GeeksforGeeks)](https://www.geeksforgeeks.org/machine-learning/what-are-embeddings-in-machine-learning-2/)
- [What are embeddings in ML? (AWS)](https://aws.amazon.com/what-is/embeddings-in-machine-learning/)
- [What are embeddings? (Cloudflare)](https://www.cloudflare.com/learning/ai/what-are-embeddings/)
- [Embeddings Crash Course (Google)](https://developers.google.com/machine-learning/crash-course/embeddings)
- [Understanding embeddings (Labelbox)](https://labelbox.com/guides/ai-foundations-understanding-embeddings/)

## What is a Mixture of Experts (MoE)?

- [Maarten Grootendorst](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts)
- [GeeksforGeeks](https://www.geeksforgeeks.org/nlp/what-is-mixture-of-experts-moe/)
- [Hugging Face](https://huggingface.co/blog/moe)
- [Siyuan Mu and Sen Lin (2026)](https://arxiv.org/abs/2503.07137)

## Open Source LLMs

The file
[verde_models.csv](https://github.com/byandell/DocumentTools/blob/main/verde_models.csv)
has open-source LLMs
 currently available (10 June 2026) via
[AI Verde](https://chat.cyverse.ai/),
which are cataloged on
[HuggingFace](https://huggingface.co/models).
Information includes:

- Technical Specifications
  - **Developer/Organization:** creator of model (e.g., Zhipu AI, Moonshot AI, Google, Meta). Tracking the lineage and ecosystem of the models.
  - **Context Window:** maximum number of tokens model can process in a single prompt (e.g., 32k, 128k, 1M). Critical factor for use cases involving long documents.
  - **Training Tokens:** number of tokens model was trained on, correlates with overall knowledge and reasoning capabilities.
- Operational & Licensing Details
 **Release Date:** how "state-of-the-art" it is relative to newer releases.
  - **License Type:** open-source (e.g., Apache 2.0, Llama 3 License) or proprietary. Determines how the model can be used commercially.
  - **Quantization Level:** bit-depth (e.g., FP16, INT8, 4-bit). Clarifies the memory requirements.
- Performance & Capabilities
  - **Benchmark Scores (e.g., MMLU, GSM8K):** standardized tests  compare the "intelligence" or reasoning ability of different models.
  - **Primary Modalities:** text-only or multimodal (e.g., can process images, audio, or video).
  - **Supported Languages:** English-centric, bilingual (e.g., English/Chinese), or multilingual.

Sources researched by Gemini:

- [glm-4.7-flash (Ollama)](https://ollama.com/library/glm-4.7-flash)
- [Gemma 3 12B (OpenRouter)](https://openrouter.ai/models/google/gemma-3-12b)
- [Phi-4 (NVIDIA)](https://catalog.ngc.nvidia.com/models/nvidia/phi-4/overview) ⚠️
- [[2505.09388] Qwen3 Technical Report (arXiv)](https://arxiv.org/abs/2505.09388)
- [MiniMax M2 (OpenRouter)](https://openrouter.ai/models/minimax/minimax-m2)
- [gpt-oss-120b (OpenRouter)](https://openrouter.ai/models/gpt-oss-120b)
