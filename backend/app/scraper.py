import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        raise ValueError("Failed to fetch Wikipedia page")

    soup = BeautifulSoup(response.text, "html.parser")

    # SAFE title extraction
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Unknown title"

    # First paragraph summary
    summary = ""
    for p in soup.select("div.mw-parser-output > p"):
        if p.get_text(strip=True):
            summary = p.get_text(strip=True)
            break

    return {
        "title": title,
        "summary": summary
    }
