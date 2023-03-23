
class ProjectConf:
    def __init__(self, project_path, csv_path):
        self.project_path = project_path
        self.csv_path = csv_path

    def get_project_path(self):
        return self.project_path

    def get_output_path(self):
        return self.csv_path