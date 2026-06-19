from agents import state
from src.agents.state import ResearchState
from src.llm.llm_client import get_llm


def analysis_agent(state: ResearchState):

    print("\nAnalysis Agent running...")


    question = state["question"]

    chunks = state["retrieved_chunks"]


    context = "\n\n".join(chunks)


    llm = get_llm()


    prompt = """
    You are an expert research paper analyst.

    You are given retrieved sections from ONE research paper.

    Rules:
1. Use only the provided context.
2. Do not combine information from unrelated papers.
3. If a section looks unrelated, ignore it.
4. For summary:
   - identify paper goal
   - identify proposed method
   - identify experiments
   - identify conclusion
5. Never invent datasets, tasks, or methods.

Context:
{context}

Question:
{question}

Answer:
""" 
    
    response = llm.invoke(prompt)


    state["analysis"] = response.content


    return state