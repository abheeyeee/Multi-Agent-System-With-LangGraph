from graph_builder import compiled_graph

if __name__ == "__main__":
    topic = input("Enter the topic to research: ")
    result = compiled_graph.invoke({
        "topic": topic,
        "research_data": [],
        "blog_post": ""
    })

    print("\n=== FINAL OUTPUT ===\n")
    print(result["blog_post"])

