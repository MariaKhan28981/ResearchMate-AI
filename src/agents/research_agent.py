from src.agents.state import ResearchState


def research_agent(state: ResearchState):

    question = state["question"]

    print("\nResearch Agent running...")

    print(f"User question: {question}")


    return state