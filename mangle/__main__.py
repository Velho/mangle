from args import arg_parser, welcome_banner
from parse import get_file_paths, get_function_names, sort_by_count, save_as_csv

from timeit import default_timer as timer

from project import Project
from project_conf import ProjectConf
from function_names import MangleFunctions
from csvbuilder import CSVBuilder

if __name__ == "__main__":
    """Main function to run the script."""
    start = timer()

    welcome_banner()
    args = arg_parser()

    PROJECT_PATH = args.project
    CSV_PATH = args.output

    project = Project(ProjectConf(PROJECT_PATH, CSV_PATH))
    mangle_functions = MangleFunctions(project)

    func_names = mangle_functions.get_function_names(
        sort=mangle_functions.sort_by_count)

    csvbuilder = CSVBuilder(func_names)
    csvbuilder.save_file()

    end = timer()
    print(f"Time: {end - start} seconds")
    #print(f"Parsed: {len(list_of_file_paths)} files")
    #print(f"Found: {len(dictionary_of_functions)} different includes")
