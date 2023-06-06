from pydantic import BaseModel
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class Role(Enum):
    user = "user"
    admin = "admin"

class User(BaseModel):
    username: str
    role: Role = Role.user


class UserInDB(User):
    hashed_password: str