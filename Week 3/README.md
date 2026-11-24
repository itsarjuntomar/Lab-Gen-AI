# Week 3 – LLM Monitoring with MongoDB

This project extends the Week 2 provider-agnostic LLM client. It supports Gemini and Ollama and stores request usage, latency, estimated cost, and final success/failure details in MongoDB.

## Project files

- `main.py` – selects Gemini or Ollama and runs a prompt.
- `llm_client.py` – provider implementations, token usage, latency, cost estimation, timeout and retry handling.
- `usage_logger.py` – MongoDB connection and usage-record storage.
- `test_client.py` – unit test using fake provider and logger (no API or database needed).
- `requirements.txt` – Python dependencies.
- `.env.example` – safe template for local secrets.
- `.gitignore` – excludes `.env`, virtual environments, and cache files.

## 1. Create your local environment settings

Copy `.env.example` to `.env` in this folder and fill in your own values:

```text
GEMINI_API_KEY=your_actual_gemini_api_key
MONGODB_URI=your_mongodb_atlas_connection_string
GEMINI_INPUT_PRICE_PER_MILLION=0
GEMINI_OUTPUT_PRICE_PER_MILLION=0
```

Use your own Gemini API key and MongoDB Atlas connection string. Never commit `.env` or share these values.

The two price values are configurable USD rates per one million input/output tokens. Set them to the current rates for the Gemini model you use. They default to zero until configured. Ollama is local, so the example records zero hosted API charge and does not estimate electricity or hardware costs.

## 2. MongoDB Atlas setup

1. Create or sign in to MongoDB Atlas.
2. Create a free M0 cluster if available.
3. Create a database user and save its username/password securely.
4. In Network Access, add your current computer IP address. Avoid `0.0.0.0/0` for this exercise.
5. Open your cluster's Connect option, choose Drivers and Python, and copy the connection string.
6. Put the connection string in your local `.env` as `MONGODB_URI=...`.

The application creates database `llm_monitoring` and collection `api_usage` when it logs the first request.

## 3. Install dependencies

Activate your existing lab virtual environment, then run:

```powershell
python -m pip install -r requirements.txt
```

## 4. Prepare Ollama (only if using the local provider)

Install Ollama, then run:

```powershell
ollama pull llama3.2
ollama run llama3.2
```

Keep Ollama running while using the Ollama option.

## 5. Run the test

```powershell
python -m unittest test_client.py
```

This test uses a fake provider and fake logger. It does not need Gemini, Ollama, or MongoDB.

## 6. Run the application

```powershell
python main.py
```

Choose `gemini` or `ollama`, then enter a prompt. The application prints the answer and usage metrics.

## Monitoring details

- Gemini usage comes from the response's prompt and candidate token counts.
- Ollama usage comes from `prompt_eval_count` and `eval_count`.
- Latency is measured in milliseconds and includes retry time.
- Gemini estimated cost uses configurable per-million-token rates.
- Ollama hosted API cost is recorded as zero; local electricity/hardware costs are not included.
- Successful requests and final failed requests are logged. A failed request has unknown token counts and cost.
- Selected temporary errors are retried up to three total attempts, with 1-second and 2-second waits.
- Gemini HTTP timeout is 60 seconds. Ollama uses connect/read timeouts of 5/60 seconds. MongoDB uses connection/socket timeouts and up to three write attempts.

## Important

The Gemini SDK may have its own retry behavior. Avoid unintentionally stacking retry policies in production. Verify current Gemini model pricing and availability for your API account.
