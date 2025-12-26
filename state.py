from typing import TypedDict, List
from langgraph.graph import StateGraph, END
class AgentState(TypedDict):
    topic: str
    research_data: List[str]
    blog_post: str

def validate_state(state: AgentState) -> bool:
    if not state.get("topic"):
        return False
    return True


