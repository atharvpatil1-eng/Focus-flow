from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from ..database import Base
from ..main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "This is a test task", "status": "todo"},
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data
    assert data["status"] == "todo"

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0 # assuming previous test ran and created one

def test_update_task():
    # Create a task to update
    create_response = client.post(
        "/tasks/",
        json={"title": "Task to Update", "status": "todo"},
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Updated Task", "status": "in_progress"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["status"] == "in_progress"

def test_delete_task():
    # Create a task to delete
    create_response = client.post(
        "/tasks/",
        json={"title": "Task to Delete", "status": "todo"},
    )
    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    # Verify it's gone
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
