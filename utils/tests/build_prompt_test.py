import os
import pytest

from utils.build_prompt import build_prompt

def setup():
    os.mkdir("./utils/tests/fixtures")
    file = open("./utils/tests/fixtures/fixture.txt", "w")
    file.write("testing...")
    file.close()

@pytest.fixture
def params():
    return {
        "model_paths": ["./utils/tests/fixtures"],
        "api_paths": ["./utils/tests/fixtures"],
        "verbose": False
    }

def teardown():
    os.remove("./utils/tests/fixtures/fixture.txt")
    os.rmdir("./utils/tests/fixtures")

def test_build_prompt(params):
    result = build_prompt(params)

    expected = [{'content': 'Generate API documentation with table of contents, models list, JSON and curl examples of them in Swagger style using MarkDown based in these models:\ntesting...\n And these handlers: \ntesting...', 'role': 'user'}]
    
    assert result == expected