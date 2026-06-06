from src.llm.llm_client import get_llm


def writing_agent(state: dict) -> dict:
    """
    Takes analysis output and converts it into final polished answer.
    """

    question = state["question"]
    analysis = state.get("analysis", "")
    chunks = state.get("retrieved_chunks", [])

    llm = get_llm()

    prompt = f"""
You are a professional research paper writing assistant.

Your job is to convert analysis into a clean, structured, high-quality final answer.

RULES:
- Do NOT repeat chunks verbatim
- Do NOT say "based on context"
- Do NOT mention retrieval process
- Keep answer concise but complete
- If analysis is weak, still produce best possible structured answer
- Use academic tone

QUESTION:
{question}

ANALYSIS:
{analysis}

RETRIEVED CONTEXT (for reference only):
{chunks}

Now write the final answer:
"""

    response = llm.invoke(prompt)

    state["final_answer"] = response.content if hasattr(response, "content") else str(response)

    return state