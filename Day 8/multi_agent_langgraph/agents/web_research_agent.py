from langchain_community.tools.tavily_search import TavilySearchResults

class WebSearchAgent:
    def __init__(self, tavily_api_key: str):
        self.search = TavilySearchResults(api_key=tavily_api_key)

    def run(self, query: str) -> str:
        return self.search.run(query)
