from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from state import AgentState

def researcher_node(state: AgentState):
    topic = state["topic"]
    print(f"Researcher is looking up: {topic}...")
    
    search = DuckDuckGoSearchRun()
    
    try:
        # You can tweak this query as you like
        results = search.run(f"key facts and latest news about {topic}")
    except Exception as e:
        results = f"Could not find data: {e}"
        
    print("Research complete.")
    
    # Only return the keys you want to update
    return {"research_data": state.get("research_data", []) + [results]}

def writer_node(state: AgentState):
    print("Writer is drafting the post...")
    
    topic = state["topic"]
    data = state["research_data"][-1] if state["research_data"] else ""
    
    llm = ChatOllama(model="llama3", temperature=0.7)
    
    prompt = ChatPromptTemplate.from_template(
        """You are a tech blog writer. 
Write a short, engaging blog post about "{topic}" 
based ONLY on the following research data:

{data}

Return just the blog post content."""
    )
    
    chain = prompt | llm
    response = chain.invoke({"topic": topic, "data": data})
    
    print("Writing complete.")
    return {"blog_post": response.content}
