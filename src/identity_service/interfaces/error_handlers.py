from fastapi import Request
from fastapi.responses import JSONResponse
from identity_service.domain.exceptions.auth import InvalidCredential


async def invalid_credential_handler(request: Request, exc: InvalidCredential):
    return JSONResponse(
        status_code=401,
        content={
            "error": "invalid_credential",
            "message": "Username or password is incorrect",
        },
    )
