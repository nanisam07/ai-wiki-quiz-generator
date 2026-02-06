# 🧠 Wiki Quiz Generator

A full-stack web application that generates interactive quizzes from any Wikipedia article using AI.  
Users paste a Wikipedia URL, attempt the quiz, submit answers, and instantly see results.

---

## 🚀 Live Demo

- **Frontend (Vercel):**  
  https://vm-lwug3ik0798ekv6xsskw0x.vusercontent.net/

- **Backend (Render):**  
  https://ai-wiki-quiz-generator-9n23.onrender.com

---

## 📌 Features

- 🔗 Paste any Wikipedia article URL
- 🤖 AI-generated quiz questions
- 📝 Multiple-choice questions
- ✅ Submit quiz to view correct answers
- 💾 Quiz history stored in database
- 🌐 Fully deployed frontend & backend

---

## 🛠️ Tech Stack

### Frontend
- React (Vite)
- JavaScript
- CSS
- Deployed on **Vercel**

### Backend
- FastAPI
- Python
- SQLite (`wikiquiz.db`)
- Wikipedia scraping (BeautifulSoup)
- AI-based quiz generation
- Deployed on **Render**

--ai-wiki-quiz-generator/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── scraper.py
│ │ ├── llm.py
│ │ ├── database.py
│ │ ├── crud.py
│ ├── wikiquiz.db
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ │ └── index.html
│ ├── src/
│ │ ├── App.js
│ │ ├── index.js
│ │ └── index.css
│ ├── package.json
│ └── vite.config.js
│
└── README.md


---

## ⚙️ Backend API Endpoints

### Generate Quiz


POST /generate-quiz?url=<wikipedia_url>


**Example**


POST /generate-quiz?url=https://en.wikipedia.org/wiki/Alan_Turing


---

### Quiz History


GET /history


Returns all previously generated quizzes.

---

## ▶️ Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend URL:

http://127.0.0.1:8000

Frontend
cd frontend
npm install
npm run dev


Frontend URL:

http://localhost:5173

📸 Screenshots

The following screenshots are included:

Homepage UI

Quiz generation

Quiz submission with answers

/history API response

Backend deployment on Render

Frontend deployment on Vercel

🎯 Key Highlights

Full-stack application

AI-powered quiz generation

REST API design using FastAPI

Error handling and caching

Production deployment

Interactive and user-friendly UI

🧑‍💻 Author

Samuel Victor
Full-Stack Developer | Backend & AI Enthusiast

📄 License

This project is created for educational and evaluation purposes.


---
