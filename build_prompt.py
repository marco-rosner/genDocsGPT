from read_files import read_paths

def build_prompt(params):
    prompt = "Generate API documentation in MarkDown with these models:\n"
    
    print("Accessing models paths...")
    prompt = prompt + read_paths(params["model_paths"])

    prompt = prompt + "\n And these handlers: \n"
    
    print("\nAccessing api paths...")
    prompt = prompt + read_paths(params["api_paths"])

    return [{"role": "user", "content": prompt}]