import uuid as uuid_pkg
from typing import Optional, TYPE_CHECKING
from app.models.base import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from .student import Student


class CitizenshipBase(SQLModel):
    social_security_number: str = Field(max_length=200, nullable=True)
    dob: str = Field(max_length=20, nullable=False)
    gender: str = Field(max_length=20, nullable=False)
    country_of_citizenship: str = Field(max_length=200, nullable=False)
    place_of_birth: str = Field(max_length=200, nullable=False)
    alien_number: str = Field(max_length=200, nullable=True)
    is_english_native_language: bool = Field(nullable=True)
    other_languages: str = Field(max_length=200, nullable=True)


class Citizenship(TimestampModel, CitizenshipBase, UUIDModel, table=True):
    __tablename__ = "citizenship"

    student_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="students.uuid"
    )
    student: Optional["Student"] = Relationship(back_populates="citizenship")


class CitizenshipCreate(CitizenshipBase):
    pass
