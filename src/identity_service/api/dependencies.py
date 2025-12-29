from bami_chassis.infrastructure.config.settings import settings
from bami_chassis.infrastructure.database.session import get_session
from fastapi import Depends
from sqlalchemy.orm import Session

from identity_service.infrastructure.repositories.user_repo import UserRepository
from identity_service.infrastructure.security.jwt import JWTService
from identity_service.application.services.auth_service import AuthService


def get_user_repo(
    db: Session = Depends(get_session),
) -> UserRepository:
    return UserRepository(db)


def get_auth_service(
    repo: UserRepository = Depends(get_user_repo),
) -> AuthService:
    jwt_service = JWTService(
        secret=settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )
    return AuthService(repo, jwt_service)
