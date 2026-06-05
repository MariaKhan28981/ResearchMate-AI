from src.rag.retriever import get_retriever
from src.llm.llm_client import get_llm


def create_rag_chain():

    retriever = get_retriever()

    llm = get_llm()


    def ask(question):

        documents = retriever.invoke(question)


        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )


        prompt = f"""
You are ResearchMate-AI.

Answer the question using only the provided context.
Rules:
- Do not use outside knowledge.
- If the answer is not present in context, say so.
- Prefer information from abstract, introduction, and conclusion sections.
- Give a concise research-style answer.


Context:
{context}


Question:
{question}

Answer:
"""


        response = llm.invoke(prompt)

        sources=[]

        for doc in documents:
            page=doc.metadata.get("page")
            source=doc.metadata.get("source")

            sources.append(
                f"Page {page+1}: {source}"
            )

        return response.content + "\n\nSources:\n" + "\n".join(sources)


    return ask