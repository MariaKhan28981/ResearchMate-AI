from src.rag.pdf_loader import load_pdf
from src.rag.splitter import split_documents
from src.rag.embeddings import get_embeddings


pdf = "data/raw/sample.pdf"


documents = load_pdf(pdf)

chunks = split_documents(documents)


embedding_model = get_embeddings()


vector = embedding_model.embed_query(
    chunks[0].page_content
)


print("Embedding length:", len(vector))

print("First 10 values:")
print(vector[:10])