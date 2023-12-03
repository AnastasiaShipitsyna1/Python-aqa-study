# **Задание 3. Клик по кнопке**

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Шаги:
# 1. Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# 2. Пять раз кликните на кнопку `Add Element`.
button_element = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')

for _ in range(5):
    button_element.click()

# 3. Соберите со страницы список кнопок `Delete`.

# Находим контейнер, в котором расположены кнопки
container = driver.find_element(By.ID, 'elements')

# Находим все кнопки "Delete" внутри контейнера
delete_buttons = container.find_elements(By.CSS_SELECTOR, 'button.added-manually[onclick="deleteElement()"]')

# Создаем список текстовых значений кнопок
delete_button_texts = [button.text for button in delete_buttons]

# 4. Выведите на экран размер списка.
print(delete_button_texts)


sleep(15)

# пояснения
# container = driver.find_element(By.ID, 'elements'): Эта строка находит элемент на веб-странице с идентификатором "elements" (в данном случае, это <div> контейнер).

# delete_buttons = container.find_elements(By.CSS_SELECTOR, 'button.added-manually[onclick="deleteElement()"]'): 
# Здесь  используем метод find_elements, чтобы найти все элементы внутри container, 
# которые соответствуют CSS-селектору 'button.added-manually[onclick="deleteElement()"]'.
#  Этот селектор ищет все кнопки (<button>), у которых есть класс "added-manually" и атрибут onclick со значением "deleteElement()".

# delete_button_texts = [button.text for button in delete_buttons]:  создаем список delete_button_texts, 
# в котором содержатся текстовые значения каждой найденной кнопки "Delete". Мы используем list comprehension для более компактного кода.

# print(delete_button_texts): Выводим список текстовых значений кнопок "Delete" на консоль.