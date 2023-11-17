# pytest

from fastapi.testclient import TestClient
from main import app
from typing import Final

# Looks for files names with test_*.py
# $ pytest
# $ pytest -vvl

# unittests
def test_basic_example():
    #pass
    assert(True)

client = TestClient(app)

put_request_json: Final = {
        "name": "Product X",
        "quantity": 10,
        "serial_number": "T240",
        "origin": {
            "country": "Ethiopia",
            "production_date": "10th Aug 2000"
        }
    }

def test_put_api():

    response = client.put("/items/T240", json={
        "name": "Product X",
        "qty": 10,
        "serial_number": "H897",
    })
    assert response.status_code == 422, f"Expecting 200 but got {response.status_code}"

    response = client.put("/items/T240", json=put_request_json)
    assert response.status_code == 200, f"Expecting 200 but got {response.status_code}"

def test_get_api():

    response = client.get("/items/T241")
    assert response.status_code == 404, f"Expecting 404 but got {response.status_code}"

    response = client.get("/items/T240")
    assert response.status_code == 200, f"Expecting 200 but got {response.status_code}"
    #assert response.json() == put_request_json

def test_delete_api():

    response = client.delete("/items/T240")
    assert response.status_code == 200, f"Expecting 200 but got {response.status_code}"

    # confirm item was deleted
    response = client.get("/items/T240")
    assert response.status_code == 404, f"Expecting 404 but got {response.status_code}"



        
    