from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import FastAPI, Request, Response
from sqlalchemy import text
from starlette.middleware.base import RequestResponseEndpoint

from icibina.config import Settings, get_settings
from icibina.errors import install_error_handlers
from icibina.infrastructure.database.session import create_engine, create_session_factory
from icibina.infrastructure.database.uow import SQLAlchemyUnitOfWork
from icibina.interface.health import router as health_router
from icibina.logging_config import configure_logging
from icibina.modules.courses.interface.router import router as courses_router


def create_app(settings: Settings | None = None) -> FastAPI:
    app_settings = settings or get_settings()
    configure_logging(app_settings.log_level)

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        engine = create_engine(app_settings)
        session_factory = create_session_factory(engine)
        app.state.uow_factory = lambda: SQLAlchemyUnitOfWork(session_factory)

        async def database_ping() -> bool:
            try:
                async with engine.connect() as connection:
                    await connection.execute(text("SELECT 1"))
                return True
            except Exception:
                app.state.logger.exception("database readiness check failed")
                return False

        app.state.database_ping = database_ping
        yield
        await engine.dispose()

    app = FastAPI(title=app_settings.app_name, version="0.1.0", lifespan=lifespan)
    app.state.logger = logging.getLogger("icibina")

    @app.middleware("http")
    async def request_id_middleware(
        request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        request.state.request_id = request.headers.get("X-Request-ID", str(uuid4()))
        response = await call_next(request)
        response.headers["X-Request-ID"] = request.state.request_id
        return response

    install_error_handlers(app)
    app.include_router(health_router)
    app.include_router(courses_router)
    return app


app = create_app()
