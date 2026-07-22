import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()


class YougileAPI:
    BASE_URL = "https://yougile.com"

    def __init__(self):
        self.token = os.getenv('YOUGILE_TOKEN')
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def create_project(self, data):
        response = requests.post(
            f"{self.BASE_URL}/api-v2/projects",
            json=data,
            headers=self.headers
        )
        return response

    def update_project(self, project_id, data):
        response = requests.put(
            f"{self.BASE_URL}/api-v2/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return response

    def get_project(self, project_id):
        response = requests.get(
            f"{self.BASE_URL}/api-v2/projects/{project_id}",
            headers=self.headers
        )
        return response


@pytest.fixture
def api_client():
    return YougileAPI()


@pytest.fixture
def project_data():
    return {
        "title": "Test Project"
    }


@pytest.fixture
def created_project(api_client, project_data):
    response = api_client.create_project(project_data)
    if response.status_code != 201:
        pytest.skip("Не удалось создать проект для теста")
    project_id = response.json().get('id')
    yield project_id
