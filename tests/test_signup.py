"""Tests for the POST /activities/{activity_name}/signup endpoint"""
import pytest


def test_signup_adds_new_participant(client):
    """Test signing up a new participant adds them to the activity"""
    response = client.post(
        "/activities/Basketball%20Team/signup?email=newstudent@mergington.edu"
    )
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]

    # Verify participant was added
    activities_response = client.get("/activities")
    participants = activities_response.json()["Basketball Team"]["participants"]
    assert "newstudent@mergington.edu" in participants


def test_signup_activity_not_found(client):
    """Test signup returns 404 for non-existent activity"""
    response = client.post(
        "/activities/Nonexistent%20Club/signup?email=test@mergington.edu"
    )
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_student_already_registered(client):
    """Test signup returns 400 if student already signed up"""
    response = client.post(
        "/activities/Chess%20Club/signup?email=michael@mergington.edu"
    )
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_signup_multiple_students_same_activity(client):
    """Test multiple students can sign up for the same activity"""
    # First signup
    response1 = client.post(
        "/activities/Art%20Club/signup?email=student1@mergington.edu"
    )
    assert response1.status_code == 200

    # Second signup
    response2 = client.post(
        "/activities/Art%20Club/signup?email=student2@mergington.edu"
    )
    assert response2.status_code == 200

    # Verify both are in the activity
    activities_response = client.get("/activities")
    participants = activities_response.json()["Art Club"]["participants"]
    assert "student1@mergington.edu" in participants
    assert "student2@mergington.edu" in participants


def test_signup_response_message_format(client):
    """Test that signup returns a proper message"""
    response = client.post(
        "/activities/Drama%20Club/signup?email=actor@mergington.edu"
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "actor@mergington.edu" in data["message"]
    assert "Drama Club" in data["message"]


def test_signup_with_different_email_formats(client):
    """Test signup works with various valid email formats"""
    emails = [
        "alice.smith@mergington.edu",
        "bob_jones@mergington.edu",
        "charlie123@mergington.edu"
    ]
    
    for email in emails:
        response = client.post(
            f"/activities/Math%20Club/signup?email={email}"
        )
        assert response.status_code == 200, f"Failed to sign up {email}"


def test_signup_preserves_existing_participants(client):
    """Test that signing up a new student preserves existing participants"""
    # Get initial participants
    initial_response = client.get("/activities")
    initial_chess_participants = initial_response.json()["Chess Club"]["participants"].copy()

    # Sign up a new student to a different activity
    client.post("/activities/Soccer%20Team/signup?email=newsoccer@mergington.edu")

    # Verify Chess Club participants unchanged
    final_response = client.get("/activities")
    final_chess_participants = final_response.json()["Chess Club"]["participants"]
    assert final_chess_participants == initial_chess_participants
