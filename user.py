from auto_complete_data import AutoCompleteData
class User:

    def __init__(self):
        self.string_search = ""

    def run(self):
        while True:
            self.string_search += " " + input(self.string_search + " ")
            if "#" not in self.string_search:
                AutoCompleteData((self.string_search.lower()).split()).find_string()
            else:
                print("The system is ready. Enter your text:")
                self.string_search = ""