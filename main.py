from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.agents.graph import create_research_graph


app = FastAPI(
    title="ResearchMate AI",
    version="1.0",
    description="AI Research Assistant using RAG and Agents"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = create_research_graph()


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "ResearchMate AI is running 🚀"
    }


@app.post("/query")
def query(request: QueryRequest):

    state = {
        "question": request.question,
        "retrieved_chunks": [],
        "analysis": "",
        "final_answer": ""
    }


    result = graph.invoke(state)


    return {
        "question": request.question,
        "answer": result.get("final_answer"),
        "analysis": result.get("analysis")
    }