# **Задание 6. Модальное окно**
# 1. Напишите скрипт. 

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Шаги:
# 1. Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")

# 2. В модальном окне дождитесь появления кнопки Close и нажмите на нее.
button_close = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer p"))
)
button_close.click()

sleep(5)

# Закрываем браузер.
driver.quit()
