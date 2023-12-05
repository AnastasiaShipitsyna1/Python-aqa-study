# **Задание 5. Клик по кнопке с CSS-классом**

# 1. Напишите скрипт. 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Шаги:
for i in range(1, 4):
    print(f"Сycle №{i}")
    # 1. Откройте страницу http://uitestingplayground.com/classattr.
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("http://uitestingplayground.com/classattr")

    # 2. Кликните на синюю кнопку.
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    sleep(1)

    # 3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
    print("Primary button pressed")

    # Закрываем браузер.
    driver.quit()
