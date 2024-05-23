import uuid as uuid_pkg
from typing import Optional, TYPE_CHECKING
from app.models.base import TimestampModel, UUIDModel
from pydantic import EmailStr
from sqlmodel import AutoString, Field, SQLModel, Relationship


if TYPE_CHECKING:
    from .student import Student


class EmergencyContactBase(SQLModel):
    first_name: str = Field(max_length=200, nullable=True)
    last_name: str = Field(max_length=200, nullable=False)
    email: EmailStr = Field(nullable=False, unique=True, index=True, sa_type=AutoString)
    street_address: str = Field(max_length=200, nullable=True)
    city: str = Field(max_length=200, nullable=True)
    state_province: str = Field(max_length=200, nullable=True)
    zip_postalcode: str = Field(max_length=200, nullable=True)
    country: str = Field(max_length=200, nullable=True)
    home_phone: Optional[str] = Field(max_length=200, nullable=True)
    cell_phone: Optional[str] = Field(max_length=200, nullable=True)
    relationship: str = Field(max_length=200, nullable=True)


class EmergencyContact(TimestampModel, EmergencyContactBase, UUIDModel, table=True):
    __tablename__ = "emergency_contacts"

    student_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="students.uuid"
    )
    student: Optional["Student"] = Relationship(back_populates="emergency_contacts")


class EmergencyCreate(EmergencyContactBase):
    pass
