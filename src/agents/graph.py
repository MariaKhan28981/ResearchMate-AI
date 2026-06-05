from langgraph.graph import StateGraph, END

from src.agents.state import ResearchState

from src.agents.analysis_agent import analysis_agent
from src.agents.research_agent import research_agent
from src.agents.retrieval_agent import retrieval_agent



def create_research_graph():

    graph = StateGraph(ResearchState)

    graph.add_node(
        "analysis_agent",
        analysis_agent
    )

    graph.add_node(
        "research_agent",
        research_agent
    )


    graph.add_node(
        "retrieval_agent",
        retrieval_agent
    )


    graph.set_entry_point(
        "research_agent"
    )


    graph.add_edge(
        "research_agent",
        "retrieval_agent",
        "analysis_agent"
    )


    graph.add_edge(
        "retrieval_agent",
        
        END
    )

    graph.add_edge(
        "analysis_agent",
        END
    )

    

    return graph.compile()