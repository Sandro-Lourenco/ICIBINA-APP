from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ErrorBody(BaseModel):
    code: str
    message: str
    request_id: str
    details: list[dict[str, Any]] | None = None


def install_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
        body = ErrorBody(
            code="validation_error",
            message="Request validation failed",
            request_id=request.state.request_id,
            details=jsonable_encoder(exc.errors()),
        )
        return JSONResponse(status_code=422, content=body.model_dump(mode="json"))

    @app.exception_handler(Exception)
    async def unhandled_error(request: Request, exc: Exception) -> JSONResponse:
        request.app.state.logger.exception(
            "unhandled request error", extra={"request_id": request.state.request_id}
        )
        body = ErrorBody(
            code="internal_error",
            message="An internal error occurred",
            request_id=request.state.request_id,
        )
        return JSONResponse(status_code=500, content=body.model_dump(mode="json"))
