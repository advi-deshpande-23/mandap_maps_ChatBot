from fastapi import APIRouter, HTTPException

from app.models.schemas import IngestDocument, IngestResponse
from app.core.vector_store import get_vector_store

router = APIRouter(prefix="/api/ingest", tags=["ingest"])


@router.post("", response_model=IngestResponse)
async def ingest_document(doc: IngestDocument):
    try:
        store = get_vector_store()
        n_chunks = store.add_document(doc.doc_id, doc.title, doc.text, doc.category)
        return IngestResponse(ingested_chunks=n_chunks, doc_id=doc.doc_id)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {exc}")


@router.get("/stats")
async def ingest_stats():
    store = get_vector_store()
    chunks = store.all_chunks()
    categories = {}
    for c in chunks:
        categories[c["category"]] = categories.get(c["category"], 0) + 1
    return {"total_chunks": len(chunks), "by_category": categories}
