from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Настройка драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Пробуем открыть страницу
try:
    driver.get("https://www.chitai-gorod.ru/")
    sleep(5)  # Даем браузеру время открыться
    print("Страница открыта успешно!")
except Exception as e:
    print(f"Ошибка открытия страницы: {e}")
finally:
    driver.quit()
