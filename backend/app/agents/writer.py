from langchain_ollama import ChatOllama


def writer_agent(state):

    print("✍️ Writer Agent running")


    llm = ChatOllama(
        model="llama3.2",
        temperature=0.1
    )


    prompt=f"""

You are a research paper expert.

Your job is to answer questions about a paper.

Use ALL available context:
- Paper overview
- Relevant sections


Rules:

1. For author/title/date questions:
   prioritize the paper overview.

2. For summary questions:
   create a structured summary:

   - Title
   - Authors
   - Problem
   - Methodology
   - Dataset
   - Results
   - Conclusion


3. Never hallucinate.

4. If information is unavailable say:
"I cannot find this in the paper."


Question:

{state["question"]}


Context:

{state["context"]}


Answer:

"""


    response = llm.invoke(prompt)


    return {
        "answer": response.content
    }