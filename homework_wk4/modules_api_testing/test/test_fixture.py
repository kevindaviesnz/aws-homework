# texting_fixture.py
# fixtures - preconditioning using fixtures
from typing import Final
# pip3 install black
import pytest

from fastapi.testclient import TestClient
from main import app

# install Python Indent extension
# install black formatter exention
# settngs -> search format - choose python indent
#             search format on save

# fixture is a pre-condition - init and return

# everytime we call client() we create a new client
@pytest.fixture
def client():
    yield TestClient(app)    

# health check

@pytest.fixture
def good_payload():
    return {
        "name": "Product X",
        "quantity": 10,
        "serial_number": "T240",
        "origin": {
            "country": "Ethiopia",
            "production_date": "10th Aug 2000"
        }
    }
    
@pytest.fixture # required otherwise get bad_payload not found
def bad_payload():
    return {
        "name": "Product X",
        "qty": 10,
        "serial_number": "T240",
        "origin": {
            "country": "Ethiopia",
            "production_date": "10th Aug 2000"
        }
    } 
    
@pytest.fixture
def create_and_delete_item(good_payload):
    client.put("/items/", json=good_payload)
    yield "Item created"
    client.delete(f"items/{good_payload.serial_number}")

def test_incorrect_put_api(client, bad_payload):
    response = client.put("/items/T240", json=bad_payload)
    assert response.status_code == 422, f"Expecting 200 but got {response.status_code}"

def test_get_api(client, good_payload):
    # client is a fresh client
    response = client.get(f"/items/T240")
    assert response.status_code == 404, f"Expecting 404 but got {response.status_code}"
    #assert response.json() == good_payload

def test_put_then_get_api(client, good_payload):
    response = client.put("items/T240", json=good_payload)
    assert response.status_code == 200
    response = client.get(f"items/T240")
    assert response.status_code == 200 and response.json() == good_payload
    
# Use to do multiple test cases
@pytest.mark.parametrize(
# first test case a=1, b=2, expected = 3    
# second test case a=5, b=-1, expected = 4    
    "a, b, expected",
    [
        (1,2,3),
        (5, -1, 4),
        (3,3,6)
    ],
)
def test_addition(a, b, expected):
    assert a + b == expected
    
@pytest.mark.parametrize(
    "payload, http_code", 
    [
        (
            {
                "name": "Product X",
                "quantity": 10,
                "serial_number": "T240",
                "origin": {
                    "country": "Ethiopia",
                    "production_date": "10th Aug 2000"
                }
            }, 
            200
        ),
        (
            {
                "name": "Product X",
                "qty": 10,
                "serial_number": "T240",
                "origin": {
                    "country": "Ethiopia",
                    "production_date": "10th Aug 2000"
                }
            },
            422
        )
    ],
    #indirect=["payload"] # indirectly saynig we're evaluation the good payload and bad payload
)
def test_many_put_apis(client, payload, http_code):
     assert client.put("items/T240", json=payload).status_code == http_code