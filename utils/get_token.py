import os
import sys

def get_token(params):
    if params["token"] != "":
        return params["token"]

    if os.path.isfile(params["env_file"]):
        text_file = open(params["env_file"], "r")

        text = text_file.read()

        text_file.close()

        return text[9:-1]
    
    print("Make sure that the {0} file exist and has only API_KEY='chatgpt_api_key' in it.".format(params["env_file"]))
    print("For more information about how to configure API_KEY: genDocsGPT -h")
    sys.exit(2)