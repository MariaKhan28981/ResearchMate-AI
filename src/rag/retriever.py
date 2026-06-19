from langchain_chroma import Chroma
from src.rag.embeddings import get_embeddings


def create_retriever(vector_store):

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 8,
            "fetch_k": 30,
            "lambda_mult": 0.7
        }
    )

    return retriever

