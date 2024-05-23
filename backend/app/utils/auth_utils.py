import secrets
import string
from datetime import datetime, timedelta
from typing import List

from core.config import get_api_settings
from core.db import get_async_session
from crud.user import UsersCRUD, get_users_crud
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import JWTError, jwt
from models.user import TokenData, User
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
settings = get_api_settings()
SECRET_KEY = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5zA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0U1V2W3X4Y5Z!@#$%^&*()_+-="
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)


def get_random_password():
    # Define the character set for generating the password
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Set the minimum and maximum password lengths
    min_length = 8
    max_length = 15

    # Generate a random password with a length between min_length and max_length
    password_length = secrets.randbelow(max_length - min_length + 1) + min_length
    password = "".join(secrets.choice(alphabet) for _ in range(password_length))

    return password


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)

        id: str = payload.get("sub")

        if id is None:
            raise credentials_exception
        token_data = TokenData(sub=id)
    except JWTError:
        raise credentials_exception
    return token_data


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    users: UsersCRUD = Depends(get_users_crud),
    session: AsyncSession = Depends(get_async_session),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(sub=user_id)
    except JWTError:
        raise credentials_exception
    user_data = await users.get(user_id=user_id)
    if user_data is None:
        raise credentials_exception
    return token_data


async def get_user_by_user_id(session, user_id: str):
    db_user = session.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return db_user


def resolve_scopes(desire_scopes: List[str], user_scopes: List[str]):
    for desire_scope in desire_scopes:
        if desire_scope in user_scopes:
            return
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not enough permissions",
    )
