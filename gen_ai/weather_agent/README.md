# 🌤️ Autonomous Weather Agent

A lightweight, conversational AI assistant that fetches live weather data using Gemini's automatic function calling and strictly enforces structured JSON outputs.

Built with the modern `google-genai` SDK, Pydantic, and `uv`.

## ✨ Features

- **Autonomous Tool Calling:** Automatically intercepts Gemini's requests to run local Python functions (via `wttr.in`) before answering the user.
- **Strict Structured Outputs:** Uses Pydantic (`ResponseSchema`) to mathematically constrain the AI's output into a predictable, type-safe format.
- **Multi-Turn Memory:** Utilizes the `chats` API to remember context across continuous conversations.
- **Lightning Fast Setup:** Managed entirely through `uv` for instant dependency resolution and execution.

## 🚀 Quick Start

**1. Clone and sync dependencies**

```bash
uv sync
```
