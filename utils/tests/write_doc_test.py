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

    header = "[![genDocsGPT](https://img.shields.io/badge/Doc%20generated%20by-genDocsGPT-blue)](https://github.com/marco-rosner/genDocsGPT)\n\n"
    footer = "\n\n*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*"

    final_text = header + response + footer

    file = open("./utils/tests/filename.md", "r")
    text = file.read()
    file.close()

    assert final_text == text 