# test_main.py
import pytest
from main import app


@pytest.fixture
def client():
    """
    Pytest fixture that creates a Flask test client from the 'app' in main.py.
    """
    with app.test_client() as client:
        yield client


def test_root_endpoint(client):
    """
    Test the GET '/' endpoint to ensure it returns the greeting and a 200 status code.
    """
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello from my Password Validator!" in resp.data


def test_valid_password(client):
    """
    Test the POST '/v1/checkPassword' endpoint with a valid password.
    A valid password must be at least 8 characters, contain an uppercase letter, a digit, and a special character.
    """
    valid_pw = "Abcdef1!"
    resp = client.post("/v1/checkPassword", json={"password": valid_pw})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data.get("valid") is True
    assert data.get("reason") == ""


def test_invalid_password_too_short(client):
    """
    Test the POST '/v1/checkPassword' endpoint with a password that is too short.
    """
    pw = "Ab1!"
    resp = client.post("/v1/checkPassword", json={"password": pw})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data.get("valid") is False
    assert "at least 8 characters" in data.get("reason")


def test_invalid_password_no_uppercase(client):
    """
    Test the POST '/v1/checkPassword' endpoint with a password missing an uppercase letter.
    """
    pw = "abcdef1!"
    resp = client.post("/v1/checkPassword", json={"password": pw})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data.get("valid") is False
    assert "uppercase letter" in data.get("reason")


def test_invalid_password_no_digit(client):
    """
    Test the POST '/v1/checkPassword' endpoint with a password missing a digit.
    """
    pw = "Abcdefgh!"
    resp = client.post("/v1/checkPassword", json={"password": pw})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data.get("valid") is False
    assert "digit" in data.get("reason")


def test_invalid_password_no_special(client):
    """
    Test the POST '/v1/checkPassword' endpoint with a password missing a special character.
    """
    pw = "Abcdefg1"
    resp = client.post("/v1/checkPassword", json={"password": pw})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data.get("valid") is False
    assert "special character" in data.get("reason")


def test_invalid_password_multiple_errors(client):
    """
    Test the POST '/v1/checkPassword' endpoint with a password that fails multiple criteria.
    For example, a password that is too short and missing an uppercase, digit, and special character.
    """
    pw = "abcdefg"
    resp = client.post("/v1/checkPassword", json={"password": pw})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data.get("valid") is False
    # The error message should include messages about the length, uppercase letter, digit, and special character.
    error_msg = data.get("reason")
    assert "at least 8 characters" in error_msg
    assert "uppercase letter" in error_msg
    assert "digit" in error_msg
    assert "special character" in error_msg
