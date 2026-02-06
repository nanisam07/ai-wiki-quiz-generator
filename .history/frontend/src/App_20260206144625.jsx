import { useState } from "react";
import "./index.css";

function App() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState([]);
  const [loading, setLoading] = useState(false);

  const generateQuiz = async () => {
    if (!url) return alert("Paste a Wikipedia URL");
    setLoading(true);

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/generate-quiz?url=${url}`,
        { method: "POST" }
      );
      const data = await res.json();
      setQuiz(data.quiz.quiz);
    } catch {
      alert("Backend error");
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

      {quiz.map((q, i) => (
        <div className="card" key={i}>
          <h3>{i + 1}. {q.question}</h3>
          <ul>
            {q.options.map((o, idx) => (
              <li key={idx}>{o}</li>
            ))}
          </ul>
          <div className="answer">✔ Answer: {q.answer}</div>
        </div>
      ))}
    </div>
  );
}

export default App;
