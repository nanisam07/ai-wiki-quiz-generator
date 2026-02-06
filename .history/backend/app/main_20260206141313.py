from fastapi import FastAPI
from app.database import Base, engine, SessionLocal
from app.scraper import scrape_wikipedia
from app.llm import generate_quiz
from app.crud import get_by_url, save_quiz, get_all

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/generate-quiz")
def generate(url: str):
    db = SessionLocal()

    cached = get_by_url(db, url)
    if cached:
        return {
            "id": cached.id,
            "title": cached.title,
            "url": cached.url,
            "quiz": cached.quiz
        }

    scraped = scrape_wikipedia(url)
    quiz_json = generate_quiz(scraped["summary"])

    data = {
        "url": url,
        "title": scraped["title"],
        "summary": scraped["summary"],   # optional
        "quiz": quiz_json
    }

    saved = save_quiz(db, data)

    return {
        "id": saved.id,
        "title": saved.title,
        "url": saved.url,
        "quiz": saved.quiz
    }

@app.get("/history")
def history():
    db = SessionLocal()
    quizzes = get_all(db)

    return [
        {
            "id": q.id,
            "title": q.title,
            "url": q.url
        }
        for q in quizzes
    ]
