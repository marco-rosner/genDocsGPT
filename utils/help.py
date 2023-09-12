import argparse

def cli_help_interface():
    parser=argparse.ArgumentParser(
        description='''Script to generate API documentation in MarkDown based in the models and api handlers for given project using ChatGPT.''',
        epilog="""We do not recommend using it in non-open-source projects.""")
    parser.add_argument('-v, --verbose', metavar='', help='Show all the messages to debug')
    parser.add_argument('-m / --model', metavar='<model_paths>', required=True, type=str, help='Model paths. If more than one, separate with a comma')
    parser.add_argument('-a / --api', metavar='<api_paths>', required=True, type=str, help='API paths. If more than one, separate with a comma')
    parser.add_argument('-o / --output', metavar='',type=str, default="./api.md", help='Filename to the documentation generated. Default: ./api.md')
    parser.parse_args()