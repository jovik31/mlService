import pandas as pd
# import postgresql_client to get file path from database
#
# file_path = problem_directory/file_name


class File:

    def __init__(self, file_name):
        self.file_name = file_name
        # self.file_path = sql.query(file_name)

    def load_file_csv(self):

        data_frame = pd.read_csv(self.file_name)
        return data_frame

    def save_file_csv(self):
