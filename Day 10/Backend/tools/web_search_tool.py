from langchain.agents import Tool
from langchain.utilities import SerpAPIWrapper

def get_web_search_tool():
    search = SerpAPIWrapper()
    return Tool(
        name="Web Search",
        func=search.run,
        description="Useful for answering questions by searching the web."
    )
