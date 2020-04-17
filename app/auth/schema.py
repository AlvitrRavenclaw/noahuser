from pydantic import BaseModel


class LoginEntry(BaseModel):
    username: str
    password: str
