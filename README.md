[![genDocsGPT](https://img.shields.io/pypi/v/genDocsGPT.svg)](https://pypi.org/project/genDocsGPT/) [![Python Versions](https://img.shields.io/badge/Python-3.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11-blue)](https://www.python.org) [![Test workflow](https://github.com/marco-rosner/genDocsGPT/actions/workflows/test.yml/badge.svg)](https://github.com/marco-rosner/genDocsGPT/actions/workflows/test.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![genDocsGPT](https://github.com/marco-rosner/genDocsGPT/raw/main/resources/genDocsGPT.png?raw=true "genDocsGPT")

## Generate Docs using ChatGPT

CLI to generate API documentation in MarkDown based on the models and api handlers for given project using ChatGPT.

## genDocsGPT badge

[![genDocsGPT](https://img.shields.io/badge/Docs%20generated%20by-genDocsGPT-blue)](https://github.com/marco-rosner/genDocsGPT)

## ChatGPT API Key

The genDosGPT demand a ChatGPT API Key that you can generate after create your free account in [OpenAI](https://www.openai.com/). Tutorial [here](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt). After this, create a `.env` file in the following format:

```
API_KEY="chatgpt_api_Key"
```

## Usage

```
usage: genDocsGPT [-h] [-v, --verbose] -m / --model <model_paths> -a / --api <api_paths> 
[-o / --output <filename>] [-t / --token <token>] [--env <filename>] [--gpt_model <model>]

CLI to generate API documentation in MarkDown based on the models and api handlers for 
given project using ChatGPT.

options:
  -h, --help            show this help message and exit
  -v, --verbose         Show all the messages to debug
  -m / --model <model_paths>
                        Model paths. If more than one, separate with a comma
  -a / --api <api_paths>
                        API paths. If more than one, separate with a comma
  -o / --output <filename>
                        Filename to the documentation generated. Default: ./api.md
  -t / --token <token>  ChatGPT API KEY
  --env <filename>      Env file that MUST and ONLY have API_KEY="chatgpt_api_key". 
                        Default: ./.env
  --gpt_model <model>   Model that will be used by ChatGPT. Default: gpt-3.5-turbo

We do not recommend using it in non-open-source projects.
```

### Standalone

![genDocsGPT](https://github.com/marco-rosner/genDocsGPT/raw/main/resources/genDocsGPT-standalone.png?raw=true "genDocsGPT")

The [genDocsGPT.sh](https://github.com/marco-rosner/genDocsGPT/blob/main/usage/Standalone/genDocsGPT.sh), the bash script above, should be used in projects where the documentation should be generated not frequently. You only need to copy this file, **change the configuration** (models, API handlers…), paste it into your project, create the .env file with the ChatGPT API Key, and run this bash script.

I am using this standalone version in the [DadosJusBr’s GraphQL](https://github.com/marco-rosner/dadosjusbr-graphql) project which is a Node/ExpressJS using Apollo Server. So, I created a script in the [package.json](https://github.com/marco-rosner/dadosjusbr-graphql/blob/main/package.json) to run it only using: `npm run genDocsGPT` or `yarn genDocsGPT`

### GitHub Action

![genDocsGPT](https://github.com/marco-rosner/genDocsGPT/raw/main/resources/genDocsGPT-gh-action.png?raw=true "genDocsGPT")

This GitHub Action will run after every commit in the main/master branch and create a pull request that you only need to approve (or not) and the documentation will be updated.

For [genDocsGPT.yml](https://github.com/marco-rosner/lightweight-go-server/blob/main/.github/workflows/genDocsGPT.yml) works fine in your project, you should set the model, API handlers paths, and other options ([line 30](https://github.com/marco-rosner/lightweight-go-server/blob/main/.github/workflows/genDocsGPT.yml#L30)), create, in the GitHub, the secret **ChatGPT_API_KEY** ([_tutorial here_](https://docs.github.com/pt/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)), and change the workflow permissions ([_tutorial here_](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-default-github_token-permissions)) to “**Read and Write permissions**” and use the “**Allow GitHub Action to create and approve pull requests**”.

![genDocsGPT](https://github.com/marco-rosner/genDocsGPT/raw/main/resources/genDocsGPT-permissions.png?raw=true "Workflow permissions after the changes needed")

For more detail, I integrated this GitHub Action in the [Lightweight Go Server](https://github.com/marco-rosner/lightweight-go-server) project, a [Go servers benchmark between Echo, Gin, and Fiber](https://blog.stackademic.com/go-servers-benchmark-echo-fiber-and-gin-caadd9a78319).