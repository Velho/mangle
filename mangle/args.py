""" Module to parse the command line arguments.
"""

from argparse import ArgumentParser
from queue import Empty

DEFAULT_PROJECT_PATH = "C:\\Users\\petri\\c\\nginx\\"
DEFAULT_OUTPUT_PATH = (
    "C:\\Users\\petri\\python\\parse-function-names\\function_names.csv"
)
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
    """
    Welcome welcome welcome
    """
    print(f"{DEFAULT_BANNER}")
    print(f"version {VERSION}")


def arg_parser():
    """Public function
    Initializes the parser and
    Returns the arguments if no arguments provided,
    return the help message.
    """
    parser = init_parser()

    args = testing_args(parser)
    if args.test is not None:
        return args

    args = get_args(parser)

    if args is Empty:
        parser.print_help()

    return args


def init_parser():
    """Initializes the argument parser.
    Adds the default parser options,
    -p, --project as the project folder,
    -o, --output as the output csv filename,
    """

    parser = ArgumentParser()
    parser.add_argument(
        "--project",
        "-p",
        help="Input project folder.",
        default=DEFAULT_PROJECT_PATH,
        type=str,
        required=False
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output for the csv, provide the whole folder/file.csv.",
        default=DEFAULT_OUTPUT_PATH,
        type=str,
        required=False
    )

    return parser


def testing_args(parser: ArgumentParser):
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--test')
    group.add_argument('-f', '--file')
    return parser.parse_args()


def get_args(parser):
    """Returns the parsed arguments."""
    return parser.parse_args()
