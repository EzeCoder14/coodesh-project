from fastapi import APIRouter, Path, Request, HTTPException, Depends
from app.models.request import IntegrationRequest
from starlette.responses import JSONResponse
from app.providers import  get_provider_handler

router = APIRouter()

@router.post("/integrate/{provider}")
async def integrate(
    provider: str = Path(..., title="Provider name"),
    payload: IntegrationRequest = None,
    request: Request = None
):
    try:
        handler = get_provider_handler(provider)
        result = await handler(payload.action, payload.parameters)
        return JSONResponse(content={"status": "success", "data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")