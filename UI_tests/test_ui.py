from Final_project.page.UI import UI
from selenium.webdriver.support.ui import WebDriverWait


my_token = "Ваш токен"
search_by = "Достоевский"
name = "Your Name"
email = "your@mail.com"
phone_number = "746732438"


def test_auth(browser):
    ui = UI(browser)
    ui.open_page()
    ui.auth(my_token)
    ui.go_to_profile()
    print(ui.get_current_url())
    assert ui.get_current_url().endswith("profile/")
    ui.close_browser()

def test_find_books_by_author(browser):
    ui = UI(browser)
    ui.open_page()
    ui.search(search_by)
    ui.wait_search_to_load()
    ui.find_authors()
    ui.close_browser()

def test_add_book_to_bookmark(browser):
    ui = UI(browser)
    ui.open_page()
    ui.auth(my_token)
    before = ui.go_to_favorite()
    ui.search(search_by)
    ui.wait_search_to_load()
    ui.cookie()
    ui.add_to_favorite()
    after = ui.go_to_favorite()
    assert before < after
    ui.remove_from_favorite()
    ui.close_browser()

def test_add_book_to_cart(browser):
    ui = UI(browser)
    ui.open_page()
    ui.auth(my_token)
    before = ui.go_to_cart()
    ui.search(search_by)
    ui.wait_search_to_load()
    ui.cookie()
    ui.add_to_cart()
    WebDriverWait(browser, 10).until(
        lambda driver: ui.go_to_cart() > before)
    after = ui.go_to_cart()
    assert before < after
    ui.remove_from_cart()
    ui.close_browser()

def test_order(browser):
    ui = UI(browser)
    ui.open_page()
    ui.auth(my_token)
    ui.search(search_by)
    ui.wait_search_to_load()
    ui.cookie()
    ui.add_to_cart()
    ui.in_cart()
    ui.go_to_cart()
    ui.go_to_order()
    ui.select_store()
    ui.select_another_store()
    ui.get_from_here()
    ui.fill_name(name)
    ui.fill_email(email)
    ui.fill_phone_number(phone_number)
    ui.go_to_cart()
    ui.remove_from_cart()
    ui.close_browser()

