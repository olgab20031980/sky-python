import pytest


class TestProjects:

    def test_create_project_positive(self, api_client, project_data):
        response = api_client.create_project(project_data)
        assert response.status_code == 201
        response_data = response.json()
        assert 'id' in response_data

    def test_create_project_negative_no_title(self, api_client):
        invalid_data = {}
        response = api_client.create_project(invalid_data)
        assert response.status_code == 400
        response_data = response.json()
        assert 'message' in response_data

    def test_update_project_positive(self, api_client, created_project):
        if created_project is None:
            pytest.skip("Проект не создан")
        updated_data = {
            "title": "Updated Project"
        }
        response = api_client.update_project(created_project, updated_data)
        assert response.status_code == 200
        response_data = response.json()
        assert 'id' in response_data
        assert response_data['id'] == created_project
        get_response = api_client.get_project(created_project)
        assert get_response.status_code == 200
        get_data = get_response.json()
        assert get_data['title'] == updated_data['title']

    def test_update_project_negative_invalid_id(self, api_client):
        invalid_id = "invalid_id_123"
        update_data = {"title": "Updated Title"}
        response = api_client.update_project(invalid_id, update_data)
        assert response.status_code == 404
        response_data = response.json()
        assert 'message' in response_data

    def test_get_project_positive(self, api_client, created_project):
        if created_project is None:
            pytest.skip("Проект не создан")
        response = api_client.get_project(created_project)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['id'] == created_project
        assert 'title' in response_data

    def test_get_project_negative_invalid_id(self, api_client):
        invalid_id = "invalid_id_123"
        response = api_client.get_project(invalid_id)
        assert response.status_code == 404
        response_data = response.json()
        assert 'message' in response_data
