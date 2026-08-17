# 🏛️ Aegis Dynamics RAG Engine

An advanced Retrieval-Augmented Generation (RAG) pipeline built to test temporal reasoning, table parsing, and "needle-in-a-haystack" retrieval using zero-leakage synthetic corporate data.

Built with the modern **Google GenAI SDK**, **LangChain**, **Qdrant**, and **uv**.

## ✨ Features

- **Synthetic Generative Benchmarking:** Procedurally generates a dense, 50-year corporate archive (1976–2026) using `reportlab`. Ensures absolute zero data leakage since the LLM has never seen this fictional dataset during pre-training.
- **Stateful SSE Streaming:** Utilizes the new Google GenAI `interactions` API for server-side conversation memory and real-time Server-Sent Events (SSE) streaming.
- **Few-Shot Chain-of-Thought (CoT):** Employs advanced prompt engineering to force the model to output a step-by-step reasoning chain before answering, drastically reducing hallucinations.
- **Robust Data Ingestion:** Uses LangChain's `PyPDFLoader` and `RecursiveCharacterTextSplitter` to chunk dense financial tables and corporate policy memos.
- **Lightning Fast Vector Search:** Embeds data using Google's `gemini-embedding-2-preview` and stores it in a local **Qdrant** vector database for high-speed similarity search.

## 🚀 Quick Start

**1. Clone and sync dependencies**
Managed entirely by `uv` for instant dependency resolution.

```bash
uv sync
```
