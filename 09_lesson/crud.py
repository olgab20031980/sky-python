from sqlalchemy.orm import Session
from models import Student


def create_student(db: Session, name: str) -> Student:
    db_student = Student(name=name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_student_by_id(db: Session, student_id: int) -> Student | None:
    return db.query(Student).filter(Student.id == student_id).first()


def get_student_by_name(db: Session, name: str) -> Student | None:
    return db.query(Student).filter(Student.name == name).first()


def update_student_name(
    db: Session, student_id: int, new_name: str
) -> Student | None:
    db_student = get_student_by_id(db, student_id)
    if db_student:
        db_student.name = new_name
        db.commit()
        db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int) -> bool:
    db_student = get_student_by_id(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    return False
