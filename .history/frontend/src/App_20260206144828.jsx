import { useState } from "react";
import "./index.css";

function App() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState([]);
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);

  const generateQuiz = async () => {
    if (!url) return alert("Paste a Wikipedia URL");

    setLoading(true);
    setSubmitted(false);
    setAnswers({});
    setQuiz([]);

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

  const handleOptionChange = (qIndex, option) => {
    setAnswers({ ...answers, [qIndex]: option });
  };

  const handleSubmit = () => {
    setSubmitted(true);
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

          {q.options.map((opt, idx) => (
            <label key={idx} style={{ display: "block", marginBottom: "6px" }}>
              <input
                type="radio"
                name={`question-${i}`}
                value={opt}
                disabled={submitted}
                checked={answers[i] === opt}
                onChange={() => handleOptionChange(i, opt)}
              />{" "}
              {opt}
            </label>
          ))}

          {submitted && (
            <div className="answer">
              {answers[i] === q.answer ? "✅ Correct!" : "❌ Wrong"}
              <br />
              ✔ Correct Answer: {q.answer}
            </div>
          )}
        </div>
      ))}

      {quiz.length > 0 && !submitted && (
        <button className="btn" style={{ marginTop: "20px" }} onClick={handleSubmit}>
          Submit Quiz
        </button>
      )}
    </div>
  );
}

export default App;
