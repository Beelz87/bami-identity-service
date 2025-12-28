from identity_service.domain.exceptions.auth import (
    InvalidCredential,
    UserAlreadyExists,
    InvalidRefreshToken,
)
from identity_service.infrastructure.security import password


class AuthService:
    def __init__(self, user_repo, jwt_service):
        self.user_repo = user_repo
        self.jwt = jwt_service

    def register(self, username: str, raw_password: str):
        if self.user_repo.get_by_username(username):
            raise UserAlreadyExists()

        hashed = password.hash_password(raw_password)

        user = self.user_repo.create(
            username=username,
            password=hashed,
            roles=["user"],
            tenant_id="default",
        )

        return self._issue_tokens(user)

    def login(self, username: str, raw_password: str):
        user = self.user_repo.get_by_username(username)

        if not user or not password.verify_password(raw_password, user.password):
            raise InvalidCredential()

        return self._issue_tokens(user)

    def refresh(self, refresh_token: str):
        try:
            payload = self.jwt.decode(refresh_token)
        except Exception:
            raise InvalidRefreshToken()

        if payload.get("type") != "refresh":
            raise InvalidRefreshToken()

        user = self.user_repo.get_by_id(payload["sub"])
        if not user:
            raise InvalidRefreshToken()

        return self._issue_access_token(user)

    # -------- internal helpers --------

    def _issue_tokens(self, user):
        access_token = self._issue_access_token(user)
        refresh_token = self.jwt.encode(
            {"sub": user.id, "type": "refresh"},
            ttl_seconds=60 * 60 * 24 * 7,
        )

        return {
            "access_token": access_token["access_token"],
            "refresh_token": refresh_token,
            "expires_in": access_token["expires_in"],
        }

    def _issue_access_token(self, user):
        token = self.jwt.encode(
            {
                "sub": user.id,
                "roles": user.roles,
                "tenant_id": user.tenant_id,
                "type": "access",
            },
            ttl_seconds=3600,
        )
        return {
            "access_token": token,
            "expires_in": 3600,
        }
