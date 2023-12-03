# **Задание 7. Поле ввода**
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 1. Откройте страницу http://the-internet.herokuapp.com/inputs.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")

# 2. Введите в поле текст `1000`.
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")

# Подождите некоторое время для визуальной проверки
sleep(2)

# 3. Очистите это поле (метод `clear`).
input_field.clear()

# Подождите некоторое время для визуальной проверки
sleep(2)

# 4. Введите в это же поле текст `999`.
input_field.send_keys("999")

# Подождите некоторое время для визуальной проверки
sleep(3)

# Закройте браузер (необходимо заменить на закрытие браузера в вашем реальном скрипте)
driver.quit()
