import sys

from check_params import check_params
from gen_docs import generate_docs_with_chatgpt

if __name__ == "__main__":
    check_params(sys.argv)
    
    user_prompt = {"role": "user", "content": "Generate a api docs on MarkDown"}

    chatbot_reponse = generate_docs_with_chatgpt([user_prompt])

    print(chatbot_reponse)
