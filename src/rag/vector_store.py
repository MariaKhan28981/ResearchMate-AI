from langchain_chroma import Chroma
from src.rag.embeddings import get_embeddings


def create_vector_store(chunks):

    embeddings = get_embeddings()


    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    for i, chunk in enumerate(chunks[:5]):
        print("\nCHUNK", i)
        print(chunk.page_content[:300])

    return vector_store