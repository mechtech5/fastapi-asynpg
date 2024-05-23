import uuid as uuid_pkg
from typing import Optional, TYPE_CHECKING
from app.models.base import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from .student import Student


class WorkExperienceBase(SQLModel):
    current_work_status: bool = Field(max_length=200, nullable=True)
    other: str = Field(max_length=100, nullable=True)
    most_recent_employer: str = Field(max_length=200, nullable=True)
    position: str = Field(max_length=200, nullable=True)
    dates_employed_from: str = Field(max_length=20, nullable=True)
    brief_description: str = Field(nullable=True)


class WorkExperience(TimestampModel, WorkExperienceBase, UUIDModel, table=True):
    __tablename__ = "work_experience"

    student_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="students.uuid"
    )
    student: Optional["Student"] = Relationship(back_populates="work_experience")


class WorkExperienceCreate(WorkExperienceBase):
    pass
