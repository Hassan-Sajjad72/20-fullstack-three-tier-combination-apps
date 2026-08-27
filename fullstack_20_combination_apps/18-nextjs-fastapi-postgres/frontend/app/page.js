"use client";
import { useEffect, useState } from "react";
export default function Home() {
  const [message, setMessage] = useState("loading");
  const base = process.env.NEXT_PUBLIC_API_BASE_URL;
  useEffect(() => {
    fetch(`${base}/message`)
      .then(r => r.json())
      .then(d => setMessage(d.message))
      .catch(e => setMessage(`error: ${e.message}`));
  }, []);
  return <main style={{fontFamily:"system-ui",padding:"2rem"}}>
    <h1>Next.js static + FastAPI + PostgreSQL</h1><p id="api-message">{message}</p><small>API base: {base}</small>
  </main>;
}
