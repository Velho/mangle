# Module to parse the command line arguments.

from argparse import ArgumentParser
from queue import Empty

DEFAULT_PROJECT_PATH = "C:\\Users\\petri\\c\\nginx\\"
DEFAULT_OUTPUT_PATH = "C:\\Users\\petri\\python\\parse-function-names\\function_names.csv"
VERSION = 0.1

DEFAULT_BANNER = """
#     #    #    #     #  #####  #       ####### ######
##   ##   # #   ##    # #     # #       #       #     #
# # # #  #   #  # #   # #       #       #       #     #
#  #  # #     # #  #  # #  #### #       #####   ######
#     # ####### #   # # #     # #       #       #   #
#     # #     # #    ## #     # #       #       #    #
#     # #     # #     #  #####  ####### ####### #     #
"""


def welcome_banner():
    print(f"{DEFAULT_BANNER}")
    print(f"Welcome to mangler v.{VERSION}")


def arg_parser():
    parser = init_parser()
    args = get_args(parser)

    if args is Empty:
        parser.print_help()

    return args

# Initializes the argument parser.


def init_parser():
    parser = ArgumentParser()
    parser.add_argument('--project', '-p', help='Input project folder.',
                        default=DEFAULT_PROJECT_PATH, type=str)
    parser.add_argument(
        '--output', '-o', help='Output for the csv, provide the whole folder/file.csv.', default=DEFAULT_OUTPUT_PATH, type=str)

    return parser

# Parse the arguments.


def get_args(parser):
    return parser.parse_args()
