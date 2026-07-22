from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Subject(id={self.id}, name='{self.name}')>"
