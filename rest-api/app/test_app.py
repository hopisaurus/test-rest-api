import pytest

from app import app


def test_request_example():
    response = app.test_client().get("/")
    assert response.status_code == 200
    # assert '{"date": "1666735082","kubernetes": "false","version": "1.0.0"}' in response.data