import openai

from utils.get_token import get_token

def generate_docs_with_chatgpt(prompt, params):
    if params["verbose"]:
        print("\nGPT Model configured: {0}".format(params['gpt_model']))

    print("\nGenerating API docs...")

    openai.api_key = get_token(params)

    response = openai.ChatCompletion.create(
        model=params['gpt_model'],
        messages=prompt,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content.strip()

    return message