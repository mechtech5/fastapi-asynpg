from typing import Optional, TYPE_CHECKING
from app.models.base import TimestampModel, UUIDModel
from pydantic import EmailStr
from sqlmodel import AutoString, Field, SQLModel, Relationship


if TYPE_CHECKING:
    from .institutional import Institutional
    from .citizenship import Citizenship
    from .emergency_contact import EmergencyContact
    from .work_experience import WorkExperience
    from .survey import Survey

9


class StudentBase(SQLModel):
    first_name: str = Field(max_length=200, nullable=True)
    last_name: str = Field(max_length=200, nullable=False)
    email: EmailStr = Field(nullable=False, unique=True, index=True, sa_type=AutoString)
    street_address: str = Field(max_length=200, nullable=True)
    city: str = Field(max_length=200, nullable=True)
    state_province: str = Field(max_length=200, nullable=True)
    zip_postalcode: str = Field(max_length=200, nullable=True)
    country: str = Field(max_length=200, nullable=True)
    home_phone: str = Field(max_length=200, nullable=True)
    cell_phone: str = Field(max_length=200, nullable=True)
    is_high_school_graduate: bool = Field(nullable=True)
    school_name: str = Field(max_length=200, nullable=True)
    school_state: str = Field(max_length=200, nullable=True)
    school_dates: str = Field(max_length=200, nullable=True)


class Student(TimestampModel, StudentBase, UUIDModel, table=True):
    __tablename__ = "students"

    citizenship: Optional["Citizenship"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="student"
    )
    survey: Optional["Survey"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="student"
    )
    work_experience: Optional["WorkExperience"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="student"
    )
    institutional: Optional["Institutional"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="student"
    )
    emgergency_contacts: list["EmergencyContact"] = Relationship(
        back_populates="student"
    )


class StudentCreate(StudentBase):
    pass
