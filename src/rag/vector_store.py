from langchain_community.vectorstores import Chroma
from src.rag.embeddings import get_embeddings


# -----------------------------
# STEP 1: Chunk quality filter
# -----------------------------
def is_valid_chunk(text: str) -> bool:
    """
    Stronger PDF chunk filter for RAG quality.
    Removes tables, code, references, and noise.
    """

    if not text:
        return False

    text = text.strip()

    # too short
    if len(text) < 80:
        return False

    # code fragments
    bad_patterns = [
        "torch.",
        "loss_",
        ">>>>>>>",
        "<<<",
        "== REPLACE ==",
        "import ",
    ]

    for p in bad_patterns:
        if p in text:
            return False

    # tables (very important fix)
    if "|" in text and text.count("|") > 5:
        return False

    # reference sections / bibliography noise
    if "references" in text.lower():
        return False

    # figure captions often useless for RAG QA
    if "figure" in text.lower() and len(text.split()) < 30:
        return False

    # numbers-only table fragments
    alpha_count = sum(c.isalpha() for c in text)
    if alpha_count < 30:
        return False

    return True

# -----------------------------
# STEP 2: Create vector store
# -----------------------------
def create_vector_store(chunks):
    """
    Takes cleaned document chunks,
    converts them into embeddings,
    and stores them in ChromaDB.
    """

    print("Creating vector store...")

    # Step 1: filter chunks
    filtered_chunks = [
        chunk for chunk in chunks
        if is_valid_chunk(chunk.page_content)
    ]

    print(f"Original chunks: {len(chunks)}")
    print(f"Filtered chunks: {len(filtered_chunks)}")

    # Step 2: embeddings model
    embeddings = get_embeddings()

    # Step 3: build vector DB
    vectorstore = Chroma.from_documents(
        documents=filtered_chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    print("Vector store created successfully")

    return vectorstore