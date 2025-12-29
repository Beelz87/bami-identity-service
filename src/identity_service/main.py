from bami_chassis.interfaces.api import metrics_router
from bami_chassis.interfaces.api.health import health_router
from fastapi import FastAPI
from bami_chassis import (
    settings,
    RequestLoggingMiddleware,
    MetricsMiddleware,
    TracingMiddleware,
    init_tracer,
    instrument_app,
)

from identity_service.api.v1 import auth


def create_app() -> FastAPI:
    app = FastAPI(
        title="identity service",
        debug=settings.debug,
    )

    app.add_middleware(MetricsMiddleware)

    if settings.enable_tracing:
        init_tracer()
        instrument_app(app)
        app.add_middleware(TracingMiddleware)

    app.include_router(health_router)
    app.include_router(metrics_router)
    app.include_router(auth.router, prefix="/api/v1")

    return app

app = create_app()
