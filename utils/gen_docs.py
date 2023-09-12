import openai
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

openai.api_key = env['API_KEY']

def generate_docs_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    print("\nGenerating API docs...")

    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content.strip()

    return message