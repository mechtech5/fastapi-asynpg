from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from models.student import Student, StudentBase
from models.course import Course, CourseBase
from models.emergency_contact import *
from models.institutional import *

# from models.survey import *
from models.work_experience import *
from models.citizenship import *
from models.student import *
from models.course import *
from typing import List, Union
import uuid as uuid_pkg
from fastapi import APIRouter, Depends, HTTPException, status
from crud.user import UsersCRUD, get_users_crud
from core.db import get_async_session
from models.student import *
from sqlalchemy.orm import Session


admission_router = APIRouter()


# @admission_router.post("/students-admission", response_model=AdmissionResponse)
# async def create_student(student: Studentcreate,
#                         course: CourseCreate,
#                         citizenship: CitizenshipCreate,
#                         emergency_contact: EmergencyCreate,
#                         work_experience: WorkExperienceCreate,
#                         survey: SurveyCreate,
#                         instituional: InstitutionalCreate,
#                         db: Session = Depends(get_async_session)):

#     try:
#         new_student = Student(**student.dict())
#         db.add(new_student)

#         new_course = Course(**course.dict())
#         db.add(new_course)

#         # # Create Citizenship entity
#         # new_citizenship = Citizenship(**citizenship.dict())
#         # db.add(new_citizenship)

#         # # Create Emergency Contact entity
#         # new_emergency_contact = Emgergency_contact(**emergency_contact.dict())
#         # db.add(new_emergency_contact)

#         # # Create Work Experience entity
#         # new_work_experience = Work_experience(**work_experience.dict())
#         # db.add(new_work_experience)

#         # # Create Survey entity
#         # new_survey = Survey(**survey.dict())
#         # db.add(new_survey)

#         # # Create Institutional entity
#         # new_institutional = Institutional(**instituional.dict())
#         # db.add(new_institutional)

#         # Commit the session to persist all changes
#         await db.commit()

#         # Refresh the session to get the latest state of the entities
#         await db.refresh(new_student)
#         await db.refresh(new_course)
#         # await db.refresh(new_citizenship)
#         # await db.refresh(new_emergency_contact)
#         # await db.refresh(new_work_experience)
#         # await db.refresh(new_survey)
#         # await db.refresh(new_institutional)

#         # Return a response indicating success
#         return {
#             "message": "Student Adimission data added successfully",
#             "student": new_student,
#             "course": new_course,
#             # "citizenship": new_citizenship,
#             # "emergency_contact": new_emergency_contact,
#             # "work_experience": new_work_experience,
#             # "survey": new_survey,
#             # "institutional": new_institutional
#         }
#     except Exception as e:
#                 raise HTTPException(status_code=500, detail="An error occurred while creating the Student Adimission data.")
