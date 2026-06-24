from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.agents.state import AgentState
from app.agents.researcher import research_agent
from app.agents.writer import writer_agent


def build_graph():

    workflow = StateGraph(
        AgentState
    )

    workflow.add_node(
        "researcher",
        research_agent
    )

    workflow.add_node(
        "writer",
        writer_agent
    )

    workflow.add_edge(
        START,
        "researcher"
    )

    workflow.add_edge(
        "researcher",
        "writer"
    )

    workflow.add_edge(
        "writer",
        END
    )

    return workflow.compile()