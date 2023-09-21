#!/bin/bash
## genDocsGPT - Generate API documentation in MarkDown based
## in the models and api handlers for given project using ChatGPT.
##
## Usage: bash genDocsGPT.sh
##
## Copyleft 2023 Marco Rosner
##
## https://github.com/marco-rosner/genDocsGPT

# Install pip
python3 -m pip install --upgrade pip

# Install genDocsGPT
python3 -m pip install --upgrade genDocsGPT

# Configure genDocsGPT
# Change the paths for your project 
MODELS="./src/models"
API_HANDLERS="./src/dataSources"
OUTPUT_FILE="./api.md"
# Remenber to create the .env file with API_KEY="chatgpt_api_key"
ENV_FILE="./.env"
GPT_MODEL="gpt-3.5-turbo-16k" # For big projects use gpt-3.5-turbo-16k

# Run genDocsGPT
python3 -m genDocsGPT -v -m $MODELS -a $API_HANDLERS -o $OUTPUT_FILE --env $ENV_FILE --gpt_model $GPT_MODEL