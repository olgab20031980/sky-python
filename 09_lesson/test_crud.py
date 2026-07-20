from crud import (
    create_student,
    get_student_by_id,
    get_student_by_name,
    update_student_name,
    delete_student,
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
