from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get(
        url="/",
        headers={"accept": "application/json"}
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Hello!"}


def test_read_item_info_endpoint_m1():
    response = client.get(
        url="/api/-1",
        headers={"accept": "application/json"}
    )

    assert response.status_code == 400

def test_read_item_info_endpoint_1():
    response = client.get(
        url="/api/1",
        headers={"accept": "application/json"}
    )

    exp_resp = {'item_name': 'item_1', 'price': 8.8, 'username': None}

    assert response.status_code == 200
    assert response.json() == exp_resp


def test_create_item_endpoint_neg_price():
    response = client.post(
        url="/items/",
        headers={"Content-Type": "application/json"},
        json={"price": -1, "item_name": "item"}
    )

    assert response.status_code == 400


def test_create_item_endpoint_price():
    response = client.post(
        url="/items/",
        headers={"Content-Type": "application/json"},
        json={"price": 1, "item_name": "item"}
    )

    assert response.status_code == 200
    assert response.json()["price"] == 0.8