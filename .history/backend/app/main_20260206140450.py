from fastapi import FastAPI
from app.database import Base, engine, SessionLocal
from app.scraper import scrape_wikipedia
from app.llm import generate_quiz
from app.crud import get_by_url, save_quiz, get_all

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/generate-quiz")
def generate(url: str):
    db = SessionLocal()

    # Check cache
    cached = get_by_url(db, url)
    if cached:
        return {
            "url": cached.url,
            "title": cached.title,
            "summary": cached.summary,
            "quiz": cached.quiz
        }

    # Scrape Wikipedia
    scraped = scrape_wikipedia(url)

    # Generate quiz from summary
    quiz_data = generate_quiz(scraped["summary"])

    # Save ONLY essential fields
    data = {
        "url": url,
        "title": scraped["title"],
        "summary": scraped["summary"],
        "quiz": quiz_data["quiz"]
    }

    saved = save_quiz(db, data)

    # Return clean response
    return {
        "url": saved.url,
        "title": saved.title,
        "summary": saved.summary,
        "quiz": saved.quiz
    }


@app.get("/history")
def history():
    db = SessionLocal()
    records = get_all(db)

    return [
        {
            "url": r.url,
            "title": r.title,
            "summary": r.summary,
            "quiz": r.quiz
        }
        for r in records
    ]
