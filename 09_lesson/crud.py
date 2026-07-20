from sqlalchemy.orm import Session
from models import Student, Subject


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


def create_subject(db: Session, name: str) -> Subject:
    db_subject = Subject(name=name)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject


def get_subject_by_id(db: Session, subject_id: int) -> Subject | None:
    return db.query(Subject).filter(Subject.id == subject_id).first()


def get_subject_by_name(db: Session, name: str) -> Subject | None:
    return db.query(Subject).filter(Subject.name == name).first()


def update_subject_name(
    db: Session, subject_id: int, new_name: str
) -> Subject | None:
    db_subject = get_subject_by_id(db, subject_id)
    if db_subject:
        db_subject.name = new_name
        db.commit()
        db.refresh(db_subject)
    return db_subject


def delete_subject(db: Session, subject_id: int) -> bool:
    db_subject = get_subject_by_id(db, subject_id)
    if db_subject:
        db.delete(db_subject)
        db.commit()
        return True
    return False
