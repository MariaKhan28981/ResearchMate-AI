from src.agents.state import ResearchState

from src.rag.retriever import get_retriever



def retrieval_agent(state: ResearchState):

    print("\nRetrieval Agent running...")


    question = state["question"]


    retriever = get_retriever()


    documents = retriever.invoke(question)


    chunks = []


    for doc in documents:

        chunks.append(
            doc.page_content
        )


    state["retrieved_chunks"] = chunks


    print(
        f"Retrieved chunks: {len(chunks)}"
    )


    return state