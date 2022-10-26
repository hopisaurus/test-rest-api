from app import app


def test_request_example():
    response = app.test_client().get("/")
    # resp_test = '{"date": "1666735082","kubernetes": "false","version": "1.0.0"}'
    assert response.status_code == 200
    # assert resp_test in response.data


def test_history():
    response = app.test_client().get("/history")
    assert response.status_code == 200


def test_lookup_validate():
    # test post call /v1/lookup/validate
    response = app.test_client().post("/v1/lookup/validate", json={"ip": "0.0.0.0"})
    assert response.status_code == 200
