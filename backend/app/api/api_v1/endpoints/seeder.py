# from faker import Faker
# from faker.providers import BaseProvider
# from db.database import get_session
# from fastapi import APIRouter, Depends
# from typing import List
# from sqlmodel import Session
# from pydantic import BaseModel
# from models import UserRead, User, UserCreate
# from models.company_options import CompanyOptions, CompanyOptionsSeed
# from utils import auth_utils
# from models import UserBase

# faker = Faker()
# seeder_router = APIRouter()


# # @seeder_router.get("/user")
# # def create_user_seeder(
# #     *,
# #     number: int,
# #     session: Session = Depends(get_session),
# #     current_user: UserBase = Depends(auth_utils.get_current_user),
# # ):
# #     for i in range(number):
# #         fake_user = UserCreate(
# #             first_name=faker.first_name(),
# #             last_name=faker.last_name(),
# #             phone=faker.phone_number(),
# #             email=faker.ascii_safe_email(),
# #             password="$2a$12$Q0PMVwnoZ2GK7Tl/M9t4OOhBitB2IQWzwly.pl4Q8y36CW9nxrUpK",  # secret
# #         )
# #         db_user = User.from_orm(fake_user)
# #         session.add(db_user)
# #     session.commit()
# #     return "Database Seeded"


# @seeder_router.post("/company_options")
# def seed_company_options(
#     *,
#     session: Session = Depends(get_session),
#     company_options: CompanyOptionsSeed,
#     # current_user: UserBase = Depends(auth_utils.get_current_user),
# ):
#     report_about = [
#         ("undesirable_behaviour", "Aggression/Violence", "Agressie/geweld"),
#         ("undesirable_behaviour", "Bullying", "Pesten"),
#         (
#             "undesirable_behaviour",
#             "Discrimination: Gender/ Orientation",
#             "Discriminatie: geslacht/oriëntatie",
#         ),
#         ("undesirable_behaviour", "Discrimination: Belief", "Discriminatie: geloof"),
#         (
#             "undesirable_behaviour",
#             "Discrimination: Color/ Origin",
#             "Discriminatie: kleur/Afkomst",
#         ),
#         (
#             "undesirable_behaviour",
#             "Discrimination (unspecified)",
#             "Discriminatie (niet gespecificeerd)",
#         ),
#         ("undesirable_behaviour", "Sexual harassment", "Seksuele intimidatie"),
#         ("undesirable_behaviour", "Intimidation / Threat", "Intimidatie/bedreiging"),
#         ("integrity", "Fraud / Theft", "Fraude / Diefstal"),
#         ("integrity", "Information leakage", "Lekken van informatie"),
#         ("integrity", "Conflict of interest", "Belangenverstrengeling"),
#         ("integrity", "Corruption", "Corruptie"),
#         ("integrity", "Abuse of company assets", "Misbruik van bedrijfsmiddelen"),
#         (
#             "integrity",
#             "Violation of law / internal policy",
#             "Overtreding van wet/intern beleid",
#         ),
#         ("others", "Other", "Anders"),
#     ]

#     report_against = [
#         ("reporter_view", "Supervisor", "Leidinggevende", ["STANDARD"]),
#         ("reporter_view", "Colleague", "Collega", ["STANDARD"]),
#         ("reporter_view", "Customer", "Klant", ["STANDARD"]),
#         ("reporter_view", "Guest", "Gast", ["STANDARD"]),
#         ("reporter_view", "Supplier", "Leverancier", ["STANDARD"]),
#         ("reporter_view", "Other member", "Lid Vereniging/club", ["SPORT"]),
#         ("reporter_view", "Trainer/coach", "Trainer/coach", ["SPORT"]),
#         ("reporter_view", "Employee", "Werknemer", ["SPORT"]),
#         ("reporter_view", "Volunteer", "Vrijwilliger", ["SPORT"]),
#         (
#             "reporter_view",
#             "Board/commission member",
#             "Bestuur/ commissielid",
#             ["SPORT"],
#         ),
#         ("reporter_view", "Other", "Anders", ["STANDARD", "SPORT"]),
#     ]

#     position = [
#         ("reporter_view", "Employee", "Werknemer", ["STANDARD", "SPORT"]),
#         ("reporter_view", "Self-Employed professional", "ZZP-er", ["STANDARD"]),
#         ("reporter_view", "Temp", "Uitzendkracht", ["STANDARD"]),
#         ("reporter_view", "Trainee", "Stagiaire", ["STANDARD"]),
#         ("reporter_view", "Supplier", "Leverancier", ["STANDARD"]),
#         ("reporter_view", "Customer", "Klant", ["STANDARD"]),
#         ("reporter_view", "Member", "Lid Vereniging/club", ["SPORT"]),
#         ("reporter_view", "Trainer/coach", "Trainer/coach", ["SPORT"]),
#         ("reporter_view", "Volunteer", "Vrijwilliger", ["SPORT"]),
#         ("reporter_view", "Guest", "Gast", ["SPORT"]),
#         ("reporter_view", "Other", "Anders", ["STANDARD", "SPORT"]),
#     ]

#     for item in report_against:
#         payload = {
#             "group": company_options.group,
#             "data_type": "report_against",
#             "value_type": item[0],
#             "value_en": item[1],
#             "value_nl": item[2],
#             "version": item[3],
#         }
#         db_company_options = CompanyOptions(**payload)
#         session.add(db_company_options)

#     for item in position:
#         payload = {
#             "group": company_options.group,
#             "data_type": "position",
#             "value_type": item[0],
#             "value_en": item[1],
#             "value_nl": item[2],
#             "version": item[3],
#         }
#         db_company_options = CompanyOptions(**payload)
#         session.add(db_company_options)

#     session.commit()
#     return "Database Seeded"
