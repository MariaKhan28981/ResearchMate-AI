from langchain_ollama import ChatOllama



def writer_agent(state):


    llm = ChatOllama(

        model="llama3.2",

        temperature=0,

        num_predict=500

    )


    prompt=f"""

You are a research paper assistant.

Answer the user's question using ONLY the paper context.

Important rules:

- Answer only what was asked.
- Do not provide a full summary unless requested.
- Do not repeat unrelated sections.
- Do not guess.
- Do not use outside knowledge.
- Do not convert initials into fake full names.
- Authors means only the paper author list.


If information is unavailable, say:

"I could not find this information in the uploaded paper."


Question:

{state["question"]}


Paper Context:

{state["context"]}


Answer:

"""


    response = llm.invoke(prompt)


    return {

        "answer":response.content

    }