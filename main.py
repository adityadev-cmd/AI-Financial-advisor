import os
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import asyncio

from my_agent.agent import call_agent


app = FastAPI(title="Gemini Agent 3 Pro", description="HTTP API for the Gemini search agent")


class QueryRequest(BaseModel):
    query: str


@app.get("/healthz")
async def healthz():
    """Health check endpoint for Cloud Run."""
    return {"status": "ok"}


@app.post("/chat")
async def chat(request: QueryRequest):
    """
    Call the Gemini search agent with a user query.
    """
    # Ensure we always run the agent coroutine in an event loop
    response_text = await call_agent(request.query)
    return {"answer": response_text}


def main():
    # Used for local development; Cloud Run will invoke uvicorn via the container CMD
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
