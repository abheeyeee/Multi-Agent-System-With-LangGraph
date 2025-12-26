from graph_builder import compiled_graph
from input_handler import get_user_input, validate_input

if __name__ == "__main__":
    topic = get_user_input()
    validate_input(topic)
    result = compiled_graph.invoke({
        "topic": topic,
        "research_data": [],
        "blog_post": ""
    })

    print("\n=== FINAL OUTPUT ===\n")
    print(result["blog_post"])

