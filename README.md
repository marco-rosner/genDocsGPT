## Generate Docs using ChatGPT

Script to generate API documentation in MarkDown based in the models and api handlers for given project using ChatGPT.

## ChatGPT API Key

The script demand a ChatGPT API Key that you can generate after create your account in [OpenAI](https://www.openai.com/). Tutorial [here](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt). After this, create a .env file in the following format:

```
API_KEY="chatgpt_api_Key"
```

## Usage

```
genDocsGPT.py [-h] [-v, --verbose] -m / --model <model_paths> -a / --api <api_paths> [-o / --output <filename>]

options:
  -h, --help            show this help message and exit
  -v, --verbose         Show all the messages to debug
  -m / --model <model_paths>
                        Model paths. If more than one, separate with a comma
  -a / --api <api_paths>
                        API paths. If more than one, separate with a comma
  -o / --output <filename>
                        Filename to the documentation generated. Default: ./api.md

We do not recommend using it in non-open-source projects.
```
