# **Задание 4. Клик по кнопке без ID**

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# 1. Напишите скрипт. 
# Шаги:
for i in range(1,4):
   print(f"Сycle №{i}")
# 1. Откройте страницу http://uitestingplayground.com/dynamicid.
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   driver.get("http://uitestingplayground.com/dynamicid")

# Кликаем на синюю кнопку три раза.
   for _ in range(3):
    # Находим кнопку после каждого клика.
       button = driver.find_element(By.CLASS_NAME, "btn-primary")
       button.click()
       sleep(1)
       dynamic_id = button.get_attribute("id")
       print("Dynamic ID:", dynamic_id)

# Закрываем браузер.
driver.quit()