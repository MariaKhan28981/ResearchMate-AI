from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


def get_vectorstore(chat_id: str):

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    db_path = f"app/data/chats/{chat_id}/chroma"

    return Chroma(
        persist_directory=db_path,
        embedding_function=embeddings
    )