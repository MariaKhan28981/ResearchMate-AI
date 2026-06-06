from fastapi import FastAPI
from pydantic import BaseModel

from src.agents.graph import create_research_graph

app = FastAPI(title="ResearchMate AI", version="1.0")

# Load graph ONCE (important for speed)
graph = create_research_graph()


# Request schema
class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query(request: QueryRequest):
    try:
        input_state = {
            "question": request.question,
            "retrieved_chunks": [],
            "analysis": "",
            "final_answer": ""
        }

        result = graph.invoke(input_state)

        return {
            "question": result.get("question"),
            "answer": result.get("final_answer", ""),
            "analysis": result.get("analysis", ""),
            "chunks_used": result.get("retrieved_chunks", [])
        }

    except Exception as e:
        return {
            "error": str(e)
        }