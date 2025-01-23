from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import allure

class UI:
    def __init__(self, driver: WebDriver) -> None:
        self.__base_url = "https://www.chitai-gorod.ru/"
        self.__driver = driver

    @allure.step("Открыть сайт")
    def open_page(self):
        """
        				Эта функция открывает сайт Читай Город.
        """
        self.__driver.get(self.__base_url)

    @allure.step("Авторизуемся")
    def auth(self,your_token):
        """
        				Эта функция отправляет в cookie токен для авторизации.
        """
        cookie = {
            "name": "access-token",
            "value": your_token,
            "domain": ".chitai-gorod.ru"
        }
        self.__driver.add_cookie(cookie)
        self.__driver.refresh()
        WebDriverWait(self.__driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    @allure.step("Перейти в профиль пользователя")
    def go_to_profile(self):
        """
        				Эта функция переводит пользователя в его профиль.
        """
        self.__driver.find_element(By.CSS_SELECTOR, "span.header-profile__title").click()
        WebDriverWait(self.__driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.profile-page__user-name")))

    @allure.step("поиск")
    def search(self, search_phrase: str):
        """
        				Эта функция находит окно поиска, вводит запрос и нажимает поиск.
        """
        search_words = self.__driver.find_element(By.NAME, 'phrase')
        search_words.send_keys(search_phrase)
        self.__driver.find_element(By.CLASS_NAME, 'header-search__button-icon').click()

    @allure.step("Закрыть браузер")
    def close_browser(self):
        """
        				Эта функция закрывает браузер
        """
        if self.__driver:
            self.__driver.quit()
            print("Браузер закрыт")

    @allure.step("Возвращает текущую ссылку")
    def get_current_url(self):
        """
        				Эта функция возвращает текущую ссылку браузера
        """
        return self.__driver.current_url

    @allure.step("Ожидание загрузки поиска")
    def wait_search_to_load(self):
        """
        				Эта функция ожидает пока прогрузится поиск
        """
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-title__author"))
        )

    @allure.step("Поиск на странице авторов")
    def find_authors(self):
        """
        				Эта функция находит на странице все элементы с авторами.
        				Выводит длину списка.
        				Если не находит элемент, выводит ошибку.
        """
        authors = self.__driver.find_elements(By.CSS_SELECTOR, "div.product-title__author")
        print(f"Найдено авторов: {len(authors)}")
        for _ in range(3):
            try:
                authors = self.__driver.find_elements(By.CSS_SELECTOR, "div.product-title__author")
                for author in authors:
                    print(author.text)
                break
            except Exception as e:
                print(f"Ошибка при получении элемента: {e}")
        authors = self.__driver.find_elements(By.CSS_SELECTOR, "div.product-title__author")
        assert len(authors) > 0, "Авторы не найдены"

    # @allure.step("Добавить в закладки")??????????????????????????????????
    # def add_to_bookmark(self):?????????????????????????????удалить?
    #     self.__driver.find_elements(By.CSS_SELECTOR, "button.favorite-button.light-blue.favorite-button__adaptive").click()


    @allure.step("Перейти в закладки")
    def go_to_favorite(self):
        """
        				Эта функция переводит пользователя в закладки.
        """
        elements = self.__driver.find_elements(By.CSS_SELECTOR,"span.sticky-header__controls-title")
        elements[1].click()
        element = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.bookmarks-catalog__count")))
        text = element.text
        number = int(text.split("/")[0].strip())
        return number


    @allure.step("Добавить в закладки")
    def add_to_favorite(self):
        """
        				Эта функция добавляет книгу в закладки.
        				Возвращает текущее кол-во книг в закладках
        """
        element = self.__driver.find_element(By.CSS_SELECTOR, "button.button.favorite-button.light-blue.favorite-button__adaptive")
        self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.favorite-button.light-blue.favorite-button__adaptive"))
            )
            element.click()
        except ElementClickInterceptedException:
            self.__driver.execute_script("arguments[0].click();", element)

    @allure.step("убрать из закладок")
    def remove_from_favorite(self):
        """
        				Эта функция убирает книгу из закладки
        """
        element = self.__driver.find_element(By.CSS_SELECTOR,
                                             "button.button.favorite-button.green.favorite-button--active.favorite-button__adaptive")
        self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.button.favorite-button.green.favorite-button--active.favorite-button__adaptive"))
            )
            element.click()
        except ElementClickInterceptedException:
            self.__driver.execute_script("arguments[0].click();", element)

    @allure.step("Принять cookie")
    def cookie(self):
        """
        				Эта функция нажимает принять cookie если видит такой элемент на странице.
        """
        try:
            button = self.__driver.find_element(By.CSS_SELECTOR, "button.button.cookie-notice__button.white")
            button.click()
        except NoSuchElementException:
            pass

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        				Эта функция переводит пользователя в корзину.
        				Возвращает текущее кол-во добавленных книг в корзину
        """
        elements = self.__driver.find_elements(By.CSS_SELECTOR,"span.sticky-header__controls-title")
        elements[2].click()
        element = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.info-item__title")))
        text = element.text
        number = int(text.split(" ")[0].strip())
        return number

    @allure.step("Нажать Купить")
    def add_to_cart(self):
        """
        				Эта функция находит элемент купить и нажимает на него
        """
        element = self.__driver.find_element(By.CSS_SELECTOR, "div.button.action-button.blue")
        self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.button.action-button.blue"))
            )
            element.click()
        except ElementClickInterceptedException:
            self.__driver.execute_script("arguments[0].click();", element)

    @allure.step("Удалить из корзины")
    def remove_from_cart(self):
        """
        				Эта функция удаляет книгу из корзины.
        """
        self.__driver.find_element(By.CSS_SELECTOR, "button.button.cart-item__actions-button.cart-item__actions-button--delete.light-blue").click()

    @allure.step("Нажать оформить")
    def in_cart(self):
        element = self.__driver.find_element(By.CSS_SELECTOR, "div.button.action-button.blue.action-button--in-cart")
        WebDriverWait(self.__driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.action-button__text")))
        text_element = self.__driver.find_element(By.CSS_SELECTOR, "span.action-button__text")
        if text_element.text == "Оформить":
            element.click()

    @allure.step("Перейти к оформлению")
    def go_to_order(self):
        """
        				Эта функция находит элемент перейти к оформлению и нажимает на него
        """
        element = self.__driver.find_element(By.CSS_SELECTOR, "button.button.cart-sidebar__order-button.blue")
        self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.cart-sidebar__order-button.blue"))
            )
            element.click()
        except ElementClickInterceptedException:
            self.__driver.execute_script("arguments[0].click();", element)

    @allure.step("Выбрать магазин")
    def select_store(self):
        """
                				Эта функция находит элемент выбрать магазин.
                				Если не находит по пропускается
         """
        try:
            case_one = self.__driver.find_element(By.CSS_SELECTOR, "button.pvz-default__button.chg-app-button.chg-app-button--primary.chg-app-button--extra-large.chg-app-button--brand-blue")
            self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", case_one)
            WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.pvz-default__button.chg-app-button.chg-app-button--primary.chg-app-button--extra-large.chg-app-button--brand-blue"))
            )
            case_one.click()
        except NoSuchElementException:
            pass

    @allure.step("Выбрать другой магазин")
    def select_another_store(self):
        """
                       Эта функция находит элемент выбрать другой магазин.
        """
        try:
            case_two = self.__driver.find_element(By.CSS_SELECTOR,
                                                  "button.pvz-default__button.chg-app-button.chg-app-button--primary.chg-app-button--extra-large.chg-app-button--brand-blue")
            self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", case_two)

            WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            "button.pvz-default__button.chg-app-button.chg-app-button--primary.chg-app-button--extra-large.chg-app-button--brand-blue"))
            )
            case_two.click()

        except NoSuchElementException:
            print("Элемент не найден.")


    @allure.step("Нажать Заберу отсюда")
    def get_from_here(self):
        """
                       Эта функция находит элемент Заберу отсюда нажимает на него.
        """
        point_button = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button.point-preview__button.chg-app-button.chg-app-button--primary.chg-app-button--small.chg-app-button--brand-blue.gtme-rocket-point-info"))
        )
        point_button.click()

    @allure.step("Заполнить ФИО")
    def fill_name(self, name: str) -> None:
        """
                                 Находит поле ФИО.
                                 Очищает его.
                                 Заполняет данными
                """
        try:
            element = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "name"))
            )
            self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.clear()
            element.send_keys(name)
        except Exception as e:
            print(f"Ошибка при заполнении имени: {e}")


    @allure.step("Заполнить почту")
    def fill_email(self, email: str) -> None:
        """
                                 Находит поле Электронная почта.
                                 Очищает его.
                                 Заполняет данными
                """
        try:
            element = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "email"))
            )
            self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.clear()
            element.send_keys(email)
        except Exception as e:
            print(f"Ошибка при заполнении email: {e}")


    @allure.step("Заполнить номер телефона")
    def fill_phone_number(self, phone: int) -> None:
        """
                         Находит поле Телефон.
                         Очищает его.
                         Заполняет данными
        """
        try:
            element = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "phone"))
            )
            self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            element.clear()
            element.send_keys(str(phone))

        except Exception as e:
            print(f"Ошибка при заполнении телефона: {e}")

    @allure.step("Оформить заказ")
    def create_order(self) -> None:
        """
                               Проверяет что кнопка оформить заказ активна для клика.
        """
        element = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.checkout-summary__button.blue"))
        )
        assert element.is_enabled()

