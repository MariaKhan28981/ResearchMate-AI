from langchain_ollama import ChatOllama


def writer_agent(state):

    print("✍️ Writer agent generating answer...")

    llm = ChatOllama(
        model="llama3.2",
        temperature=0,
        num_predict=700
    )

    prompt = f"""
You are ResearchHelp,
an expert academic research assistant.

Conversation History:

{state["history"]}


Retrieved Paper Context:

{state["context"]}


Current Question:

{state["question"]}


Rules:

1. Use ONLY the provided paper context.

2. Use conversation history to understand references like:
   - "they"
   - "this method"
   - "that dataset"

3. Do NOT invent information.

4. If the answer cannot be found, respond:

"I could not find this information in the uploaded papers."

5. If multiple papers are involved,
mention which paper the answer comes from.

6. For summaries:
Provide:

- Title
- Authors
- Research Problem
- Methodology
- Dataset
- Results
- Conclusion

Only when user explicitly asks for a summary.


Answer:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }