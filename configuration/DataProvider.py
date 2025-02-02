import os
import json


file_path = os.path.join(os.path.dirname(__file__),
                         "..", "tests", "test_data.json")


if not os.path.exists(file_path):
    raise FileNotFoundError(
        f"Файл {file_path} не найден! Убедитесь, что он существует.")

with open(file_path, encoding="utf-8") as my_file:
    global_data = json.load(my_file)

class DataProvider:
    def __init__(self) -> None:
        self.data = global_data

    def get(self, prop: str):
        return self.data.get(prop)
