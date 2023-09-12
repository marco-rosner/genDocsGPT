import sys

from check_params import check_params
from gen_docs import generate_docs_with_chatgpt
from build_prompt import build_prompt
from write_doc import write_documentation

if __name__ == "__main__":
    params = check_params(sys.argv)
    
    prompt = build_prompt(params)
    
    chatgpt_response = generate_docs_with_chatgpt(prompt)

    write_documentation(params["output_file"], chatgpt_response)

    print("API documentation generated")
