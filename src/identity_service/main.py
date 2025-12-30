from bami_chassis.bootstrap.app_factory.api_app_factory import create_app
from src.identity_service.api.v1.auth import router as auth_router

app = create_app(
    service_name="identity-service"
)

app.include_router(
    auth_router,
    prefix="/api/v1",
)
