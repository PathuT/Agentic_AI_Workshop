from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def get_top_attractions(city: str) -> str:
    """Returns top tourist attractions in the city."""
    search = DuckDuckGoSearchResults()
    return search.run(f"Top tourist attractions in {city}")
