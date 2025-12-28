from fastapi import APIRouter, Depends

from identity_service.api.dependencies import get_auth_service
from identity_service.application.dto.login import LoginRequest
from identity_service.application.dto.register import RegisterRequest
from identity_service.application.dto.refresh import RefreshTokenRequest
from identity_service.application.dto.token import TokenResponse
from identity_service.application.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(req: LoginRequest, svc: AuthService = Depends(get_auth_service)):
    return svc.login(req.username, req.password)


@router.post("/register", response_model=TokenResponse)
def register(req: RegisterRequest, svc: AuthService = Depends(get_auth_service)):
    return svc.register(req.username, req.password)


@router.post("/refresh", response_model=TokenResponse)
def refresh(req: RefreshTokenRequest, svc: AuthService = Depends(get_auth_service)):
    return svc.refresh(req.refresh_token)
