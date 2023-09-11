import sys
import getopt

def validate_arg(arg, help):
    if arg=="":
        print("{0} is missing. Try --help to use the command correct.".format(help))
        sys.exit(2)

def check_params(args):
    model_path = ""
    api_path = ""
    help = "{0} -m <model_path> -a <api_path> -o <output_file>".format(args[0])

    try:
        opts, args = getopt.getopt(args[1:], "hm:a:o:", ["help", "model=", "api=", "output="])
    except:
        print(help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit(2)
        elif opt in ("-m", "--model"):
            model_path = arg
        elif opt in ("-a", "--api"):
            api_path = arg
        elif opt in ("-o", "--output"):
            output_file = arg
    try:
        output_file
    except NameError:
        output_file = "./api.md" # default output file
    
    validate_arg(model_path, "Model path (-m, --model)")
    validate_arg(api_path, "Api path (-a, --api)")

    print('model_path:', model_path)
    print('api_path:', api_path)
    print('output_file:', output_file )

    # read the path and send the blob to ChatGPT

