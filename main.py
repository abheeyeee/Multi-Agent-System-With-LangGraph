from graph_builder import compiled_graph

import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    topic = input("Please provide a topic: ")
    result = compiled_graph.invoke({
        "topic": topic,
        "research_data": [],
        "blog_post": ""
    })

    print("\n=== FINAL OUTPUT ===\n")
    print(result["blog_post"])

