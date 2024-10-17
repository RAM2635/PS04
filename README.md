# Wikipedia Browser Automation

Эта программа позволяет искать информацию на Википедии с помощью консоли, используя Selenium WebDriver и браузер Microsoft Edge.

## Описание

Программа запускает Microsoft Edge, открывает главную страницу Википедии и предоставляет следующие возможности:
1. Выполнить поиск по запросу на Википедии.
2. Листать параграфы текущей статьи.
3. Переходить по связанным ссылкам на другие страницы и продолжать просмотр.
4. Повторить поиск или выйти из программы.

## Требования

- Python 3.x
- Установленный [Selenium](https://pypi.org/project/selenium/)
- Microsoft Edge
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) (установлен в `C:\WebDriver\`, пути для `msedgedriver` прописаны)

## Установка

1. Установите Selenium с помощью pip:
    ```bash
    pip install selenium
    ```
2. Убедитесь, что Microsoft Edge WebDriver установлен и пути к `msedgedriver` прописаны.

## Использование

Запустите программу:
```bash
python your_script_name.py
