from langgraph.graph import StateGraph, END
from state import AgentState
from agents import researcher_node, writer_node

# ----- Build the LangGraph -----
workflow = StateGraph(AgentState)

workflow.add_node("Researcher", researcher_node)
workflow.add_node("Writer", writer_node)

# Flow: Start -> Researcher -> Writer -> END
workflow.set_entry_point("Researcher")
workflow.add_edge("Researcher", "Writer")
workflow.add_edge("Writer", END)

app = workflow.compile()