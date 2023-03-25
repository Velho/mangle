import re
from c_function import Function


class Tokenizer:
    def __init__(self, file_content):
        self.content = file_content

    def parse_functions(self):
        """
        Parse all functions from the content and return the functions
        """
        functions = []
        fn_filter = r'\b[a-zA-Z]+\s+\w+\s*\(\s*\)\s*{'
        # match = re.findall(fn_filter, self.content)
        for match in re.finditer(fn_filter, self.content):
            functions.append(Function(*match.group().split()[0:2]))

        return functions
