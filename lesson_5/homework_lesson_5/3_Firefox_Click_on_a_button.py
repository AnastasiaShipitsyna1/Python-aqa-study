# **Задание 3. Клик по кнопке**
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# 1. Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# 2. Пять раз кликните на кнопку `Add Element`.
button_element = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')

for _ in range(5):
    button_element.click()

# 3. Соберите со страницы список кнопок `Delete`.

# Находим контейнер, в котором расположены кнопки
container = driver.find_element(By.ID, 'elements')

# Находим все кнопки "Delete" внутри контейнера
delete_buttons = container.find_elements(By.CSS_SELECTOR, 'button.added-manually[onclick="deleteElement()"]')

# Создаем список текстовых значений кнопок
delete_button_texts = [button.text for button in delete_buttons]

# 4. Выведите на экран размер списка.
print(delete_button_texts)

sleep(15)
