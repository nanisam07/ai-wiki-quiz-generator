from fastapi import FastAPI
from .database import Base, engine, SessionLocal
from .scraper import scrape_wikipedia
from .llm import generate_quiz
from .crud import get_by_url, save_quiz, get_all

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/generate-quiz")
def generate(url: str):
    db = SessionLocal()

    cached = get_by_url(db, url)
    if cached:
        return cached

    scraped = scrape_wikipedia(url)
    quiz_json = generate_quiz(scraped["summary"])

    data = {
        "url": url,
        "title": scraped["title"],
        "summary": scraped["summary"],
        "sections": scraped["sections"],
        "quiz": quiz_json,
        "related_topics": [],
        "raw_html": scraped["raw_html"]
    }

    return save_quiz(db, data)

@app.get("/history")
def history():
    db = SessionLocal()
    return get_all(db)
