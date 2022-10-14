from app import app


def test1():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test2():
    response = app.test_client().get("/tony")
    assert response.status_code == 200


def test3():
    response = app.test_client().get("/tony")
    assert b"AVENGERS ASSEMBLE" in response.data
