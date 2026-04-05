"""Pytest configuration and fixtures for API tests"""
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test"""
    initial_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Practice and compete in basketball games",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": []
        },
        "Soccer Team": {
            "description": "Train and play soccer matches",
            "schedule": "Mondays and Wednesdays, 3:00 PM - 4:30 PM",
            "max_participants": 22,
            "participants": []
        },
        "Art Club": {
            "description": "Explore various art forms and create masterpieces",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 10,
            "participants": []
        },
        "Drama Club": {
            "description": "Act in plays and improve public speaking",
            "schedule": "Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": []
        },
        "Debate Club": {
            "description": "Engage in debates and critical thinking exercises",
            "schedule": "Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": []
        },
        "Math Club": {
            "description": "Solve math problems and participate in competitions",
            "schedule": "Mondays, 3:30 PM - 4:30 PM",
            "max_participants": 25,
            "participants": []
        }
    }

    # Clear and reset the activities dictionary
    activities.clear()
    activities.update(initial_activities)

    yield
