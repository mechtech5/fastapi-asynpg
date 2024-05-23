import re
from typing import List

from app.models.base import TimestampModel, UUIDModel
from pydantic import BaseModel, EmailStr, validator
from sqlmodel import AutoString, Field, SQLModel


class UserBase(SQLModel):
    first_name: str = Field(max_length=200, nullable=False)
    last_name: str = Field(max_length=200, nullable=False)
    email: EmailStr = Field(nullable=False, unique=True, index=True, sa_type=AutoString)
    password: str = Field(max_length=200, nullable=False)
    reset_code: str = Field(max_length=6, nullable=True)


class User(TimestampModel, UserBase, UUIDModel, table=True):
    __tablename__ = "users"


class UserCreate(UserBase):
    pass


class UserRead(UserBase, UUIDModel):
    pass


class UserPatch(UserBase):
    pass


def check_password(password: str):
    # Check if the password length is between 8 and 15 characters
    if 8 <= len(password) <= 20:
        # Check if the password contains at least one upper case letter
        if any(char.isupper() for char in password):
            # Check if the password contains at least one special character
            if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                # Check if the password contains at least one number
                if any(char.isdigit() for char in password):
                    return True
    return False


def is_valid_password(password: str):
    if not check_password(password):
        raise ValueError("please give strong password with min 8 to max 15 char")
    else:
        return password


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: str


class UserLogin(SQLModel):
    email: EmailStr
    password: str


class UpdatePassword(BaseModel):
    old_password: str
    new_password: str
    _password_check = validator("new_password", check_fields=False, allow_reuse=True)(
        is_valid_password
    )


class NewPasswordRequest(BaseModel):
    id: str
    password: str
    token: str


class ErrorMessage(BaseModel):
    """
    ErrorMessage class for error properties
    """

    code: str
    message: str
    description: str
    path: str
    errors: List[str]
