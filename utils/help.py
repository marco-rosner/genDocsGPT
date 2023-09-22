import argparse

def cli_help_interface():
    parser=argparse.ArgumentParser(
        prog='genDocsGPT',
        description='''CLI to generate API documentation in MarkDown based on the models and api handlers for given project using ChatGPT.''',
        epilog="""We do not recommend using it in non-open-source projects.""")
    parser.add_argument('-v, --verbose', metavar='', help='Show all the messages to debug')
    parser.add_argument('-m / --model', metavar='<model_paths>', required=True, type=str, help='Model paths. If more than one, separate with a comma')
    parser.add_argument('-a / --api', metavar='<api_paths>', required=True, type=str, help='API paths. If more than one, separate with a comma')
    parser.add_argument('-o / --output', metavar='<filename>',type=str, default="./api.md", help='Filename to the documentation generated. Default: ./api.md')
    parser.add_argument('-t / --token', metavar='<token>',type=str, help='ChatGPT API KEY')
    parser.add_argument('--env', metavar='<filename>',type=str, default="./.env", help='Env file that MUST and ONLY have API_KEY="chatgpt_api_key". Default: ./.env')
    parser.add_argument('--gpt_model', metavar='<model>',type=str, default="gpt-3.5-turbo", help='Model that will be used by ChatGPT. Default: gpt-3.5-turbo')
    parser.parse_args()