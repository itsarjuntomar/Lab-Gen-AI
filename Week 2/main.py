import os

from dotenv import load_dotenv

from llm_client import GeminiProvider, OllamaProvider, LLMClient


def main():
    load_dotenv(override=True)

    provider_name = input("Choose provider (gemini/ollama): ").strip().lower()

    if provider_name == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Gemini API key not found. Add it to your .env file.")
        provider = GeminiProvider(api_key)

    elif provider_name == "ollama":
        provider = OllamaProvider("llama3.2")

    else:
        raise ValueError("Invalid provider. Please choose gemini or ollama.")

    client = LLMClient(provider)
    prompt = input("Enter your question: ")
    answer = client.generate(prompt)

    print("\nLLM Response:")
    print(answer)


if __name__ == "__main__":
    main()
