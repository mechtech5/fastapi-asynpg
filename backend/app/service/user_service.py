import logging
import random

from sqlmodel import Session, select
from fastapi import HTTPException, status, BackgroundTasks
from utils.mail_utils import send_sendgrid_email
from models.user import (
    UserCreate, 
    User,
    UpdatePassword
)


from core.config import get_api_settings
from utils.auth_utils import get_random_password, hash_password
from utils import auth_utils
from utils.base_utils import get_url
from datetime import datetime, timedelta
import secrets
# import bcrypt

LOGGER = logging.getLogger("information")
settings = get_api_settings()

verification_key = b"6yuT2fVyAHFpzmoH26Ic70K5euPIMm1eqdgfdfg"


class UserService:
    MAX_OTP_ATTEMPTS = 5
    LOCKOUT_DURATION = timedelta(hours=1)
    # LOCKOUT_DURATION = timedelta(minutes=5)

    def create_user_and_company(
        self, user_dto: UserCreate, session: Session, background_tasks: BackgroundTasks
    ):
        db_company = session.exec(
            select(Company).filter(Company.name == user_dto.company_details.name)
        ).first()

        print("Company", db_company)

        user_json = user_dto.dict(
            exclude={"company_details": True, "company_id": True, "auth_id": True}
        )

        if db_company:
            db_company_user = session.exec(
                select(User)
                .filter(User.email == user_dto.email)
                .filter(User.company_id == db_company.id)
            ).first()

            if db_company_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Profile already exist with same user and company",
                )
            else:
                try:
                    auth_user_id = self.registration(
                        user_dto,
                        email=user_dto.email,
                        session=session,
                        background_tasks=background_tasks,
                    )
                    db_user = User(
                        **user_json, company_id=db_company.id, auth_id=auth_user_id
                    )
                    session.add(db_user)
                    session.commit()
                    session.flush()
                    session.refresh(db_user)
                    if db_user.is_rank_1:
                        existing_rank_1_user = session.exec(
                            select(User)
                            .filter(User.is_rank_1 == True)
                            .filter(User.company_id == db_company.id)
                            .filter(User.id != db_user.id)
                        ).first()
                        if existing_rank_1_user:
                            existing_rank_1_user.is_rank_1 = False
                            session.commit()
                except Exception as database_exception:
                    session.rollback()
                    return "DBOperationError"

                return {
                    "msg": "User created successfully",
                    "status": True,
                    "data": {"company_id": db_company.id},
                }

        try:
            company_json = user_dto.company_details.dict()
            db_company = Company(**company_json)
            session.add(db_company)
            session.commit()
            session.flush()
            session.refresh(db_company)
            user_auth_id = self.registration(
                user_dto,
                email=user_dto.email,
                session=session,
                background_tasks=background_tasks,
            )
            db_user = User(**user_json, company_id=db_company.id, auth_id=user_auth_id)
            session.add(db_user)
            session.commit()
            session.flush()
            session.refresh(db_user)

        except Exception as database_exception:
            session.rollback()
            print(database_exception)
            return "DBOperationError"

        return {
            "msg": "User created successfully",
            "status": True,
            "data": {"company_id": db_company.id},
        }

    def registration(
        self,
        user_dto: UserCreate,
        email: str,
        session: Session,
        background_tasks: BackgroundTasks,
    ):
        temp_password = get_random_password()
        print(f"unhashed password --> {temp_password}")
        # hash the pass word
        url = get_url()
        hashed_password = hash_password(temp_password)
        db_registration = session.exec(
            select(User).filter(User.email == email)
        ).first()
        if user_dto.is_rank_1:
            settings.default_scope = {"scopes": ["counsellor", "rank_one_counsellor"]}
        if db_registration:
            return db_registration.id
        else:
            try:
                db_registration = User(
                    email=email,
                    password=hashed_password,
                    scopes=settings.default_scope,
                )
                # Generate a reset token
                token = secrets.token_urlsafe(32)

                # Set reset token and expiration time for the user
                # db_registration.create_token = token
                # db_registration.create_token_expiration = datetime.utcnow() + timedelta(
                #     hours=1
                # )

                session.add(db_registration)
                session.commit()

                # email_payload = SmsPayload(
                #     email=user_dto.email,
                #     subject="Welcome to Trustool",
                #     message=message_fmt,
                # )
                # background_tasks.add_task(send_sendgrid_email, email_payload)
                return db_registration.id
            except Exception as database_exception:
                session.rollback()
                print(database_exception)
                return "DBOperationError"
            # send password email to user

    def update_password(
        self, user_password_dto: UpdatePassword, user_id: str, session: Session
    ):
        """
        This function updates a password using old password.
        :param user_password_dto: request body
        :param user_id: id of the user.
        :returns: None
        """

        if user_password_dto.old_password == user_password_dto.new_password:
            return "SamePasswordError"
        hash_pass = hash_password(user_password_dto.new_password)
        db_registration = (
            session.query(UserAuthentication)
            .filter(UserAuthentication.user_id == user_id)
            .first()
        )
        if db_registration:
            db_registration.password = hash_pass
        else:
            return "UserNotFound"

    # def create_or_update_verification_code(
    #     self,
    #     generate_code_dto: str,
    #     session: Session,
    #     background_tasks: BackgroundTasks,
    # ):
    #     code = str(random.randint(100000, 999999))

    #     hashed = bcrypt.hashpw(verification_key, bcrypt.gensalt())

    #     db_user = (
    #         session.query(UserAuthentication)
    #         .filter(UserAuthentication.email == generate_code_dto["email"])
    #         .first()
    #     )
    #     print(db_user)
    #     if db_user:
    #         db_user.verification_code = code
    #         db_user.no_of_attempts = 0
    #         session.add(db_user)
    #         session.commit()
    #         print("Your code ", code)
    #         print("email ", db_user.email)

    #         # send password email to user
    #         message_fmt = f"Hello, {db_user.email}, Your verification code is {code}. Please don't share with anyone."

    #         email_payload = SmsPayload(
    #             email=db_user.email,
    #             subject="Verification Code: Counsellor",
    #             message=message_fmt,
    #         )
    #         background_tasks.add_task(send_sendgrid_email, email_payload)
    #     else:
    #         raise HTTPException(
    #             status_code=404,
    #             detail=f"User not found: {generate_code_dto.email}",
    #         )
    #     # return "Otp generated and sent to mail"
    #     return {
    #         "msg": "Otp generated and sent to mail",
    #         "verification_key": hashed,
    #     }

    # def verify_code(
    #     self,
    #     verify_code_dto: VerifyUserCode,
    #     session: Session,
    # ):
    #     db_verification = (
    #         session.query(UserAuthentication)
    #         .filter(UserAuthentication.email == verify_code_dto.email)
    #         .first()
    #     )

    #     users_data = (
    #         session.query(users.User, Company)
    #         .join(Company, Company.id == User.company_id)
    #         .filter(users.User.email == verify_code_dto.email)
    #         .all()
    #     )
    #     # fetching code details based on user_id
    #     if db_verification:
    #         # Check if the user's account is locked
    #         if (
    #             db_verification.account_locked_until
    #             and db_verification.account_locked_until > datetime.now()
    #         ):
    #             raise HTTPException(
    #                 status_code=status.HTTP_403_FORBIDDEN,
    #                 detail=f"Account locked try again after some time.",
    #             )
    #         # check if the verification code matches proper to the code from database.
    #         if (
    #             db_verification.no_of_attempts < self.MAX_OTP_ATTEMPTS
    #             and db_verification.verification_code == verify_code_dto.otp
    #         ):
    #             # OTP is correct, reset the OTP attempts
    #             db_verification.no_of_attempts = 0
    #             session.commit()
    #             user_objects = []
    #             for user in users_data:
    #                 user_objects.append(
    #                     {
    #                         "user_id": user.User.id,
    #                         "company_name": user.Company.name,
    #                         "company_id": user.Company.id,
    #                         "is_rank_1": user.User.is_rank_1,
    #                         "name": user.User.first_name + " " + user.User.last_name,
    #                     }
    #                 )
    #             data = {
    #                 "sub": str(db_verification.id),
    #                 "scopes": db_verification.scopes["scopes"],
    #                 "is_super_admin": db_verification.is_super_admin,
    #                 "user_data": user_objects,
    #             }
    #             access_token = auth_utils.create_access_token(data)
    #             return {"access_token": access_token, "token_type": "bearer"}

    #         else:
    #             # Increment the OTP attempts
    #             db_verification.no_of_attempts += 1
    #             session.commit()
    #             # Check if the maximum attempts have been reached
    #             if db_verification.no_of_attempts >= self.MAX_OTP_ATTEMPTS:
    #                 print("Too many incorrect OTP attempts. Account locked.")
    #                 # Lock the account for one hour
    #                 db_verification.account_locked_until = (
    #                     datetime.now() + self.LOCKOUT_DURATION
    #                 )
    #                 session.commit()
    #                 raise HTTPException(
    #                     status_code=status.HTTP_400_BAD_REQUEST,
    #                     detail="Too many incorrect OTP attempts. Account locked.",
    #                 )
    #             else:
    #                 raise HTTPException(
    #                     status_code=status.HTTP_400_BAD_REQUEST,
    #                     detail="Invalid credientials",
    #                 )
    #     else:
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credientials"
    #         )


user_service = UserService()
