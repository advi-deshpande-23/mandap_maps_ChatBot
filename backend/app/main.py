import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.api import chat, ingest, mandals

logging.basicConfig(level=logging.INFO)
settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="Hybrid RAG chatbot for Pune Ganeshotsav (Ekdanta) — powered by FAISS + BM25 + Ollama.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(ingest.router)
app.include_router(mandals.router)


@app.get("/health")
async def health():
    return {"status": "ok", "app": settings.APP_NAME}
