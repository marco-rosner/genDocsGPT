import sys
import getopt

from utils.help import cli_help_interface

def validate_arg(arg, help):
    if arg=="":
        print("{0} is missing. Try -h or --help to use the command correct.".format(help))
        sys.exit(2)

def check_params(args):
    model_paths = ""
    api_paths = ""
    verbose = False

    try:
        opts, args = getopt.getopt(args[1:], "vhm:a:o:", ["verbose", "help", "model=", "api=", "output="])
    except:
        cli_help_interface()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            cli_help_interface()
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-m", "--model"):
            model_paths = arg
        elif opt in ("-a", "--api"):
            api_paths = arg
        elif opt in ("-o", "--output"):
            output_file = arg
    try:
        output_file
    except NameError:
        output_file = "./api.md" # default output file
    
    validate_arg(model_paths, "Model path (-m, --model)")
    validate_arg(api_paths, "Api path (-a, --api)")

    return {
        "model_paths": [model_paths],
        "api_paths": [api_paths],
        "output_file": output_file,
        "verbose": verbose
    }

