from fastapi import FastAPI, HTTPException, Query, Header
from typing import Optional
from urja_client import UrjaClient

app = FastAPI(
    title="Flock Urja Meter Ops API",
    description="Clean, documented API wrapper for the Urja Meter Ops legacy portal.",
    version="1.0.0"
)

@app.get("/api/v1/meters", summary="List/Search Meters", tags=["Meters"])
def list_meters(
    page: int = Query(1, ge=1, description="Page number"),
    q: Optional[str] = Query("", description="Search query"),
    x_session_token: str = Header(..., alias="X-Session-Token", description="Session token for Urja portal auth")
):
    """
    Fetch a list of meters from the Urja portal with optional search query and pagination.
    """
    try:
        client = UrjaClient(session_token=x_session_token)
        return client.search_meters(page=page, query=q)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
