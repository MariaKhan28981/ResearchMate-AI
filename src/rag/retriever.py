from src.rag.embeddings import get_embeddings
from langchain_chroma import Chroma


def get_retriever():

    embeddings = get_embeddings()


    vector_store = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )


    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 15,
        }
    )


    return retriever