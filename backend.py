from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


from fastapi import FastAPI

ALLOWED_MODEL_NAMES=["LLama3-70b-8192", "mixtral-8x7b-32768", "LLama-3.3-70b-versatile","gpt-40-mini"]

app=FastAPI(title="Langgraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """API Endpoint to interact with the Chatbot using LangGraph and search tools.
       It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI Model"}
    
    