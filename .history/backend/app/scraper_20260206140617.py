import requests
from bs4 import BeautifulSoup
import re


def scrape_wikipedia(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title = soup.find("h1").get_text(strip=True)

    # First meaningful paragraphs
    paragraphs = soup.select("p")
    clean_paras = []

    for p in paragraphs:
        text = p.get_text(strip=True)
        if len(text) > 50:
            clean_paras.append(text)
        if len(clean_paras) == 2:   # ONLY 2 paragraphs
            break

    summary = " ".join(clean_paras)

    # Remove citation numbers like [1], [2]
    summary = re.sub(r"\[\d+\]", "", summary)

    return {
        "title": title,
        "summary": summary
    }
