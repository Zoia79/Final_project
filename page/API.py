import requests
from urllib.parse import quote_plus


class API:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def search_request(self, phrase):
        """
         Эта функция отправляет GET запрос.
         Возвращает ответ или выводит текст об ошибке.
        :param phrase:
        :return:
        """
        try:
            url = f"{self.base_url}api/v2/search/product"
            params = {
                "phrase": phrase,
                "customerCityId": 198,
                "products[page]": 1,
                "products[per-page]": 48,
                "sortPreset": "relevance"
            }
            response = requests.get(url, headers=self.headers, params=params)

            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None

    def search_request_with_post(self, phrase):
        """
        Отправляет POST-запрос для семантического поиска и возвращает ответ.
        Если статус-код 405, то не вызывает исключение.
        :param phrase: Фраза для поиска.
        :return: Ответ сервера.
        """
        url = f"{self.base_url}api/v1/recommend/semantic"
        data = {"phrase": phrase, "perPage": 48}
        try:
            response = requests.post(url, headers=self.headers, json=data, timeout=10)
            if response.status_code == 405:
                return response
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return None


    def search_request_negative(self, phrase):
        """
        Отправляет GET-запрос.
        """
        url = f"{self.base_url}api/v2/search/product"
        params = {
            "phrase": phrase,
            "customerCityId": 198,
            "products[page]": 1,
            "products[per-page]": 48,
            "sortPreset": "relevance"
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response



