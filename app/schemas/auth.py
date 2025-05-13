from datetime import datetime
from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
