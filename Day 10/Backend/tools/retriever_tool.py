from langchain.agents import Tool

def retriever_function(query: str) -> str:
    return "This is a dummy retrieved answer for query: " + query

retriever_tool = Tool(
    name="Retriever",
    func=retriever_function,
    description="Retrieve relevant documents or data for a query."
)
