import os
import pytest

from utils.read_files import read_paths, read_file

def setup():
    os.mkdir("./utils/tests/fixtures")
    file = open("./utils/tests/fixtures/fixture.txt", "w")
    file.write("testing...")
    file.close()

@pytest.fixture
def paths():
    return ["./utils/tests/fixtures"]

def teardown():
    os.remove("./utils/tests/fixtures/fixture.txt")
    os.rmdir("./utils/tests/fixtures")

def test_read_paths(paths, verbose=False):
    result = read_paths(paths, verbose)

    file = open(paths[0] + "/fixture.txt", "r")
    text = file.read()
    file.close()

    assert result == text

def test_read_file_with_path(paths, verbose=False):
    result = read_file(paths[0], verbose)

    file = open(paths[0] + "/fixture.txt", "r")
    text = file.read()
    file.close()

    assert result != text

def test_read_file_with_filename(paths, verbose=False):
    result = read_file(paths[0] + "/fixture.txt", verbose)

    file = open(paths[0] + "/fixture.txt", "r")
    text = file.read()
    file.close()

    assert result == text