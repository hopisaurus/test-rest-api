from app import app


def test_request_example():
    response = app.test_client().get("/")
    resp_test = '{"date": "1666735082","kubernetes": "false","version": "1.0.0"}'
    assert response.status_code == 200
    # assert resp_test in response.data
