import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    if "wikipedia.org/wiki/" not in url:
        raise ValueError("Invalid Wikipedia URL")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        raise ValueError("Failed to fetch Wikipedia page")

    soup = BeautifulSoup(response.text, "html.parser")

    # SAFELY extract title
    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else "Unknown Title"

    # Extract summary paragraphs
    paragraphs = soup.select("p")
    summary = " ".join(
        p.text.strip() for p in paragraphs[:8] if p.text.strip()
    )

    # Extract section headings
    sections = [
        h.text.strip()
        for h in soup.select("h2 span.mw-headline")
    ]

    return {
        "title": title,
        "summary": summary,
        "sections": sections,
        "url": url
    }
