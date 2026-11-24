# Week 1 – First LLM API Call

A beginner-friendly Python project that sends a prompt to an OpenAI model using the OpenAI Responses API and prints the generated response.

## Project files

- `main.py` – loads the API key, sends a prompt, and prints the response.
- `.env.example` – template for the required environment variable.
- `.gitignore` – keeps `.env`, virtual environments, and cache files out of Git.
- `requirements.txt` – lists the Python packages used.

## Setup

1. Open this folder in Visual Studio Code.
2. Activate the existing virtual environment for your lab. The lab guide says to reuse the existing `.venv` in the parent `LAB_Experiments` folder; do not create another environment if that one is already available.
3. Install the packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create a file named `.env` in the same folder as `main.py`.
5. Add your own OpenAI API key to `.env`:

   ```text
   OPENAI_API_KEY=your_actual_openai_api_key
   ```

   Do not share this key or commit the `.env` file.

6. Run the program:

   ```powershell
   python main.py
   ```

The terminal should show `LLM Response:` followed by the model's answer.

## Notes

- ChatGPT access and OpenAI API access are separate. API usage may require billing or available credits.
- The example uses the `gpt-5.5` model ID from the lab guide. If your API project cannot access it, replace it with a model available to your API account.
- Never commit your real API key. If it is accidentally published, revoke it and create a replacement.
