from app.models.base import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel


class CourseBase(SQLModel):
    program: str = Field(max_length=500, nullable=False)
    week_length: int = Field(default=1, nullable=False)
    name: str = Field(max_length=500, nullable=True)
    code: str = Field(max_length=200, nullable=True)
    exam_cert: str = Field(nullable=True)
    tuition: float = Field(nullable=True)
    are_books_included: bool = Field(nullable=True)


class Course(TimestampModel, CourseBase, UUIDModel, table=True):
    __tablename__ = "courses"


class CourseCreate(CourseBase):
    pass
