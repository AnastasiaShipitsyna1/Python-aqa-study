# **Задание 8. Форма авторизации**
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 1. Откройте страницу http://the-internet.herokuapp.com/login.
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

# 2. В поле username введите значение `tomsmith`.
input_username = driver.find_element(By.ID, "username")
input_username.send_keys("tomsmith")

# 3. В поле password введите значение `SuperSecretPassword!`.
input_password = driver.find_element(By.ID, "password")
input_password.send_keys("SuperSecretPassword!")

# 4. Нажмите кнопку `Login`.
button_login = driver.find_element(By.CSS_SELECTOR, ".radius")
button_login.click()

sleep(2)
driver.quit()




