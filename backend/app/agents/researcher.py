from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


DB_DIR = "chroma_db"
COLLECTION_NAME = "current_paper"



def research_agent(state):

    print("🔍 Research agent searching...")


    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )


    vectorstore = Chroma(

        persist_directory=DB_DIR,

        embedding_function=embeddings,

        collection_name=COLLECTION_NAME

    )



    question = state["question"]



    # ---------------------------------
    # Get complete paper information
    # First pages -> title/authors
    # Last pages -> conclusion/future scope
    # ---------------------------------

    all_docs = vectorstore.get()



    global_context = ""



    if all_docs and "documents" in all_docs:


        documents = all_docs["documents"]

        metadatas = all_docs["metadatas"]


        total = len(documents)



        # first pages
        for text, meta in zip(

            documents[:5],

            metadatas[:5]

        ):


            global_context += f"""

PAGE {meta.get("page")}

{text}

----------------

"""



        # last pages
        if total > 5:


            for text, meta in zip(

                documents[-5:],

                metadatas[-5:]

            ):


                global_context += f"""

PAGE {meta.get("page")}

{text}

----------------

"""



    # ---------------------------------
    # Semantic retrieval
    # ---------------------------------

    results = vectorstore.similarity_search(

        question,

        k=8

    )



    search_context = ""



    for doc in results:


        search_context += f"""

PAGE {doc.metadata.get("page")}

{doc.page_content}

----------------

"""



    final_context = f"""

===== IMPORTANT PAPER PAGES =====

{global_context}



===== RELEVANT SEARCH RESULTS =====

{search_context}

"""



    return {

        "context": final_context

    }