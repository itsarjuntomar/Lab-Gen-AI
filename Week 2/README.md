# Week 2 – Provider-Agnostic LLM Client

## Problem

Build one common LLM client that works with either a hosted Gemini API or a local Ollama model. The program uses the same `generate()` method whichever provider is selected.

## Files

- `llm_client.py` – common interface, Gemini provider, Ollama provider, and common client.
- `main.py` – asks which provider to use and sends the prompt.
- `test_client.py` – tests the client with a fake provider.
- `requirements.txt` – required Python packages.
- `.env.example` – template for the Gemini API key.

## Setup

1. Install Ollama from https://ollama.com/download and open it.
2. In PowerShell, download the model:

   ```powershell
   ollama pull llama3.2
   ```

   Wait for the download to finish. Keep Ollama running when using the local provider.

3. Open this folder in VS Code.
4. Activate your existing lab virtual environment if you already have one.
5. Install packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Copy `.env.example` to a file named `.env` and add your Gemini API key:

   ```text
   GEMINI_API_KEY=your_actual_gemini_api_key
   ```

   The key is needed only for Gemini. Never upload your real `.env` file.

## Run the project

```powershell
python main.py
```

Choose `gemini` for the hosted API or `ollama` for the local model, then enter a question.

## Run the test

```powershell
python -m unittest test_client.py
```

The test uses a fake provider and does not need an API key or a running Ollama model.

## How it works

1. `LLMProvider` defines the common `generate(prompt)` method.
2. `GeminiProvider` implements it using the Gemini SDK.
3. `OllamaProvider` implements it by sending an HTTP request to Ollama on your computer.
4. `LLMClient` accepts either provider and forwards the prompt.

This lets the main program switch providers without changing how it requests an answer.

## Note about the Gemini model

The model ID `gemini-3.8-flash` is copied from the Week 2 handout. If your API account does not support that model ID, replace it with a Gemini model ID available to your account.
