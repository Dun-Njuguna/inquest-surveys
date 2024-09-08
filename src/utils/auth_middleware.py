from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse
from fastapi import status
from pydantic import ValidationError
from src.schemas.user_schema import UserSchema
from typing import List

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, exempt_paths: List[str] = None):
        super().__init__(app)
        self.exempt_paths = exempt_paths or []

    async def dispatch(self, request: Request, call_next):
        # Check if the path is exempt from authentication
        if any(request.url.path.startswith(path) for path in self.exempt_paths):
            return await call_next(request)

        # Retrieve user data from headers
        user_id = request.headers.get("X-User-ID")
        user_email = request.headers.get("X-User-Email")
        user_username = request.headers.get("X-User-Username")

        # Check if all required user data is present
        if not (user_id and user_email and user_username):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"error": True, "message": "Missing user data in headers", "data": None},
            )

        try:
            # Validate and attach user data to the request state
            request.state.user = UserSchema(
                id=user_id,
                email=user_email,
                username=user_username
            )
        except ValidationError as e:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"error": True, "message": "Invalid user data", "data": str(e)},
            )

        # Proceed to the next middleware or route handler
        response = await call_next(request)
        return response
