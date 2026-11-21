from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "Application is running"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_workouts():
    client = app.test_client()
    response = client.get("/workouts")

    assert response.status_code == 200
    assert "workouts" in response.json
    assert len(response.json["workouts"]) > 0


def test_members():
    client = app.test_client()
    response = client.get("/members")

    assert response.status_code == 200
    assert "members" in response.json
    assert len(response.json["members"]) == 2
    assert response.json["members"][0]["name"] == "Member One"
    assert response.json["members"][0]["membership"] == "Premium"
