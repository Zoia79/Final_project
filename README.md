# Final_project

## Тестирование сайта Читай Город

### Шаги
<ol>
  <li>Склонировать проект 'git clone https://github.com/Zoia79/Final_project.git'</li>
  <li>Установить все зависимости 'pip3 install > -r requirements.txt</li>
  <li>Запустить тесты:
    <ol>
      <li>UI: python -m pytest -v tests/test_ui.py’</li>
      <li>APi: python -m pytest -v tests/test_api.py’</li>
      <li>Все тесты: python -m pytest’</li>
    </ol>
  </li>
  <li>Сгенерировать отчет 'pytest -v --alluredir=allure-results'</li>
  <li>Открыть отчет 'allure serve allure-results'</li>
</ol>


### Стек:
- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- configparser
- json

### Структура:
- ./tests - тесты
  - test_ui -тесты UI
  - test_api - тесты API
  - test_config.ini - провайдер конфиг данных
  - test_data.json - провайдер тестовых данных
- ./page - хелперы
  - API - хелпер для работы с API
  - UI - хелпер для работы с UI
- ./configuration -провайдер настроек
   - ConfiProvider - настройки для тестов
   - DataProvider - настройки тестовых данных


### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Про configparser](https://docs.python.org/3/library/configparser.html)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)

###### Для корректной работы тестов нужно вставить свой токен в файле test_data.json
- Для API тестов в формате: eyJ0eXAiOiJKV1QiLCJh...
- Для UI тестов в формате: Bearer%20eyJ0eXAiOiJK...