import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

function App() {
  const [message, setMessage] = useState("loading");
  const base = import.meta.env.VITE_API_BASE_URL;
  useEffect(() => {
    fetch(`${base}/message`)
      .then(r => r.json())
      .then(d => setMessage(d.message))
      .catch(e => setMessage(`error: ${e.message}`));
  }, []);
  return <main style={{fontFamily:"system-ui",padding:"2rem"}}>
    <h1>React + Flask + PostgreSQL</h1>
    <p id="api-message">{message}</p>
    <small>API base: {base}</small>
  </main>;
}

createRoot(document.getElementById("root")).render(<App />);
