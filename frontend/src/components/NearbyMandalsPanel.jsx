import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchNearbyMandals, togglePanel } from "../features/mandalsSlice.js";

export default function NearbyMandalsPanel() {
  const dispatch = useDispatch();
  const { nearby, status, error, panelOpen } = useSelector((s) => s.mandals);

  useEffect(() => {
    if (panelOpen && nearby.length === 0 && status === "idle") {
      dispatch(fetchNearbyMandals());
    }
  }, [panelOpen]); // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <div className="border-b border-turmeric/40 bg-white">
      <button
        onClick={() => dispatch(togglePanel())}
        className="w-full flex items-center justify-between px-4 py-2 text-sm font-medium text-sindoor"
      >
        <span>📍 Mandals near me</span>
        <span className="text-leaf/50">{panelOpen ? "▲" : "▼"}</span>
      </button>

      {panelOpen && (
        <div className="px-4 pb-3">
          {status === "loading" && (
            <p className="text-xs text-leaf/60 italic">Finding mandals near you…</p>
          )}
          {status === "error" && (
            <p className="text-xs text-red-700">
              {error || "Couldn't get your location."} You can still ask me by area name in chat.
            </p>
          )}
          {status === "idle" && nearby.length > 0 && (
            <ul className="space-y-2">
              {nearby.map((m) => (
                <li key={m.doc_id} className="flex items-center justify-between text-sm">
                  <div>
                    <p className="font-medium text-leaf">{m.name_en}</p>
                    <p className="text-xs text-leaf/60">{m.area}</p>
                  </div>
                  <span className="text-xs text-marigold font-semibold">{m.distance_km} km</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}
