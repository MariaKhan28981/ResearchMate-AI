from typing import TypedDict, List


class ResearchState(TypedDict):

    question: str

    retrieved_chunks: List[str]

    analysis: str

    final_answer: str