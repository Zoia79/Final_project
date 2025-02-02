from Final_project.page.API import API
from configuration.ConfiProvider import ConfigProvider
from configuration.DataProvider import DataProvider
import allure


@allure.title("Поиск на кириллице")
@allure.story("API")
@allure.severity("normal")
def test_search_in_cyrillic():
    url = ConfigProvider().get_api_url()
    token = DataProvider().get("token")
    cyrillic_phrase = DataProvider().get("cyrillic_phrase")
    api = API(url, token)
    response = api.search_request(cyrillic_phrase)
    assert response is not None, "Ошибка запроса"
    assert response.status_code == 200, \
        f"Ошибка: ожидался статус код 200, но получен {response.status_code}"
    data = response.json()
    print("Тест пройден успешно, получен статус код 200.")
    print(data)


@allure.title("Поиск на латинице")
@allure.story("API")
@allure.severity("normal")
def test_search_in_latin():
    url = ConfigProvider().get_api_url()
    token = DataProvider().get("token")
    latin_phrase = DataProvider().get("latin_phrase")
    api = API(url, token)
    response = api.search_request(latin_phrase)
    assert response is not None, "Ошибка запроса"
    assert response.status_code == 200, \
        f"Ошибка: ожидался статус код 200, но получен {response.status_code}"
    data = response.json()
    print("Тест пройден успешно, получен статус код 200.")
    print(data)


@allure.title("Поиск по пустому запросу")
@allure.story("API")
@allure.severity("trivial")
def test_search_empty_request():
    url = ConfigProvider().get_api_url()
    token = DataProvider().get("token")
    empty_phrase = DataProvider().get("empty_phrase")
    api = API(url, token)
    response = api.search_request_negative(empty_phrase)
    assert response.status_code == 400, \
        f"Ожидался код 400, но получен {response.status_code}"
    print("Тест прошел успешно (код 400)")


@allure.title("Поиск через другой метод")
@allure.story("API")
@allure.severity("trivial")
def test_search_wrong_method():
    url = ConfigProvider().get_api_url()
    token = DataProvider().get("token")
    wrong_method_phrase = DataProvider().get("wrong_method_phrase")
    api = API(url, token)
    response = api.search_request_with_post(wrong_method_phrase)
    if response and response.status_code == 405:
        print("Тест прошел успешно (код 405)")
        return
    assert response is not None, "API вернул None вместо ответа"
    assert response.status_code == 405, \
        f"Ожидался код 405, но получен {response.status_code}"


@allure.title("Поиск по иероглифу")
@allure.story("API")
@allure.severity("trivial")
def test_search_by_hieroglyph():
    url = ConfigProvider().get_api_url()
    token = DataProvider().get("token")
    hieroglyph_phrase = DataProvider().get("hieroglyph_phrase")
    api = API(url, token)
    response = api.search_request_negative(hieroglyph_phrase)
    assert response.status_code == 422, \
        f"Ожидался код 422, но получен {response.status_code}"
    print("Тест прошел успешно (код 422)")
