import { useState } from "react";

export default function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);

  const generate = async () => {
    const res = await fetch("http://localhost:8000/generate-quiz?url=" + url, {
      method: "POST"
    });
    setResult(await res.json());
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>AI Wiki Quiz Generator</h2>

      <input
        value={url}
        onChange={e => setUrl(e.target.value)}
        placeholder="Wikipedia URL"
        style={{ width: "60%" }}
      />
      <button onClick={generate}>Generate Quiz</button>

      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
