from .models import Quiz

def get_by_url(db, url):
    return db.query(Quiz).filter(Quiz.url == url).first()

def save_quiz(db, data):
    quiz = Quiz(**data)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def get_all(db):
    return db.query(Quiz).all()
