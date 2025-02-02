import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from configuration.ConfiProvider import ConfigProvider


@pytest.fixture
def browser():
    browser_name = ConfigProvider().get_browser_name()
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
    else:
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))

    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()
