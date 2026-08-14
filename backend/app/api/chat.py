from fastapi import APIRouter, HTTPException

from app.models.schemas import ChatRequest, ChatResponse
from app.core.rag_pipeline import answer_query
from app.core import memory

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        return await answer_query(request.session_id, request.query, request.language)
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail=f"Chat pipeline failed: {exc}")


@router.delete("/{session_id}")
async def clear_session(session_id: str):
    memory.clear_history(session_id)
    return {"status": "cleared", "session_id": session_id}


@router.get("/{session_id}/history")
async def get_session_history(session_id: str):
    return {"session_id": session_id, "history": memory.get_history(session_id)}
