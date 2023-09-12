import sys

from utils.check_params import check_params
from utils.gen_docs import generate_docs_with_chatgpt
from utils.build_prompt import build_prompt
from utils.write_doc import write_documentation

if __name__ == "__main__":
    params = check_params(sys.argv)
    
    prompt = build_prompt(params)
    
    chatgpt_response = generate_docs_with_chatgpt(prompt)

    write_documentation(params, chatgpt_response)
