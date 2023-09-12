from utils.read_files import read_paths

def build_prompt(params):
    prompt = "Generate API documentation with table of contents, models list, JSON and curl examples of them in Swagger style using MarkDown based in these models:\n"
    
    print("Accessing models paths...")
    prompt = prompt + read_paths(params["model_paths"], params["verbose"])

    prompt = prompt + "\n And these handlers: \n"
    
    print("\nAccessing api paths...")
    prompt = prompt + read_paths(params["api_paths"], params["verbose"])

    if params["verbose"]:
        print("\nPrompt content:")
        print(prompt)

    return [{"role": "user", "content": prompt}]