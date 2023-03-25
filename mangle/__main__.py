from timeit import default_timer as timer

from args import arg_parser, welcome_banner
from parse import get_file_paths, get_function_names, save_as_csv, sort_by_count


def mangle_cli(args):
    start = timer()

    # welcome_banner()
    # args = arg_parser()

    PROJECT_PATH = args.project
    CSV_PATH = args.output

    list_of_file_paths = []
    dictionary_of_functions = {}

    list_of_file_paths = get_file_paths(PROJECT_PATH)
    dictionary_of_functions = get_function_names(list_of_file_paths)
    dictionary_of_functions = sort_by_count(dictionary_of_functions)
    sort_by_count(dictionary_of_functions)
    save_as_csv(CSV_PATH, dictionary_of_functions)

    end = timer()
    print(f"Time: {end - start} seconds")
    print(f"Parsed: {len(list_of_file_paths)} files")
    print(f"Found: {len(dictionary_of_functions)} different includes")


from tokenizer import Tokenizer


if __name__ == "__main__":
    """Main function to run the script."""

    welcome_banner()
    args = arg_parser()

    if args.test is None and args.file is None:
        mangle_cli(args)
        exit()

    # testing tokenizer
    with open(args.file) as f:
        tokenizer = Tokenizer(f.read())
        ret = tokenizer.parse_functions()

        for function in ret:
            print(f'{function}')
