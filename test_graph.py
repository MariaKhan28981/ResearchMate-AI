from src.agents.graph import create_research_graph


app = create_research_graph()


state = {

    "question": "What is the conclusion of this research paper?",

    "retrieved_chunks": [],

    "analysis": "",

    "final_answer": ""

}


result = app.invoke(state)


print("\nFinal state:")
print(result)