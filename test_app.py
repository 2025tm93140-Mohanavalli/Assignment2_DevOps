
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "Application is running"
    assert response.json["version"] == "2.1"

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["version"] == "2.1"

def test_workouts():
    client = app.test_client()
    response = client.get("/workouts")
    assert response.status_code == 200
    assert "workouts" in response.json
    assert len(response.json["workouts"]) == 3

def test_members():
    client = app.test_client()
    response = client.get("/members")

    assert response.status_code == 200
    assert "members" in response.json
    assert len(response.json["members"]) == 2
    assert response.json["members"][0]["name"] == "Member One"
    assert response.json["members"][0]["membership"] == "Premium"

def test_get_single_workout():
    client = app.test_client()
    response = client.get("/workouts/1")

    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["name"] == "Strength Training"
    assert response.json["category"] == "Strength"
    assert response.json["difficulty"] == "Intermediate"

def test_invalid_workout():
    client = app.test_client()
    response = client.get("/workouts/999")

    assert response.status_code == 404
    assert response.json["error"] == "Workout not found"
