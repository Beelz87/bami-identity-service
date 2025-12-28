from datetime import datetime, timedelta
from jose import jwt


class JWTService:
    def __init__(self, secret: str, algorithm: str = "HS256"):
        self.secret = secret
        self.algorithm = algorithm

    def encode(self, payload: dict, ttl_seconds: int) -> str:
        payload = payload.copy()
        payload["exp"] = datetime.now() + timedelta(seconds=ttl_seconds)
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def decode(self, token: str) -> dict:
        return jwt.decode(token, self.secret, algorithms=[self.algorithm])
