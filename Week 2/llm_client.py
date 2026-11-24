from abc import ABC, abstractmethod

from google import genai
import requests


class LLMProvider(ABC):
    """Common interface for all LLM providers."""

    @abstractmethod
    def generate(self, prompt):
        pass


class GeminiProvider(LLMProvider):
    """Hosted Gemini API provider."""

    def __init__(self, api_key, model="gemini-3.8-flash"):
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text


class OllamaProvider(LLMProvider):
    """Local Ollama provider."""

    def __init__(self, model="llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["response"]


class LLMClient:
    """A single client that can use any provider implementing the interface."""

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)
