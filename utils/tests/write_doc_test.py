import os
import pytest

from utils.write_doc import write_documentation

@pytest.fixture
def params():
    return {
        "output_file": "./utils/tests/filename.md"
    }

@pytest.fixture
def response():
    return "Testing..."

def teardown():
    os.remove("./utils/tests/filename.md")

def test_write_documentation(params, response):
    write_documentation(params, response)

    final_text = response + "\n\n*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*"

    file = open("./utils/tests/filename.md", "r")
    text = file.read()
    file.close()

    assert final_text == text 