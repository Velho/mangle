# Creator   Petri Pihla
# Date      2022-10-30
# License   MIT

from os import walk
import re
from timeit import default_timer as timer

# start timer
start = timer()

PROJECT_PATH = "C:\\Users\\petri\\c\\nginx\\"
list_of_files = []
dictionary_of_functions = {}

for root, dirs, files in walk(PROJECT_PATH):
    for file in files:
        if file.endswith(".c" or ".h"):
            # append file path to list
            list_of_files.append(root + "\\" + file)

for i in list_of_files:
    with open(i, "r") as f:
        for line in f:
            # macth function names
            function = re.search(r"[A-Za-z0-9_]+\(", line)
            if function:
                #remove last character from string
                string = function.group()[:-1]
                # if function name is not in dictionary
                if string not in dictionary_of_functions:
                    # add function name to dictionary
                    dictionary_of_functions[string] = 1
                else:
                    # increment function name in dictionary
                    dictionary_of_functions[string] += 1

# save dictionary to csv file in value order (descending)
with open("C:\\Users\\petri\\python\\parse-function-names\\function_names.csv", "w") as f:
    for key, value in sorted(dictionary_of_functions.items(), key=lambda item: item[1], reverse=True):
        f.write("%s,%s\n" % (key, value))

# stop timer
end = timer()
print("Time: ", end - start, "seconds")
