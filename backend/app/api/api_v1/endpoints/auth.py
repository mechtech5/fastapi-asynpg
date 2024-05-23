from core.config import get_api_settings
from core.db import get_async_session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security.oauth2 import OAuth2PasswordBearer
from models.user import Token, User, UserCreate, UserRead
from crud.user import UsersCRUD, get_users_crud
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from utils import auth_utils
from utils.auth_utils import get_random_password, hash_password
from utils.mail_utils import send_sendgrid_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
settings = get_api_settings()

auth_router = APIRouter()

# @auth_router.post("/token", response_model=Token)
# async def token(
#     user_credientials: OAuth2PasswordRequestForm = Depends(),
#     session: AsyncSession = Depends(get_async_session)
# ):
#     db_verification = (
#         session.query(UserAuthentication)
#         .filter(UserAuthentication.email == user_credientials.username)
#         .first()
#     )

#     users_data = (
#         session.query(users.User, Company)
#         .join(Company, Company.id == User.company_id)
#         .filter(users.User.email == user_credientials.username)
#         .all()
#     )

#     if not db_verification:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credientials"
#         )
#     else:
#         if not auth_utils.verify_password(
#             user_credientials.password, db_verification.password
#         ):
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credientials"
#             )

#         user_objects = []
#         for user in users_data:
#             user_objects.append(
#                 {
#                     "user_id": user.User.id,
#                     "company_name": user.Company.name,
#                     "company_id": user.Company.id,
#                     "is_rank_1": user.User.is_rank_1,
#                     "name": user.User.first_name + " " + user.User.last_name,
#                 }
#             )

#         data = {
#             "sub": str(db_verification.id),
#             "scopes": db_verification.scopes["scopes"],
#             "is_super_admin": db_verification.is_super_admin,
#             "user_data": user_objects,
#         }

#         access_token = auth_utils.create_access_token(data)
#         return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post(
    "/register", response_model=UserRead, status_code=status.HTTP_201_CREATED
)
async def register(data: UserCreate, users: UsersCRUD = Depends(get_users_crud)):
    data.password = hash_password(data.password)
    user = await users.create(data=data)

    return user


@auth_router.post("/login", response_model=Token)
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    users: UsersCRUD = Depends(get_users_crud),
):
    user = await users.get_by_email(user_credentials.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials"
        )
    else:
        if not auth_utils.verify_password(user_credentials.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials"
            )
    print(type(user))
    data = {
        "sub": str(user.uuid),
        "user": {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        },
    }
    access_token = auth_utils.create_access_token(data)
    return {"access_token": access_token, "token_type": "bearer"}


# @auth_router.post(
#     "/login",
#     response_model=Token,
#     status_code=status.HTTP_200_OK,
# )
# async def login(
#     verify_code_dto: str,
#     session: AsyncSession = Depends(get_async_session)
# ):
#     """
#     This endpoint verifies a four digit verification code sent over email.
#     """

#     return user_service.verify_code(verify_code_dto, session=session)


# @auth_router.post(
#     "/logout",
#     status_code=status.HTTP_200_OK,
# )
# async def logout(
#     token: str = Depends(oauth2_scheme),
#     session: AsyncSession = Depends(get_async_session)
# ):
#     # Create a new instance of BlacklistedToken with deleted_at set to the current time
#     blacklisted_token = BlacklistedToken(token=token, deleted_at=datetime.utcnow())
#     session.add(blacklisted_token)
#     session.commit()
#     return {"message": "Logout successful"}


# @auth_router.post("/request_reset_token")
# async def request_reset_token(
#     email: str,
#     session: Session = Depends(get_session),
# ):
#     # Check if the user with the given email exists
#     user = (
#         session.query(UserAuthentication)
#         .filter(UserAuthentication.email == email)
#         .first()
#     )

#     if not user:
#         return {
#             "message": "You will receive reset link on email if you have entered valid email!",
#         }
#         # raise HTTPException(
#         #     status_code=status.HTTP_404_NOT_FOUND,
#         #     detail="You will receive reset link on email if you have entered valid email",
#         # )
#     else:
#         if (
#             user.reset_token_expiration is not None
#             and datetime.utcnow() < user.reset_token_expiration
#         ):
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Reset link already sent to mail",
#             )
#         # Generate a reset token
#         token = secrets.token_urlsafe(32)

#         # Set reset token and expiration time for the user
#         user.reset_token = token
#         user.reset_token_expiration = datetime.utcnow() + timedelta(hours=1)

#         session.add(user)
#         session.commit()
#         session.refresh(user)

#     # Send the token to the user (e.g., via email)
#     # You can use a mail library or another method of your choice to send the token.
#     message_fmt = f"Link to reset your password is {settings.CLIENT_URL}/reset-password/{user.reset_token}/{user.id}"

#     email_payload = SmsPayload(
#         email=email,
#         subject="Welcome to Trustool",
#         message=message_fmt,
#     )
#     send_sendgrid_email(email_payload)
#     return {
#         "message": "You will receive reset link on email if you have entered valid email!",
#         # "link": message_fmt,
#     }


# @auth_router.put("/reset-password")
# async def update_password(
#     user_password_dto: NewPasswordRequest,
#     session: Session = Depends(get_session),
# ):
#     """
#     This endpoint creates a pin for the specified user.
#     """
#     user = (
#         session.query(UserAuthentication)
#         .filter(UserAuthentication.id == user_password_dto.id)
#         .first()
#     )

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
#         )
#     else:
#         if user.reset_token_expiration is not None:
#             if datetime.utcnow() > user.reset_token_expiration:
#                 user.reset_token_expiration = None
#                 user.reset_token = None
#                 session.add(user)
#                 session.commit()
#                 session.refresh(user)
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="Password reset link expired!",
#                 )
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Password reset link expired!",
#             )

#         if user.reset_token == user_password_dto.token:
#             # Check if existing password and new password are the same
#             if pwd_context.verify(user_password_dto.password, user.password):
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="Existing and new password cannot be the same",
#                 )

#             hash_password = get_password(user_password_dto.password)
#             user.password = hash_password
#             user.reset_token = None
#             user.reset_token_expiration = None
#             session.add(user)
#             session.commit()
#             session.refresh(user)
#             return "Password reseted successfully!"
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Token!"
#             )


# @auth_router.put("/create-password")
# async def create_password(
#     user_password_dto: NewPasswordRequest,
#     session: Session = Depends(get_session),
# ):
#     user = (
#         session.query(UserAuthentication)
#         .filter(UserAuthentication.id == user_password_dto.id)
#         .first()
#     )

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
#         )
#     else:
#         if user.create_token_expiration is not None:
#             if datetime.utcnow() > user.create_token_expiration:
#                 user.create_token_expiration = None
#                 user.create_token = None
#                 session.add(user)
#                 session.commit()
#                 session.refresh(user)
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="Password create link expired!",
#                 )
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Password create link expired!",
#             )

#         if user.create_token == user_password_dto.token:
#             hash_password = get_password(user_password_dto.password)
#             user.password = hash_password
#             user.create_token = None
#             user.create_token_expiration = None
#             session.add(user)
#             session.commit()
#             session.refresh(user)
#             return "Password created successfully!"
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Token!"
#             )
