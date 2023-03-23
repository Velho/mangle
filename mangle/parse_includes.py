# Creator   Petri Pihla
# Date      2022-10-30
# License   MIT

"""
This script parses all .c and .h files in the given directory tree.
It then saves the function names and their count as a csv file.
"""

import re
from os import walk


def get_file_paths(path):
    """Returns a list of all file paths in the given directory tree."""
    list_of_file_paths = []
    for dirpath, dirnames, filenames in walk(path):
        for filename in filenames:
            if filename.endswith(".c") or filename.endswith(".h"):
                list_of_file_paths.append(dirpath + "\\" + filename)
    return list_of_file_paths


# TODO: shold be split into smaller functions for better readability
def get_function_names(filepaths):
    """Returns a dictionary of function names and their count."""
    dictionary_of_includes = {}
    for filepath in filepaths:
        with open(filepath, "r") as file:
            for line in file:
                # regex include "#include stdio.h" and "#include "stdio.h""
                if line.startswith("#include"):
                    if line.startswith("#include <"):
                        include = re.findall(r"#include\s*<(.*)>", line)[0]
                    else:
                        include = re.findall(r"#include\s*\"(.*)\"", line)[0]
                    if include in dictionary_of_includes:
                        dictionary_of_includes[include] += 1
                    else:
                        dictionary_of_includes[include] = 1
                # function = re.findall(r"#include <[A-Za-z0-9_]+\.h>", line)
                # if function:
                #    string = function[0]
                #    if string in dictionary_of_includes:
                #        dictionary_of_includes[string] += 1
                #    else:
                #        dictionary_of_includes[string] = 1
    return dictionary_of_includes


def save_as_csv(filepaths, dictionary):
    """Saves the dictionary as a csv file."""
    with open("includes_names.csv", "w") as file:
        file.write("File name, Count\n")
        for key, value in dictionary.items():
            file.write(f"{key}, {value}\n")


def sort_by_count(dictionary):
    """Sorts the dictionary by the count of the function names."""
    sorted_dict = dict(
        sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    )
    return sorted_dict
