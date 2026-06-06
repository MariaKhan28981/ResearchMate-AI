from src.agents.research_agent import research_agent


state = {

    "question": "what is the conclusion of this research paper",

    "retrieved_chunks": [],

    "analysis": "",

    "final_answer": ""
}


result = research_agent(state)


print(result)