"""Tests for the GET /activities endpoint"""


def test_get_activities_returns_all_activities(client):
    """Test that GET /activities returns all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 9
    assert "Chess Club" in data
    assert "Programming Class" in data


def test_get_activities_includes_participants(client):
    """Test that each activity includes a participants list"""
    response = client.get("/activities")
    data = response.json()

    assert "participants" in data["Chess Club"]
    assert isinstance(data["Chess Club"]["participants"], list)
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in data["Chess Club"]["participants"]


def test_get_activities_includes_all_required_fields(client):
    """Test that activities include all required fields"""
    response = client.get("/activities")
    data = response.json()

    activity = data["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity


def test_get_activities_empty_participants_list(client):
    """Test that activities with no participants have empty lists"""
    response = client.get("/activities")
    data = response.json()

    assert len(data["Basketball Team"]["participants"]) == 0
    assert len(data["Soccer Team"]["participants"]) == 0


def test_get_activities_response_structure(client):
    """Test the structure of each activity object"""
    response = client.get("/activities")
    data = response.json()

    for activity_name, activity in data.items():
        assert isinstance(activity, dict)
        assert isinstance(activity["description"], str)
        assert isinstance(activity["schedule"], str)
        assert isinstance(activity["max_participants"], int)
        assert isinstance(activity["participants"], list)
