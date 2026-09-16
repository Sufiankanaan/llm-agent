# 🤖 AI Agent with Tool-Calling

A local AI agent that decides when to use tools to answer questions. Instead of just generating text, it can call functions — like a calculator or a clock — execute them, and use the results to form accurate answers.

Built entirely with **local, free tools** — no API keys, no token costs.

---

## ✨ What It Does

The agent reads a user's question and **decides on its own** whether it needs a tool:
- **"What is 4728 times 391?"** → calls the calculator tool, returns the exact result.
- **"What time is it?"** → calls the time tool.
- **"Hello, how are you?"** → answers directly, no tool needed.

The model is the *brain* that decides; the code is the *hand* that executes.

---

## 🛠️ Tech Stack

- **Ollama** — runs the model locally, fully offline
- **llama3.2** — the model that decides which tool to use
- **Python**

---

## 🏗️ How It Works

```
User question
   ↓
Model receives the question + available tools
   ↓
Does the model request a tool?
   ├─ Yes → execute the tool → return result to model → final answer
   └─ No  → answer directly
```

This is the core **tool-calling loop**: the model chooses a tool and extracts its
arguments from natural language, the code runs it, and the result is fed back so
the model can compose a natural answer.

---

## 🔧 Available Tools

- **calculator** — performs add, subtract, multiply, divide (with divide-by-zero protection)
- **get_current_time** — returns the current date and time

---

## 🛡️ Production Features

- **Error handling** — the agent uses try/except so a failing tool never crashes it; unknown tools return a clean error message.
- **Logging** — every decision is traced (`[AGENT] Tool chosen: ...`, `[AGENT] Result: ...`) for debugging and transparency.
- **Interactive loop** — accepts continuous questions until the user types "exit".

---

## 🚀 Getting Started

### Prerequisites
- [Ollama](https://ollama.com) installed and running
- Python 3.10+

### Setup

```bash
ollama pull llama3.2
pip install -r requirements.txt
python agent.py
```

### Usage
```
Ask me anything (calc or chat, "exit" to quit): what is 4728 times 391
[AGENT] Tool chosen: calculator
[AGENT] Arguments: {'operation': 'multiply', 'x': '4728', 'y': '391'}
[AGENT] Result: 1848648.0
The result of multiplying 4728 by 391 is 1848648.
```

---

## 🔑 Key Concepts Demonstrated

- **Tool-calling (function-calling)** — letting an LLM invoke functions
- **Tool schemas** — describing tools to the model so it can choose them
- **Message roles** — user / assistant / tool in a multi-step conversation
- **Error handling** — building a robust agent that doesn't crash
- **Logging** — tracing an agent's decisions

---

## 📁 Project Structure

```
├── agent.py          # The agent: tools, tool-calling loop, error handling, logging
├── requirements.txt  # Dependencies
└── README.md
```

---

## 🔮 Possible Improvements

- Add more tools (web search, file operations)
- Support multi-step tasks (chaining several tool calls)
- Integrate MCP (Model Context Protocol) for standardized tool connections
- Add a web interface

---

## 👤 Author
**Sufian Kanaan** — [LinkedIn](https://www.linkedin.com/in/sufian-kanaan/)
