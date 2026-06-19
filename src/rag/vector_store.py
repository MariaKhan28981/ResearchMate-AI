from langchain_chroma import Chroma
from src.rag.embeddings import get_embeddings


def create_vector_store(chunks):

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="data/vectorstore"
    )

    return vector_store