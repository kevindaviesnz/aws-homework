# texting_fixture.py
# fixtures
from typing import Final
# pip3 install black
import pytest

from fastapi.testclient import TestClient
from main import app

# fixture is a pre-condition - init and return

client = TestClient(app)

# health check

put_request_json: Final = {
        "name": "Product X",
        "quantity": 10,
        "serial_number": "T240",
        "origin": {
            "country": "Ethiopia",
            "production_date": "10th Aug 2000"
        }
    }

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
