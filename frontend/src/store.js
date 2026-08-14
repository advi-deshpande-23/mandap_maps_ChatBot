import { configureStore } from "@reduxjs/toolkit";
import chatReducer from "./features/chatSlice.js";
import mandalsReducer from "./features/mandalsSlice.js";

export const store = configureStore({
  reducer: {
    chat: chatReducer,
    mandals: mandalsReducer,
  },
});
