import configparser
global_config = configparser.ConfigParser()
global_config.read('C:/Users/tumor/OneDrive/Документы/Final_project/Final_project/tests/test_config.ini', encoding='utf-8')


class ConfigProvider:
    def __init__(self) -> None:
        self.config = global_config
        print(self.config.sections())  # Это выведет все секции, которые удалось загрузить из конфигурации

    def get_browser_name(self):
        return self.config["test_ui"].get("browser_name")

    def get_ui_url(self):
        return self.config["test_ui"].get("base_url")

    def get_api_url(self):
        return self.config["tests_api"].get("base_url")
