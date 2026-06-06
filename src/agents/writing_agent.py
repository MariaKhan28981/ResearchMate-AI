from src.llm.llm_client import get_llm

llm = get_llm()

def writing_agent(state: dict) -> dict:
    """
    Final writing agent that converts analysis into polished answer.
    """

    question = state["question"]
    analysis = state.get("analysis", "")
    chunks = state.get("retrieved_chunks", [])

    context = "\n\n".join(chunks)

    prompt = f"""
You are a research writing assistant.

Your task is to produce a FINAL polished answer.

Rules:
- Be precise
- Do not say "insufficient information"
- Use ONLY provided context
- Keep answer concise but complete
- If multiple interpretations exist, summarize best one

QUESTION:
{question}

ANALYSIS:
{analysis}

CONTEXT:
{context}

Now write the final answer:
"""

    response = llm.invoke(prompt)

    state["final_answer"] = response.content
    return state