from fastapi import APIRouter
from pydantic import BaseModel


from app.agents.graph import build_graph



router=APIRouter()


graph=build_graph()



from app.models import QuestionRequest



@router.post("/chat")
def chat(
    request:QuestionRequest
):


    result=graph.invoke(

        {
        "question":request.question,
        "context":"",
        "answer":"",
        "sources":[]
        }

    )


    return {

        "answer":result["answer"],

        "sources":result["sources"]

    }