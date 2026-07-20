from crud import (
    create_student,
    get_student_by_id,
    get_student_by_name,
    update_student_name,
    delete_student,
    create_subject,
    get_subject_by_id,
    get_subject_by_name,
    update_subject_name,
    delete_subject,
)


class TestStudentCRUD:
    def test_create_student(self, db_session):
        student_name = "Alice"
        new_student = create_student(db_session, student_name)
        assert new_student.id is not None
        assert new_student.name == student_name
        found_student = get_student_by_name(db_session, student_name)
        assert found_student is not None
        assert found_student.id == new_student.id

    def test_update_student(self, db_session):
        original_name = "Bob"
        new_name = "Robert"
        student = create_student(db_session, original_name)
        updated_student = update_student_name(db_session, student.id, new_name)
        assert updated_student is not None
        assert updated_student.name == new_name
        from_db = get_student_by_id(db_session, student.id)
        assert from_db is not None
        assert from_db.name == new_name
        old_student = get_student_by_name(db_session, original_name)
        assert old_student is None

    def test_delete_student(self, db_session):
        student_name = "Charlie"
        student = create_student(db_session, student_name)
        student_id = student.id
        is_deleted = delete_student(db_session, student_id)
        assert is_deleted is True
        from_db = get_student_by_id(db_session, student_id)
        assert from_db is None
        by_name = get_student_by_name(db_session, student_name)
        assert by_name is None

    def test_delete_nonexistent_student(self, db_session):
        is_deleted = delete_student(db_session, 99999)
        assert is_deleted is False


class TestSubjectCRUD:
    def test_create_subject(self, db_session):
        subject_name = "Mathematics"
        new_subject = create_subject(db_session, subject_name)
        assert new_subject.id is not None
        assert new_subject.name == subject_name
        found_subject = get_subject_by_name(db_session, subject_name)
        assert found_subject is not None
        assert found_subject.id == new_subject.id

    def test_update_subject(self, db_session):
        original_name = "Physics"
        new_name = "Advanced Physics"
        subject = create_subject(db_session, original_name)
        updated_subject = update_subject_name(db_session, subject.id, new_name)
        assert updated_subject is not None
        assert updated_subject.name == new_name
        from_db = get_subject_by_id(db_session, subject.id)
        assert from_db is not None
        assert from_db.name == new_name
        old_subject = get_subject_by_name(db_session, original_name)
        assert old_subject is None

    def test_delete_subject(self, db_session):
        subject_name = "Chemistry"
        subject = create_subject(db_session, subject_name)
        subject_id = subject.id
        is_deleted = delete_subject(db_session, subject_id)
        assert is_deleted is True
        from_db = get_subject_by_id(db_session, subject_id)
        assert from_db is None
        by_name = get_subject_by_name(db_session, subject_name)
        assert by_name is None

    def test_delete_nonexistent_subject(self, db_session):
        is_deleted = delete_subject(db_session, 99999)
        assert is_deleted is False
