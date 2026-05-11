from graph_builder import app
from state import AgentState

if __name__ == "__main__":
    print("Starting the Multi-Agent System...\n")
    
    # Check if we should prompt or not. For the test to pass we might want to just run the default or take user input
    try:
        topic = input("Please provide a topic: ")
        if not topic.strip():
            topic = "The future of AI Agents"
    except EOFError:
        topic = "The future of AI Agents"
    
    inputs: AgentState = {
        "topic": topic,
        "research_data": [],
        "blog_post": "",
    }
    
    result = app.invoke(inputs)
    
    print("\n---------------- FINAL OUTPUT ----------------\n")
    print(result["blog_post"])