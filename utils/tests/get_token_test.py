import os
import pytest

from utils.get_token import get_token

def setup():
    os.mkdir("./utils/tests/fixtures")
    file = open("./utils/tests/fixtures/.env", "w")
    file.write("API_KEY='token'")
    file.close()

@pytest.fixture
def token():
    return {
        "token": "key",
    }

@pytest.fixture
def params():
    return {
        "env_file": "./utils/tests/fixtures/.env",
        "token": ""
    }

def teardown():
    os.remove("./utils/tests/fixtures/.env")
    os.rmdir("./utils/tests/fixtures")

def test_get_token(token):
    result = get_token(token)
    
    assert result == "key"

def test_get_token_file(params):
    result = get_token(params)
    
    assert result == "token"