import openai
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

openai.api_key = env['API_KEY']

def generate_docs_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        max_tokens=4_000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content.strip()

    return message