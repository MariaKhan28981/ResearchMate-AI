from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


DB="chroma_db"


def create_vectorstore(docs):

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )


    db=Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=DB
    )

    return db



def get_vectorstore():

    embeddings=OllamaEmbeddings(
        model="nomic-embed-text"
    )


    return Chroma(
        persist_directory=DB,
        embedding_function=embeddings
    )