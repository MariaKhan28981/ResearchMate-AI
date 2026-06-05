from src.agents.state import ResearchState
from src.llm.llm import get_llm


def analysis_agent(state: ResearchState):

    print("\nAnalysis Agent running...")


    question = state["question"]

    chunks = state["retrieved_chunks"]


    context = "\n\n".join(chunks)


    llm = get_llm()


    prompt = f"""

You are a research paper analysis assistant.

Use only the provided context.

Question:
{question}


Context:
{context}


Give a clear analysis.

"""


    response = llm.invoke(prompt)


    state["analysis"] = response.content


    return state