import configparser

global_config = configparser.ConfigParser()
global_config.read('test_config.ini', encoding='utf-8')

class ConfigProvider:
    def __init__(self) -> None:
        self.config = global_config

    def get_browser_name(self):
        return self.config["test_ui"].get("browser_name")

    def get_ui_url(self):
        return self.config["test_ui"].get("base_url")

    def get_api_url(self):
        return self.config["tests_api"].get("base_url")

