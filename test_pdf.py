from src.rag.pdf_loader import load_pdf


pdf = "data/raw/sample.pdf"


documents = load_pdf(pdf)


print("Number of pages:", len(documents))


for i, doc in enumerate(documents[:2]):
    print("\n--- Page", i+1, "---")
    print(doc.page_content[:500])