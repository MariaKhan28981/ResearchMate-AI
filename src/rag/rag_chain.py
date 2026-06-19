from src.rag.retriever import get_retriever
from src.llm.llm_client import get_llm
from langchain.prompts import PromptTemplate

def create_rag_chain():

    retriever = get_retriever()

    llm = get_llm()


    def ask(question):

        documents = retriever.invoke(question)


        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )


      from langchain.prompts import PromptTemplate


prompt = PromptTemplate(
    input_variables=[
        "context",
        "question"
    ],
    template="""

You are a research paper assistant.

Answer ONLY from the provided context.

If the answer is not present in the context,
say:
"I cannot find this information in the paper."

Do not guess.
Do not use outside knowledge.

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