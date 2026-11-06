# LangGraph Chatbot

A conversational chatbot with a Streamlit chat interface. It uses LangGraph to manage the conversation flow and runs the Qwen 2.5 model locally through Ollama.

## Features

- Chat interface built with Streamlit
- Conversation flow managed with LangGraph
- Local language model powered by Ollama and `qwen2.5`

## Requirements

- Python 3.10 or later
- [Ollama](https://ollama.com/) installed and running

## Setup

1. Download the model:

   ```powershell
   ollama pull qwen2.5:latest
   ```

2. From the project directory, create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the Python packages:

   ```powershell
   python -m pip install streamlit langgraph langchain-ollama
   ```

## Run

Start the app from the project directory:

```powershell
streamlit run streamlit_frontend.py
```

Streamlit will open the chatbot in your browser. Make sure Ollama is running and the `qwen2.5:latest` model is available.

## Project files

- `streamlit_frontend.py` — Streamlit interface and display of chat history
- `langgraph_backend.py` — LangGraph workflow and Ollama model configuration

The conversation checkpoint is stored in memory and is cleared when the backend process restarts.
