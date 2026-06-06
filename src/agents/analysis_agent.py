from src.agents.state import ResearchState
from src.llm.llm_client import get_llm


def analysis_agent(state: ResearchState):

    print("\nAnalysis Agent running...")


    question = state["question"]

    chunks = state["retrieved_chunks"]


    context = "\n\n".join(chunks)


    llm = get_llm()


    prompt = f"""

You are a carefulresearch paper analyst.

RULES:
- Use ONLY the provided context
- Ignore code fragments and tables unless relevant
- Do NOT guess missing information
- If context is unclear, say "insufficient information"


Question:
{question}


Context:
{context}


Give a clear analysis.

"""


    response = llm.invoke(prompt)


    state["analysis"] = response.content


    return state