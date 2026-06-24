from typing import TypedDict


class AgentState(TypedDict):

    chat_id: str

    question: str

    context: str

    answer: str

    history: str