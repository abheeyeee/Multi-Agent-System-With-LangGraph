from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from state import AgentState
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

def researcher_node(state: AgentState):
    print(">>> Researcher running")

    search = DuckDuckGoSearchRun()
    result = search.run(f"Explain {state['topic']}")

    return {
        "research_data": state.get("research_data", []) + [result]
    }

def writer_node(state: AgentState):
    print(">>> Writer running")

    llm = ChatOllama(model="llama3", temperature=0.7, base_url=OLLAMA_BASE_URL)

    prompt = ChatPromptTemplate.from_template(
        "Using the following research:\n{research}\n\nWrite a short blog post about {topic}."
    )

    chain = prompt | llm
    try:
        print(">>> Generating blog post...")
        full_content = ""
        for chunk in chain.stream({
            "topic": state["topic"],
            "research": "\n".join(state["research_data"])
        }):
            if chunk.content:
                print(chunk.content, end="", flush=True)
                full_content += chunk.content
        print() # Newline after streaming
        
        response_content = full_content
    except Exception as e:
        return {"blog_post": f"Error during generation: {str(e)}"}

    if not response_content:
        return {
            "blog_post": "Error: No content generated."
        }

    return {
        "blog_post": response_content
    }
