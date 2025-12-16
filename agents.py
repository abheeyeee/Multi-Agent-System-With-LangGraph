from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from state import AgentState

def researcher_node(state: AgentState):
    print(">>> Researcher running")

    search = DuckDuckGoSearchRun()
    result = search.run(f"Explain {state['topic']}")

    return {
        "research_data": state.get("research_data", []) + [result]
    }

def writer_node(state: AgentState):
    print(">>> Writer running")

    llm = ChatOllama(model="llama3", temperature=0.7)

    prompt = ChatPromptTemplate.from_template(
        "Using the following research:\n{research}\n\nWrite a short blog post about {topic}."
    )

    chain = prompt | llm

    response = chain.invoke({
        "topic": state["topic"],
        "research": "\n".join(state["research_data"])
    })

    return {
        "blog_post": response.content
    }

