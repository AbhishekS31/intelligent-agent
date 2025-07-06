## Intelligent Agent API

Live API: [https://intelligent-agent.onrender.com/docs](https://intelligent-agent.onrender.com/docs)

A production-grade FastAPI service that routes user prompts to intelligent tools such as weather, jokes, and quotes using a rule-based system prompt.

## Features

- Rule-based agent with pluggable tools
- System prompt (tone, fallback, tool routing) defined in structured JSON
- Fully automated evaluation framework with rule-based pass/fail reporting
- FastAPI REST endpoint with structured Pydantic models
- Dockerized and deployable on Render or any cloud provider
- Cleanly organized, production-ready code

## Setup Instructions

```bash
git clone https://github.com/yourusername/intelligent-agent-api.git
cd intelligent-agent-api/part1
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit the interactive API docs at:  
[http://localhost:8000/docs](http://localhost:8000/docs)

## API Usage

### Endpoint

```
POST /agent
```

### Request Payload

```json
{
  "prompt": "Tell me a joke"
}
```

### Response Format

```json
{
  "response": "Why don't scientists trust atoms? Because they make up everything!",
  "metadata": {
    "tool_used": "joke",
    "success": true,
    "reason": null
  }
}
```

## System Prompt

The system prompt is defined in `prompts/system_config.json`. It guides the agent behavior for:

- Tool routing based on keywords
- Friendly tone configuration
- Fallback messages for unsupported or failed prompts

```json
{
  "tone": "friendly and slightly humorous",
  "fallback": {
    "no_match": "Sorry, can't help with that.",
    "tool_failed": "Sorry! That didn’t work. You can try again?"
  },
  "tools": {
    "weather": ["weather", "temperature", "forecast", "rain", "hot", "cold"],
    "joke": ["joke", "laugh", "funny", "humor"],
    "quote": ["quote", "inspire", "motivation", "life", "saying"]
  }
}
```

## Testing Instructions

### Unit Tests

```bash
pytest tests/test_agent.py
```

Tests include:
- Valid prompt-tool routing
- Edge case behavior
- Fallback response testing

### Evaluation Framework

Run the automated rule-based evaluation:

```bash
python evaluate.py
```

Sample Output:

```
Prompt: What's the weather in Delhi today?
Expected Tool: weather
Actual Tool: weather
Success: True
Status: PASS
```

## Docker Instructions

### Build the Docker Image

```bash
docker build -t intelligent-agent-api .
```

### Run the Container

```bash
docker run -p 8000:8000 intelligent-agent-api
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Deployment Instructions (Render)

1. Go to [https://render.com](https://render.com)
2. Click "New Web Service" → "From GitHub"
3. Select your repository
4. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2`
   - Environment: Python 3.11
   - Port: 8000
5. Click "Deploy"

Your app will be live at a public URL provided by Render.

## Tools Overview

- **Weather Tool (`tool_weather.py`)**  
  Retrieves current weather information using the Tomorrow.io external API.

- **Joke Tool (`tool_joke.py`)**  
  Provides a random, hardcoded joke from a predefined list.

- **Quote Tool (`tool_quote.py`)**  
  Returns a motivational or inspirational quote from a static collection.

## Evaluation Criteria Coverage

-  FastAPI service implemented for structured API interaction.
-  Intelligent agent design using a rule-based routing mechanism.
-  System prompt defined in structured JSON and applied during tool selection and fallback.
-  Three tools integrated (weather, joke, quote) — exceeding the two-tool requirement.
-  Unit tests created to validate prompt routing, tool execution, and fallback behavior.
-  Rule-based automated evaluation framework (`evaluate.py`) implemented to score system accuracy.
-  Service containerized using Docker with a minimal, optimized image.
-  Deployment guide and instructions included for Render cloud hosting.
-  Production-grade concurrency configuration (`--workers 2`) included in Docker startup command.
