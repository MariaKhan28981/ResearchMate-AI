from app.rag.vectorstore import get_vectorstore
from app.storage import load_summary


def research_agent(state):

    print("🔍 Research Agent running")


    vectorstore = get_vectorstore()


    question = state["question"]


    # Handle summary questions
    if "summary" in question.lower():

        cached_summary = load_summary()

        if cached_summary:

            return {
                "context": cached_summary,
                "sources": [
                    "Generated Summary"
                ]
            }


    # Get first pages for global awareness
    all_docs = vectorstore.get()


    global_context = ""


    if all_docs and "documents" in all_docs:

        global_context = "\n\n".join(
            all_docs["documents"][:8]
        )


    # Semantic retrieval
    docs = vectorstore.similarity_search(
        question,
        k=8
    )


    context = (
        "[PAPER OVERVIEW]\n"
        + global_context
        +
        "\n\n[RELEVANT SECTIONS]\n"
    )


    sources=[]


    for d in docs:

        context += (
            f"\n\nPage {d.metadata['page']}:\n"
            f"{d.page_content}"
        )


        sources.append(
            f"Page {d.metadata['page']}"
        )


    return {

        "context": context,

        "sources": sources

    }