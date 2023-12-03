# **Задание 5. Клик по кнопке с CSS-классом**
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# 1. Напишите скрипт. 

# Шаги:

# 1. Откройте страницу http://uitestingplayground.com/classattr.
for i in range(1,4):
   print(f"Сycle №{i}")
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   driver.get("http://uitestingplayground.com/classattr")

# 2. Кликните на **синюю** кнопку.
   button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
   button.click()
   sleep(1)

# 3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
   print("Primary button pressed")

