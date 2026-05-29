# Focus Coach Bot

OpenRouter-powered Streamlit chatbot with a direct productivity-coach personality.

## Run

```bash
pip install -r requirements.txt
set OPENROUTER_API_KEY=your_key_here
# optional
set OPENROUTER_MODEL=deepseek/deepseek-r1-0528:free
streamlit run app.py
```

## What It Does

- Uses OpenRouter for live responses
- Keeps a direct coaching style through a fixed system prompt
- Keeps chat history in the Streamlit session
- Requires `OPENROUTER_API_KEY`
