## Generate Docs using ChatGPT

Script to generate API documentation in MarkDown based in the models and api handlers for given project using ChatGPT.

## ChatGPT API Key

The script demand a ChatGPT API Key that you can generate after create your account in [OpenAI](https://www.openai.com/). Tutorial [here](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt). After this, create a .env file in the following format:

```
API_KEY="chatgpt_api_Key"
```

## How to use

The command have the params:

  * model_path (-m, --model) **REQUIRED** - The path that will be used to read the models used by the API
  * api_path (-a, --api) **REQUIRED** - The path that will be used to read the api handlers
  * output_file (-o, --output) - The path to the file that will be created with the MarkDown documentation. Default value is `./api.md`.
  * help (-h, --help) - The help instructions.