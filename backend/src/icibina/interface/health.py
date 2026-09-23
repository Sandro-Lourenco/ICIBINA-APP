from collections.abc import Awaitable, Callable
from typing import cast

from fastapi import APIRouter, Request, Response, status
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    status: str


@router.get("/live", response_model=HealthResponse)
async def live() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/ready", response_model=HealthResponse)
async def ready(request: Request, response: Response) -> HealthResponse:
    ping = cast(Callable[[], Awaitable[bool]], request.app.state.database_ping)
    if await ping():
        return HealthResponse(status="ready")
    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return HealthResponse(status="not_ready")
