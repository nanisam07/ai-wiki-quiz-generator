import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generateQuiz = async () => {
    if (!url) {
      alert("Enter Wikipedia URL");
      return;
    }

    setLoading(true);
    setError("");
    setQuiz(null);

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/generate-quiz?url=${encodeURIComponent(url)}`,
        { method: "POST" }
      );

      if (!res.ok) throw new Error("Failed to fetch quiz");

      const data = await res.json();
      setQuiz(data.quiz.quiz);
    } catch (err) {
      setError("Backend not reachable or error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "auto" }}>
      <h1>🧠 Wiki Quiz Generator</h1>

      <input
        type="text"
        placeholder="Paste Wikipedia URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "100%", padding: "10px", marginBottom: "10px" }}
      />

      <button onClick={generateQuiz} style={{ padding: "10px 20px" }}>
        Generate Quiz
      </button>

      {loading && <p>⏳ Generating quiz...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {quiz && (
        <div style={{ marginTop: "20px" }}>
          {quiz.map((q, i) => (
            <div
              key={i}
              style={{
                border: "1px solid #ccc",
                padding: "10px",
                marginBottom: "10px",
              }}
            >
              <h3>
                {i + 1}. {q.question}
              </h3>
              <ul>
                {q.options.map((opt, idx) => (
                  <li key={idx}>{opt}</li>
                ))}
              </ul>
              <strong>Answer:</strong> {q.answer}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
