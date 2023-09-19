import openai

def generate_docs_with_chatgpt(prompt, token, model="gpt-3.5-turbo"):
    print("\nGenerating API docs...")

    openai.api_key = token

    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content.strip()

    return message