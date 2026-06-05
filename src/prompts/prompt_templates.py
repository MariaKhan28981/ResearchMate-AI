from langchain_core.prompts import ChatPromptTemplate


research_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are ResearchMate-AI, an assistant that helps users understand research papers."
        ),
        (
            "human",
            "{question}"
        )
    ]
)