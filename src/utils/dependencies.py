from fastapi import HTTPException, Request, status

from src.schemas.user_schema import UserSchema

def get_current_user(request: Request) -> UserSchema:
    """
    Extracts the current user from the request state.
    Args:
        request (Request): The incoming request.
    Returns:
        UserModel: The current user data.
    
    Raises:
        HTTPException: If the user data is not present or invalid in the request state.
    """
    user = request.state.user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )
    if not isinstance(user, UserSchema):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user data"
        )
    return user