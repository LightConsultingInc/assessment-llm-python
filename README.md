# LightCI LLM

![chat](screenshot1.png)

## Setup Instructions

### Web

```terminal
cd web
npm install
npm run dev
```

### API

```terminal
cd api
npm install
npm run dev
```

## Task Instructions

Your assignment is to integrate an LLM into this existing chat app. The feature should answer the user's question as if it were Abe Lincoln, and also filter the user question for only PG rated topics, otherwise a polite message response indicating "no answer" should be provided.

### OpenAI API Key

Add this in `api/api/settings.py`

```python
OPENAI_API_KEY = 'your-openai-api-key'
```

## Open AI Playground

Here is a link: [https://platform.openai.com/playground/chat](https://platform.openai.com/playground/chat)
