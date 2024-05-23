import uuid as uuid_pkg
from typing import Optional, TYPE_CHECKING

from app.models.base import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel, Relationship


if TYPE_CHECKING:
    from .student import Student


class InstitutionalBase(SQLModel):
    hear_about_ntai: str = Field(max_length=200, nullable=True)
    recommended_by: bool = Field(nullable=True)
    if_yes: str = Field(max_length=200, nullable=True)
    agency_name: str = Field(max_length=200, nullable=True)
    counselor_name: str = Field(max_length=200, nullable=True)
    desired_dates: str = Field(max_length=200, nullable=True)
    courses_interested: str = Field(max_length=200, nullable=True)
    list_certifications: str = Field(max_length=200, nullable=True)
    institutional_name: str = Field(max_length=200, nullable=True)
    institutional_phone: str = Field(max_length=200, nullable=True)


class Institutional(TimestampModel, InstitutionalBase, UUIDModel, table=True):
    __tablename__ = "institutional"

    student_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="students.uuid"
    )
    student: Optional["Student"] = Relationship(back_populates="institution")


class InstitutionalCreate(InstitutionalBase):
    pass
