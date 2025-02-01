import json

my_file = open('test_data.json')
global_data = json.load(my_file)

class DataProvider:
    def __init__(self) -> None:
        self.data = global_data

    def get(self, prop: str):
        return self.data.get(prop)

