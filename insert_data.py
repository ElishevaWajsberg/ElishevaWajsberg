import json
import os
import re
from databace import Database

class InsertData:
    data_base = Database()

    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self, file):
        with open(file, encoding="utf8") as current_file:
            file_data = current_file.readlines()
            return file_data

    def insert_data_to_DB(self):
        print("Loading the files and preparing the system...")
        for root, dirs, files in os.walk(self.file_path):
            for f in files:
                data_file = self.read_data(os.path.join(root, f))
                for line in data_file:
                    for word in line.split():
                        InsertData.data_base.insert((re.sub('[!@#$%^&*().,;:/?><"\']', "", word.lower())), (line, line.find(word), os.path.join(root, f)))
        print("The system is ready. Enter your text:")







