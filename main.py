import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

# Настройка WebDriver
service = Service(verbose=True)
driver = webdriver.Edge(service=service)
driver.get("https://ru.wikipedia.org")  # Открываем главную страницу Википедии


def search_wikipedia(query):
    url = f"https://ru.wikipedia.org/wiki/{query}"
    driver.get(url)


def list_paragraphs():
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {paragraph.text[:100]}...")  # Отображать первые 100 символов
        next_action = input("Введите 'далее' для следующего параграфа, 'назад' чтобы выйти: ")
        if next_action.lower() == 'назад':
            break


def list_links():
    links = driver.find_elements(By.XPATH, "//div[@id='bodyContent']//a[@href]")
    for i, link in enumerate(links):
        title = link.get_attribute("title")
        if title:
            print(f"{i + 1}. {title}")
    return links


def browse_wikipedia():
    while True:
        query = input("Введите запрос для поиска на Википедии: ")
        if not query:
            break
        search_wikipedia(query)
        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на связанную страницу")
            print("3. Повторить запрос")
            print("4. Выйти из программы")

            choice = input("Ваш выбор: ")
            if choice == '1':
                list_paragraphs()
            elif choice == '2':
                links = list_links()
                while True:
                    try:
                        link_choice = input("Введите номер связанной страницы, чтобы перейти: ")
                        if not link_choice.strip():
                            print("Вы ничего не ввели. Пожалуйста, введите номер.")
                            continue
                        link_choice = int(link_choice) - 1
                        if 0 <= link_choice < len(links):
                            links[link_choice].send_keys(Keys.CONTROL + Keys.RETURN)  # Открыть в новой вкладке
                            driver.switch_to.window(driver.window_handles[-1])
                            break
                        else:
                            print("Некорректный номер. Попробуйте снова.")
                    except ValueError:
                        print("Пожалуйста, введите числовое значение.")
            elif choice == '3':
                break
            elif choice == '4':
                driver.quit()
                os._exit(0)  # Принудительно завершить процесс
            else:
                print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    try:
        browse_wikipedia()
    finally:
        driver.quit()
