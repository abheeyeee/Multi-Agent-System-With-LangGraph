# LangGraph Multi-Agent System

This is a demo of a multi-agent system built using [LangGraph](https://github.com/langchain-ai/langgraph). The system consists of two agents: a Researcher and a Writer. They collaborate to research a topic and write a brief blog post about it.

## Agents

1.  **Researcher**: Uses DuckDuckGo to search for information about the given topic.
2.  **Writer**: Uses a local LLM (via Ollama) to write a blog post based on the research data provided by the Researcher.

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running locally.
- The `llama3` model pulled in Ollama (`ollama pull llama3`).

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Ensure Ollama is running.

2.  Run the main script:
    ```bash
    python main.py
    ```

3.  Enter the topic you want the agents to research and write about when prompted.

    Example:
    ```
    Enter the topic to research: Artificial Intelligence Agents
    ```

4.  The system will output the progress and finally the generated blog post.

## File Structure

- `main.py`: The entry point of the application.
- `agents.py`: Defines the agent nodes (Researcher and Writer).
- `graph_builder.py`: Constructs the LangGraph workflow.
- `state.py`: Defines the state object passed between agents.
- `requirements.txt`: List of project dependencies.
