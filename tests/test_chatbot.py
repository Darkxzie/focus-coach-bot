import pytest

from chatbot import FocusCoachBot, OpenRouterError


class DummyResponse:
    def __init__(self, status_code=200, json_data=None, text=""):
        self.status_code = status_code
        self._json_data = json_data or {}
        self.text = text

    def json(self):
        return self._json_data


def test_missing_api_key_raises_clear_error(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)

    with pytest.raises(OpenRouterError, match="OPENROUTER_API_KEY"):
        FocusCoachBot()


def test_request_includes_focus_system_prompt(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    captured = {}

    def fake_post(url, headers=None, json=None, timeout=None):
        captured["json"] = json
        return DummyResponse(
            json_data={
                "choices": [
                    {"message": {"content": "Direct reply"}}
                ]
            }
        )

    monkeypatch.setattr("chatbot.requests.post", fake_post)
    bot = FocusCoachBot()

    reply = bot.reply([{"role": "user", "content": "Need focus"}])

    assert reply == "Direct reply"
    assert captured["json"]["messages"][0]["role"] == "system"
    assert "direct" in captured["json"]["messages"][0]["content"].lower()
    assert "no-fluff" in captured["json"]["messages"][0]["content"].lower()


def test_api_failure_raises_clean_error(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")

    def fake_post(url, headers=None, json=None, timeout=None):
        return DummyResponse(status_code=429, text="rate limited")

    monkeypatch.setattr("chatbot.requests.post", fake_post)
    bot = FocusCoachBot()

    with pytest.raises(OpenRouterError, match="OpenRouter request failed"):
        bot.reply([{"role": "user", "content": "Need focus"}])
