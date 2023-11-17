# pytest

from fastapi.testclient import TestClient
from main import app

# Looks for files names with test_*.py
# $ pytest
# $ pytest -vvl

# unittests
def test_basic_example():
    #pass
    assert(True)

client = TestClient(app)

def test_put_api():
    response = client.put("/items/T240", json={
        "name": "Product X",
        "quantity": 10,
        "serial_number": "H897",
        "origin": {
            "country": "Ethiopia",
            "production_date": "10th Aug 2000"
        }
    })
    assert response.status_code == 200
    


