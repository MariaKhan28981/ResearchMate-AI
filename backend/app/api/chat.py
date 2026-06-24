from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.graph import build_graph

from app.core.memory import (
    save_message,
    get_recent_history
)


router = APIRouter()

graph = build_graph()


class ChatRequest(BaseModel):

    chat_id: str

    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    history = get_recent_history(
        request.chat_id
    )

    result = graph.invoke(

        {
            "chat_id": request.chat_id,

            "question": request.question,

            "context": "",

            "answer": "",

            "history": history
        }

    )

    save_message(
        request.chat_id,
        "user",
        request.question
    )

    save_message(
        request.chat_id,
        "assistant",
        result["answer"]
    )

    return {

        "answer": result["answer"]

    }