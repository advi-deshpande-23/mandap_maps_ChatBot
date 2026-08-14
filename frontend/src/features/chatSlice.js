import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

function getOrCreateSessionId() {
  let id = localStorage.getItem("ekdanta_session_id");
  if (!id) {
    id = crypto.randomUUID();
    localStorage.setItem("ekdanta_session_id", id);
  }
  return id;
}

export const sendMessage = createAsyncThunk(
  "chat/sendMessage",
  async (query, { rejectWithValue }) => {
    try {
      const session_id = getOrCreateSessionId();
      const res = await fetch(`${API_BASE}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id, query, language: "auto" }),
      });
      if (!res.ok) throw new Error(`Request failed: ${res.status}`);
      return await res.json();
    } catch (err) {
      return rejectWithValue(err.message);
    }
  }
);

const chatSlice = createSlice({
  name: "chat",
  initialState: {
    messages: [
      {
        role: "assistant",
        text: "Ganpati Bappa Morya! 🙏 I'm Ekdanta — ask me about mandal timings, darshan queues, parking, transport or festival history.",
        sources: [],
      },
    ],
    status: "idle", // idle | loading | error
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(sendMessage.pending, (state, action) => {
        state.status = "loading";
        state.messages.push({ role: "user", text: action.meta.arg });
      })
      .addCase(sendMessage.fulfilled, (state, action) => {
        state.status = "idle";
        state.messages.push({
          role: "assistant",
          text: action.payload.answer,
          sources: action.payload.sources || [],
        });
      })
      .addCase(sendMessage.rejected, (state, action) => {
        state.status = "error";
        state.error = action.payload;
        state.messages.push({
          role: "assistant",
          text: "Sorry, I couldn't reach the assistant right now. Please make sure the backend and Ollama are running.",
          sources: [],
        });
      });
  },
});

export default chatSlice.reducer;
