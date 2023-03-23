from project_conf import ProjectConf
from os import walk

class Project:
    def __init__(self, confs : ProjectConf):
        self.confs = confs

    def __get_file_paths(self):
        """Returns a list of all file paths in the given directory tree."""
        list_of_file_paths = []
        for (dirpath, _, filenames) in walk(self.confs.get_project_path()):
            for filename in filenames:
                if filename.endswith(".c") or filename.endswith(".h"):
                    list_of_file_paths.append(dirpath + "\\" + filename)
        return list_of_file_paths