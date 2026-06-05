from src.rag.rag_chain import create_rag_chain


rag = create_rag_chain()


answer = rag(
    rag(
"Summarize this paper in 5 points"
)
)


print(answer)