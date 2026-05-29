import os

import requests


class OpenRouterError(Exception):
    pass


class FocusCoachBot:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise OpenRouterError("OPENROUTER_API_KEY is required.")
        self.model = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-r1-0528:free")
        self.system_prompt = (
            "You are a direct, structured, no-fluff focus coach chatbot. "
            "Be concise, actionable, and firm. Push the user toward concrete execution steps."
        )

    def reply(self, messages):
        payload = {
            "model": self.model,
            "messages": [{"role": "system", "content": self.system_prompt}, *messages],
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
        if response.status_code != 200:
            raise OpenRouterError(f"OpenRouter request failed: {response.status_code} {response.text}")

        data = response.json()
        try:
            return data["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, TypeError):
            raise OpenRouterError("OpenRouter response was malformed.")
