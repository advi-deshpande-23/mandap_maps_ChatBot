import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export const fetchNearbyMandals = createAsyncThunk(
  "mandals/fetchNearby",
  async (_, { rejectWithValue }) => {
    if (!("geolocation" in navigator)) {
      return rejectWithValue("Location isn't available in this browser.");
    }
    try {
      const position = await new Promise((resolve, reject) =>
        navigator.geolocation.getCurrentPosition(resolve, reject, { timeout: 8000 })
      );
      const { latitude, longitude } = position.coords;
      const res = await fetch(
        `${API_BASE}/api/mandals/nearby?lat=${latitude}&lng=${longitude}&limit=5`
      );
      if (!res.ok) throw new Error(`Request failed: ${res.status}`);
      return await res.json();
    } catch (err) {
      return rejectWithValue(err.message || "Couldn't get your location.");
    }
  }
);

const mandalsSlice = createSlice({
  name: "mandals",
  initialState: {
    nearby: [],
    status: "idle", // idle | loading | error
    error: null,
    panelOpen: false,
  },
  reducers: {
    togglePanel(state) {
      state.panelOpen = !state.panelOpen;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchNearbyMandals.pending, (state) => {
        state.status = "loading";
        state.error = null;
      })
      .addCase(fetchNearbyMandals.fulfilled, (state, action) => {
        state.status = "idle";
        state.nearby = action.payload.mandals;
      })
      .addCase(fetchNearbyMandals.rejected, (state, action) => {
        state.status = "error";
        state.error = action.payload;
      });
  },
});

export const { togglePanel } = mandalsSlice.actions;
export default mandalsSlice.reducer;
