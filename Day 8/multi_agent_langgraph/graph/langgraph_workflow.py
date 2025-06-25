from langgraph.graph import StateGraph, END
from langgraph.graph.message import AnyMessage
from agents.router_agent import RouterAgent
from agents.rag_agent import RAGAgent
from agents.web_research_agent import WebSearchAgent
from agents.summarizer_agent import SummarizerAgent

# State schema definition
state_schema = {
    "query": str,
    "rag_response": AnyMessage,
    "web_response": AnyMessage,
    "llm_response": AnyMessage,
    "final_response": str,
}

def build_graph(google_api_key: str, tavily_api_key: str, vectorstore_path: str):
    # Instantiate agents
    router_agent = RouterAgent()
    rag_agent = RAGAgent(vectorstore_path, google_api_key)
    websearch_agent = WebSearchAgent(tavily_api_key)
    summarization_agent = SummarizerAgent(google_api_key)

    # Create graph with schema
    graph = StateGraph(state_schema)

    # Add nodes
    graph.add_node("router", router_agent)
    graph.add_node("rag", rag_agent)
    graph.add_node("websearch", websearch_agent)
    graph.add_node("summarize", summarization_agent)

    # Define routing logic
    def route_decider(state):
        route = state["llm_response"].content.lower()
        if "web" in route:
            return "websearch"
        elif "rag" in route:
            return "rag"
        else:
            return "summarize"  # fallback

    # Connect the graph
    graph.set_entry_point("router")
    graph.add_conditional_edges("router", route_decider, {
        "websearch": "websearch",
        "rag": "rag",
        "summarize": "summarize",
    })

    graph.add_edge("websearch", "summarize")
    graph.add_edge("rag", "summarize")
    graph.set_finish_point("summarize")

    return graph.compile()
