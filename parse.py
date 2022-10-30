# Creator   Petri Pihla
# Date      2022-10-30
# License   MIT

"""
This script parses all .c and .h files in the given directory tree.
It then saves the function names and their count as a csv file.
"""

import re
from os import walk
from timeit import default_timer as timer


def get_file_paths(path):
    """Returns a list of all file paths in the given directory tree."""
    list_of_file_paths = []
    for (dirpath, dirnames, filenames) in walk(path):
        for filename in filenames:
            if filename.endswith(".c") or filename.endswith(".h"):
                list_of_file_paths.append(dirpath + "\\" + filename)
    return list_of_file_paths


def get_function_names(filepaths):
    """Returns a dictionary of function names and their count."""
    for filepath in filepaths:
        with open(filepath, "r") as file:
            for line in file:
                function = re.findall(r"[A-Za-z0-9_]+\(", line)
                if function:
                    if function.__len__() > 1:
                        for f in function:
                            string = f[:-1]
                            if string in dictionary_of_functions:
                                dictionary_of_functions[string] += 1
                            else:
                                dictionary_of_functions[string] = 1
                    else:
                        string = function.pop()[:-1]
                        if string in dictionary_of_functions:
                            dictionary_of_functions[string] += 1
                        else:
                            dictionary_of_functions[string] = 1
    return dictionary_of_functions


def save_as_csv(filepaths, dictionary):
    """Saves the dictionary as a csv file."""
    with open("function_names.csv", "w") as file:
        file.write("Function name, Count\n")
        for key, value in dictionary.items():
            file.write(f"{key}, {value}\n")


def sort_by_count(dictionary):
    """Sorts the dictionary by the count of the function names."""
    sorted_dict = dict(
        sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    )
    return sorted_dict


if __name__ == "__main__":
    """Main function to run the script."""
    start = timer()

    PROJECT_PATH = "C:\\Users\\petri\\c\\nginx\\"

    CSV_PATH = "C:\\Users\\petri\\python\\parse-function-names\\function_names.csv"

    list_of_file_paths = []
    dictionary_of_functions = {}

    list_of_file_paths = get_file_paths(PROJECT_PATH)
    get_function_names(list_of_file_paths)
    dictionary_of_functions = sort_by_count(dictionary_of_functions)
    sort_by_count(dictionary_of_functions)
    save_as_csv(CSV_PATH, dictionary_of_functions)

    end = timer()
    print(f"Time: {end - start} seconds")
    print(f"Parsed: {len(list_of_file_paths)} files")
    print(f"Found: {len(dictionary_of_functions)} different functions")
