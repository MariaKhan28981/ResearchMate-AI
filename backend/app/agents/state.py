from typing import TypedDict, List


class AgentState(TypedDict):

    question: str

    context: str

    answer: str

    sources: List[str]