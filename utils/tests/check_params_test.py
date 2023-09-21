import pytest

from utils.check_params import check_params

@pytest.fixture
def args():
    return ['genDocsGPT.py', '-m', '../lightweight-go-server/models', '-a', '../lightweight-go-server/gin']

@pytest.fixture
def args_t():
    return ['genDocsGPT.py', '-v', '-m', '../lightweight-go-server/models', '-a', '../lightweight-go-server/gin', '-t', 'token']

@pytest.fixture
def args_e():
    return ['genDocsGPT.py', '-v', '-m', '../lightweight-go-server/models', '-a', '../lightweight-go-server/gin', '--env', './.genDocsGPT']

@pytest.fixture
def args_m():
    return ['genDocsGPT.py', '-v', '-m', '../lightweight-go-server/models', '-a', '../lightweight-go-server/gin', '--gpt_model', 'gpt_model']

@pytest.fixture
def args_o():
    return ['genDocsGPT.py', '-v', '-m', '../lightweight-go-server/models', '-a', '../lightweight-go-server/gin', '-o', 'filename.md']

@pytest.fixture
def args_verbose():
    return ['genDocsGPT.py', '--verbose', '--model', '../lightweight-go-server/models', '--api', '../lightweight-go-server/gin', '--output', 'filename.md']

@pytest.fixture
def args_f():
    return ['genDocsGPT.py', '-X']

def test_check_params(args):
    result = check_params(args)

    assert result["model_paths"] == ["../lightweight-go-server/models"]
    assert result["api_paths"] == ["../lightweight-go-server/gin"]
    assert result["output_file"] == "./api.md"
    assert result["env_file"] == "./.env"
    assert result["gpt_model"] == "gpt-3.5-turbo"
    assert result["token"] == ""
    assert result["verbose"] == False

def test_check_params_token(args_t):
    result = check_params(args_t)

    assert result["model_paths"] == ["../lightweight-go-server/models"]
    assert result["api_paths"] == ["../lightweight-go-server/gin"]
    assert result["output_file"] == "./api.md"
    assert result["token"] == "token"
    assert result["gpt_model"] == "gpt-3.5-turbo"
    assert result["verbose"] == True

def test_check_params_env_file(args_e):
    result = check_params(args_e)

    assert result["model_paths"] == ["../lightweight-go-server/models"]
    assert result["api_paths"] == ["../lightweight-go-server/gin"]
    assert result["output_file"] == "./api.md"
    assert result["env_file"] == "./.genDocsGPT"
    assert result["token"] == ""
    assert result["gpt_model"] == "gpt-3.5-turbo"
    assert result["verbose"] == True

def test_check_params_gpt_model(args_m):
    result = check_params(args_m)

    assert result["model_paths"] == ["../lightweight-go-server/models"]
    assert result["api_paths"] == ["../lightweight-go-server/gin"]
    assert result["output_file"] == "./api.md"
    assert result["env_file"] == "./.env"
    assert result["token"] == ""
    assert result["gpt_model"] == "gpt_model"
    assert result["verbose"] == True

def test_check_params_output_file(args_o):
    result = check_params(args_o)

    assert result["model_paths"] == ["../lightweight-go-server/models"]
    assert result["api_paths"] == ["../lightweight-go-server/gin"]
    assert result["output_file"] == "filename.md"
    assert result["env_file"] == "./.env"
    assert result["token"] == ""
    assert result["gpt_model"] == "gpt-3.5-turbo"
    assert result["verbose"] == True

def test_check_params_verbose(args_verbose):
    result = check_params(args_verbose)

    assert result["model_paths"] == ["../lightweight-go-server/models"]
    assert result["api_paths"] == ["../lightweight-go-server/gin"]
    assert result["output_file"] == "filename.md"
    assert result["env_file"] == "./.env"
    assert result["token"] == ""
    assert result["gpt_model"] == "gpt-3.5-turbo"
    assert result["verbose"] == True

def test_check_params_fail(args_f):
    with pytest.raises(SystemExit) as pytest_wrapped_e: check_params(args_f)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2