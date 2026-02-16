import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    response = client.post("/api/tasks/", {"title": "CI/CD"})
    assert response.status_code == 201
