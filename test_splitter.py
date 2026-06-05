from src.rag.pdf_loader import load_pdf
from src.rag.splitter import split_documents


pdf = "data/raw/sample.pdf"


documents = load_pdf(pdf)


chunks = split_documents(documents)


print("Original pages:", len(documents))

print("Total chunks:", len(chunks))


print("\nFirst chunk:")
print(chunks[0].page_content[:500])