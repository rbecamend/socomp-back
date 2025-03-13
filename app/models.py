from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Student(SQLModel, table=True):
    student_id: int = Field(nullable=False, default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    email: str = Field(nullable=False, index=True)
    registration_number: str = Field(nullable=False, unique=True, index=True)

    history: List["StudentHistory"] = Relationship(back_populates="student")
class Area(SQLModel, table=True):
    area_id: int = Field(nullable=False, default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True, index=True)
    description: str

    subjects: List["AreaSubject"] = Relationship(back_populates="area")
    professors: List["ProfessorArea"] = Relationship(back_populates="area")
    laboratories: List["LaboratoryArea"] = Relationship(back_populates="area")

class Subject(SQLModel, table=True):
    subject_id: int = Field(nullable=False, default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True, index=True)
    description: str

    areas: List["AreaSubject"] = Relationship(back_populates="subject")
    professors: List["SubjectProfessor"] = Relationship(back_populates="subject")
    students: List["StudentHistory"] = Relationship(back_populates="subject")

class Professor(SQLModel, table=True):
    professor_id: int = Field(nullable=False, default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True, index=True)
    email: str = Field(nullable=False, index=True)

    areas: List["ProfessorArea"] = Relationship(back_populates="professor")
    subjects: List["SubjectProfessor"] = Relationship(back_populates="professor")
    laboratories: List["LaboratoryProfessor"] = Relationship(back_populates="professor")

class Laboratory(SQLModel, table=True):
    laboratory_id: int = Field(nullable=False, default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True, index=True)
    description: str

    areas: List["LaboratoryArea"] = Relationship(back_populates="laboratory")
    professors: List["LaboratoryProfessor"] = Relationship(back_populates="laboratory")

    # many-to-many relations

class StudentHistory(SQLModel, table=True):
    student_history_id: int = Field(nullable=False, default=None, primary_key=True)
    student_id: int = Field(nullable=False, index=True, foreign_key="student.student_id")
    subject_id: int = Field(nullable=False, index=True, foreign_key="subject.subject_id")
    grade: str

    student: Optional[Student] = Relationship(back_populates="history")
    subject: Optional[Subject] = Relationship(back_populates="students")

class AreaSubject(SQLModel, table=True):
    area_id: int = Field(nullable=False, foreign_key="area.area_id", primary_key=True)
    subject_id: int = Field(nullable=False, foreign_key="subject.subject_id", primary_key=True)

    area: Optional[Area] = Relationship(back_populates="subjects")
    subject: Optional[Subject] = Relationship(back_populates="areas")

class ProfessorArea(SQLModel, table=True):
    professor_id: int = Field(nullable=False, foreign_key="professor.professor_id", primary_key=True)
    area_id: int = Field(nullable=False, foreign_key="area.area_id", primary_key=True)

    professor: Optional[Professor] = Relationship(back_populates="areas")
    area: Optional[Area] = Relationship(back_populates="professors")

class SubjectProfessor(SQLModel, table=True):
    subject_id: int = Field(nullable=False, foreign_key="subject.subject_id", primary_key=True)
    professor_id: int = Field(nullable=False, foreign_key="professor.professor_id", primary_key=True)

    subject: Optional[Subject] = Relationship(back_populates="professors")
    professor: Optional[Professor] = Relationship(back_populates="subjects")

class LaboratoryArea(SQLModel, table=True):
    laboratory_id: int = Field(nullable=False, foreign_key="laboratory.laboratory_id", primary_key=True)
    area_id: int = Field(nullable=False, foreign_key="area.area_id", primary_key=True)

    laboratory: Optional[Laboratory] = Relationship(back_populates="areas")
    area: Optional[Area] = Relationship(back_populates="laboratories")

class LaboratoryProfessor(SQLModel, table=True):
    laboratory_id: int = Field(nullable=False, foreign_key="laboratory.laboratory_id", primary_key=True)
    professor_id: int = Field(nullable=False, foreign_key="professor.professor_id", primary_key=True)

    laboratory: Optional[Laboratory] = Relationship(back_populates="professors")
    professor: Optional[Professor] = Relationship(back_populates="laboratories")
