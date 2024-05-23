import uuid as uuid_pkg
from typing import Optional, TYPE_CHECKING
from app.models.base import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from .student import Student


class SurveyBase(SQLModel):
    enroll_at_ntai: str = Field(max_length=200, nullable=True)
    your_time_here: bool = Field(max_length=200, nullable=True)
    nondiscriminatory: bool = Field(nullable=True)
    other: str = Field(max_length=200, nullable=True)


class Survey(TimestampModel, SurveyBase, UUIDModel, table=True):
    __tablename__ = "survey"

    student_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="students.uuid"
    )
    student: Optional["Student"] = Relationship(back_populates="survey")


class SurveyCreate(SurveyBase):
    pass
