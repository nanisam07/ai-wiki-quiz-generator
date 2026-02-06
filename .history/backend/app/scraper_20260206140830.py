import requests
from bs4 import BeautifulSoup
import re


def scrape_wikipedia(url: str):
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise ValueError("Failed to fetch Wikipedia page")

    soup = BeautifulSoup(response.text, "html.parser")

    h1 = soup.find("h1")
    if not h1:
        raise ValueError("Invalid Wikipedia page")

    title = h1.get_text(strip=True)

    paragraphs = soup.select("p")
    clean_paras = []

    for p in paragraphs:
        text = p.get_text(strip=True)
        if len(text) > 50:
            clean_paras.append(text)
        if len(clean_paras) == 2:
            break

    summary = " ".join(clean_paras)
    summary = re.sub(r"\[\d+\]", "", summary)

    return {
        "title": title,
        "summary": summary
    }
