from src.rag.retriever import get_retriever


retriever = get_retriever()


query = "What is the main contribution of this paper?"


results = retriever.invoke(query)

for r in results:
    print("\nPage:",r.metadata["page"])
    print(r.page_content[:200])

print("Number of retrieved chunks:", len(results))


for i, doc in enumerate(results):

    print("\n--- Result", i+1, "---")

    print(doc.page_content[:500])

    print("Metadata:", doc.metadata)