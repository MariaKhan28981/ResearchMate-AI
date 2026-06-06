from langgraph.graph import StateGraph, END

from src.agents.state import ResearchState

from src.agents.research_agent import research_agent
from src.agents.retrieval_agent import retrieval_agent
from src.agents.analysis_agent import analysis_agent
from src.agents.writing_agent import writing_agent  


def create_research_graph():

    graph = StateGraph(ResearchState)


    # Add agents as nodes

    graph.add_node(
        "research_agent",
        research_agent
    )


    graph.add_node(
        "retrieval_agent",
        retrieval_agent
    )


    graph.add_node(
        "analysis_agent",
        analysis_agent
    )



    # Define workflow

    graph.set_entry_point(
        "research_agent"
    )


    graph.add_edge(
        "research_agent",
        "retrieval_agent"
    )


    graph.add_edge(
        "retrieval_agent",
        "analysis_agent"
    )


    graph.add_edge(
        "analysis_agent",
        "writing_agent"
    )

    graph.add_edge(
        "writing_agent",
        END
    )
    
    graph.add_node(
        "writing_agent", 
        writing_agent
        )

    return graph.compile()