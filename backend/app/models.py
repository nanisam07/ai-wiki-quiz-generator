from sqlalchemy import Column, Integer, Text, JSON
from .database import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    url = Column(Text, unique=True)
    title = Column(Text)
    summary = Column(Text)
    sections = Column(JSON)
    quiz = Column(JSON)
    related_topics = Column(JSON)
    raw_html = Column(Text)
