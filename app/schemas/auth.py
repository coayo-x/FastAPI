from pydantic import BaseModel

from schemas.user import UserRead


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LogoutRequest(BaseModel):
    token: str


class MessageResponse(BaseModel):
    message: str


class MeResponse(BaseModel):
    user: UserRead
