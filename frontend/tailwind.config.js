/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        // Ekdanta palette — inspired by modak leaf-wrap green, marigold,
        // and deep sindoor red rather than generic AI-chat purple/cream.
        sindoor: "#8C2F26",   // deep vermillion — header / primary
        marigold: "#E7A33E",  // accent — user bubbles, highlights
        turmeric: "#F5D06F",  // secondary accent
        leaf: "#274B3B",      // deep green — text on light bg
        ivory: "#FBF4E6",     // warm background
      },
      fontFamily: {
        display: ["'Poppins'", "sans-serif"],
        body: ["'Inter'", "sans-serif"],
      },
    },
  },
  plugins: [],
};
