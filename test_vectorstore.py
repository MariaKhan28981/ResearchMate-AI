from src.rag.pdf_loader import load_pdf
from src.rag.splitter import split_documents
from src.rag.vector_store import create_vector_store


pdf = "data/raw/sample.pdf"


documents = load_pdf(pdf)


chunks = split_documents(documents)


vector_store = create_vector_store(chunks)


print("Vector store created successfully")