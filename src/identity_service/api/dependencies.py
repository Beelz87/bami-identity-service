from bami_chassis.infrastructure.config.settings import settings

from identity_service.application.services.auth_service import AuthService
from identity_service.infrastructure.repositories.user_repo import UserRepository
from identity_service.infrastructure.security.jwt import JWTService


_user_repo = UserRepository()

def get_auth_service() -> AuthService:
    jwt_service = JWTService(
        secret=settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )
    return AuthService(_user_repo, jwt_service)
