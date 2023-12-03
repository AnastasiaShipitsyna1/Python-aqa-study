from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Зайти в лабиринт
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.labirint.ru")

# Найти книги по слову Python
search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)  # Строка поиска на сайте
search_input.send_keys("Python", Keys.RETURN)  # Написать слово Python в строке поиска и нажать Enter

# Подождать загрузки результатов поиска (включите, если необходимо)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-card")))

# Собрать все карточки товаров
book_locator = "div.product-card"  # Переменная по отбору всех книг
books = driver.find_elements(By.CSS_SELECTOR, book_locator)  # Переменная по поиску элементов

# Вывести в консоль информацию: название + автор + цена
for book in books:
    title_locator = ".product-card__name"
    titles = book.find_element(By.CSS_SELECTOR, title_locator).text

    # Собрать цену
    price_locator = ".product-card__price-val-old div"
    prices_elements = book.find_elements(By.CSS_SELECTOR, price_locator)
    prices = [price.text for price in prices_elements]

    # Собрать авторов
    author_locator = ".product-card__author span"
    authors_elements = book.find_elements(By.CSS_SELECTOR, author_locator)
    authors = [author.text for author in authors_elements]

    # Вывести информацию
    for author, price in zip(authors, prices):
        print(f"{author}\t{titles}\t{price}rub")

sleep(5)
driver.quit()
