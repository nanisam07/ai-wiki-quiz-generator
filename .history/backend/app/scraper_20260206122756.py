import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    if "wikipedia.org/wiki/" not in url:
        raise ValueError("Invalid Wikipedia URL")

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find("h1").text
    paragraphs = soup.select("p")
    summary = " ".join(p.text for p in paragraphs[:8])

    sections = [h.text for h in soup.select("h2 span.mw-headline")]

    return {
        "title": title,
        "summary": summary,
        "sections": sections,
        "raw_html": res.text
    }
