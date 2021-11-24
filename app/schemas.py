from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


"""
   USERS
"""


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


"""
Posts
"""


class PostBase(BaseModel):
    title: str
    content: str
    # optional value
    published: bool = True
    # null optiona value
    #rating: Optional[int] = None


class PostCreated(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


"""
Token
"""


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


"""
Vote
"""


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)