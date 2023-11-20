# pytest

from fastapi.testclient import TestClient
from main import app
from typing import Final

import pytest


# Looks for files names with test_*.py
# $ pytest
# $ pytest -vvl
#
# unittests
def test_basic_example():
    #pass
    assert(True)

#client = TestClient(app)
@pytest.fixture
def client():
    yield TestClient(app) 

@pytest.fixture
def good_request_json():
    return {
        "name": "Product X",
        "quantity": 10,
        "serial_number": "T240",
        "origin": {
            "country": "Ethiopia",
            "production_date": "10th Aug 2000"
        }
    }

@pytest.fixture
def bad_request_json():
    return {
        "name": "Product X",
        "qty": 10,
        "serial_number": "T240",
        "origin": {
            "country": "Ethiopia",
            "production_date": "10th Aug 2000"
        }
    }
    

def test_put_api(client, good_request_json, bad_request_json):
    response = client.put(f"/items/{good_request_json['serial_number']}", json = bad_request_json)
    assert response.status_code == 422, f"Expecting 200 but got {response.status_code}"
    response = client.put(f"/items/{good_request_json['serial_number']}", json=good_request_json)
    assert response.status_code == 200, f"Expecting 200 but got {response.status_code}"


def test_get_api(client, good_request_json, bad_request_json):
    response = client.get(f"/items/{good_request_json['serial_number']}")
    assert response.status_code == 200, f"Expecting 200 but got {response.status_code}"
    assert response.json() == good_request_json


def test_delete_api(client, good_request_json, bad_request_json):
    response = client.delete(f"/items/{good_request_json['serial_number']}")
    assert response.status_code == 200, f"Expecting 200 but got {response.status_code}"
    response = client.get("/items/T240")
    assert response.status_code == 404, f"Expecting 404 but got {response.status_code}"


# -------------------------------------------------------------------------
@pytest.mark.parametrize(
    "item_id, http_code", 
    [('T240', 200),('T2100', 404)]
)

def test_many_get_apis(client, item_id, http_code):
    client.put("/items/T240", json = {
        "name": "Product X",
        "quantity": 10,
        "serial_number": "T240",
        "origin": {
            "country": "Ethiopia",
            "production_date": "10th Aug 2000"
        }
    })
    assert client.get(f"items/{item_id}").status_code == http_code
        
    