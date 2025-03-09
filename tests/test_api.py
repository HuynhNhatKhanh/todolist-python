import requests
import pytest

BASE_URL = "http://localhost:8000"

# Test the root endpoint
def test_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Test creating a new task
def test_create_task():
    task_data = {"title": "Test Task", "description": "This is a test task"}
    response = requests.post(f"{BASE_URL}/task", json=task_data)
    assert response.status_code == 200
    assert "id" in response.json()
    
# Test listing all tasks
def test_list_tasks():
    response = requests.get(f"{BASE_URL}/task")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test retrieving a specific task by ID
def test_get_task():
    task_data = {"title": "Sample Task", "description": "Sample task description"}
    create_response = requests.post(f"{BASE_URL}/task", json=task_data)
    assert create_response.status_code == 200
    task_id = create_response.json()["id"]

    response = requests.get(f"{BASE_URL}/task/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Sample Task"

# Test updating an existing task
def test_update_task():
    task_data = {"title": "Task to Update", "description": "Initial description"}
    create_response = requests.post(f"{BASE_URL}/task", json=task_data)
    assert create_response.status_code == 200
    task_id = create_response.json()["id"]

    update_data = {"title": "Updated Task", "description": "Updated description"}
    response = requests.put(f"{BASE_URL}/task/{task_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

# Test deleting a task
def test_delete_task():
    task_data = {"title": "Task to Delete", "description": "Will be deleted"}
    create_response = requests.post(f"{BASE_URL}/task", json=task_data)
    assert create_response.status_code == 200
    task_id = create_response.json()["id"]

    response = requests.delete(f"{BASE_URL}/task/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted successfully"}
