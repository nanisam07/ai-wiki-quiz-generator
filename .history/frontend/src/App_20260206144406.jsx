import { useState } from "react";
import "./index.css";

function App() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateQuiz = async () => {
    setLoading(true);
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/generate-quiz?url=${url}`,
        { method: "POST" }
      );
      const data = await res.json();
      setQuiz(data.quiz.quiz);
    } catch (e) {
      alert("Backend not reachable");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1 className="title">🧠 Wiki Quiz Generator</h1>

      <input
        className="input"
        placeholder="Paste Wikipedia URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <button className="btn" onClick={generateQuiz}>
        {loading ? "Generating..." : "Generate Quiz"}
      </button>

      {quiz &&
        quiz.map((q, i) => (
          <div className="card fade-in" key={i}>
            <h3>{i + 1}. {q.question}</h3>
            <ul>
              {q.options.map((op, idx) => (
                <li key={idx}>{op}</li>
              ))}
            </ul>
            <p className="answer">✔ Answer: {q.answer}</p>
          </div>
        ))}
    </div>
  );
}

export default App;
