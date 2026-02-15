from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud.auth import blacklist_token, is_token_blacklisted
from crud.user import get_user_by_username
from db import get_db
from dependencies import get_current_user, oauth2_scheme
from models.user import User
from schemas.auth import LoginRequest, MeResponse, MessageResponse, LogoutRequest, TokenResponse
from security import create_access_token, verify_password

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse, summary="Login and receive JWT")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> TokenResponse:
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    token = create_access_token(subject=user.username)
    return TokenResponse(access_token=token)



@router.post("/logout", response_model=MessageResponse, summary="Logout and blacklist token")
def logout(
    payload: LogoutRequest,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
) -> MessageResponse:
    if payload.token != token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token body must match bearer token")

    if not is_token_blacklisted(db, token):
        blacklist_token(db, token)

    return MessageResponse(message="Logged out successfully")


@router.get("/me", response_model=MeResponse, summary="Get current authenticated user")
def me(current_user: User = Depends(get_current_user)) -> MeResponse:
    return MeResponse(user=current_user)
