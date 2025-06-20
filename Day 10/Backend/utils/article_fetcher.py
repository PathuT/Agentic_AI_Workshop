# utils/article_fetcher.py
import requests
from bs4 import BeautifulSoup

def fetch_linkedin_article_text(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/90.0.4430.93 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # This selector may vary — find article content container
        article_content = soup.find_all("p")  # naive: get all <p> tags text

        text = "\n".join(p.get_text() for p in article_content)
        return text.strip()
    except Exception as e:
        return f"Error fetching article: {e}"
