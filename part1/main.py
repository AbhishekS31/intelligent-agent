from fastapi import FastAPI
from pydantic import BaseModel
from schemas import PromptRequest, PromptResponse
from agent import run_agent

app = FastAPI(
    title="Intelligent Agent API",
    description="Routes user prompt to appropriate tool based on system config - Rule-based decision making",
)

@app.get("/")
def root():
    return {"message": "Welcome to the Intelligent Agent API. Use /docs to try it out."}

@app.post("/agent", response_model=PromptResponse)
def agent_endpoint(request: PromptRequest):
    return run_agent(request.prompt)

