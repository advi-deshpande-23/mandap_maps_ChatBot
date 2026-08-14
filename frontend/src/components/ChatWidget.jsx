import React, { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { sendMessage } from "../features/chatSlice.js";
import NearbyMandalsPanel from "./NearbyMandalsPanel.jsx";

export default function ChatWidget() {
  const dispatch = useDispatch();
  const { messages, status } = useSelector((s) => s.chat);
  const [input, setInput] = useState("");
  const scrollRef = useRef(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [messages]);

  const handleSend = (e) => {
    e.preventDefault();
    const trimmed = input.trim();
    if (!trimmed || status === "loading") return;
    dispatch(sendMessage(trimmed));
    setInput("");
  };

  return (
    <div className="flex flex-col h-screen max-w-xl mx-auto bg-ivory">
      {/* Header — marigold garland motif as the signature element */}
      <header className="relative bg-sindoor text-ivory px-5 pt-5 pb-4 shadow-md">
        <h1 className="font-display text-xl font-bold tracking-wide">Ekdanta</h1>
        <p className="text-sm text-turmeric font-medium">Your Ganeshotsav companion, Pune</p>
        <div
          className="absolute bottom-0 left-0 w-full h-2"
          style={{
            backgroundImage:
              "repeating-radial-gradient(circle at 8px 0px, #E7A33E 0 4px, transparent 5px)",
            backgroundSize: "16px 8px",
          }}
          aria-hidden="true"
        />
      </header>

      <NearbyMandalsPanel />

      {/* Message list */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto px-4 py-5 space-y-4">
        {messages.map((m, i) => (
          <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm leading-relaxed shadow-sm ${
                m.role === "user"
                  ? "bg-marigold text-leaf rounded-br-sm"
                  : "bg-white text-leaf border border-turmeric/40 rounded-bl-sm"
              }`}
            >
              <p>{m.text}</p>
              {m.sources && m.sources.length > 0 && (
                <details className="mt-2 text-xs text-leaf/70">
                  <summary className="cursor-pointer font-medium">Sources</summary>
                  <ul className="mt-1 space-y-1 list-disc list-inside">
                    {m.sources.map((s, j) => (
                      <li key={j}>{s.source}</li>
                    ))}
                  </ul>
                </details>
              )}
            </div>
          </div>
        ))}
        {status === "loading" && (
          <div className="flex justify-start">
            <div className="bg-white border border-turmeric/40 rounded-2xl rounded-bl-sm px-4 py-3 text-sm text-leaf/60 italic">
              Ekdanta is checking the mandal records…
            </div>
          </div>
        )}
      </div>

      {/* Input */}
      <form onSubmit={handleSend} className="flex items-center gap-2 px-4 py-3 bg-white border-t border-turmeric/40">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about darshan timings, parking, routes…"
          className="flex-1 rounded-full border border-leaf/20 px-4 py-2 text-sm text-leaf focus:outline-none focus:ring-2 focus:ring-marigold"
        />
        <button
          type="submit"
          disabled={status === "loading"}
          className="rounded-full bg-sindoor text-ivory px-5 py-2 text-sm font-medium disabled:opacity-50 hover:bg-sindoor/90 transition"
        >
          Send
        </button>
      </form>
    </div>
  );
}
