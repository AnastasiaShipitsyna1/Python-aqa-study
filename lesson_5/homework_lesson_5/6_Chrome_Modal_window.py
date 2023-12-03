# **Задание 6. Модальное окно**
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 1. Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")

# 2. В модальном окне дождитесь появления кнопки Close и нажмите на нее.
button_close = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer p"))
)
button_close.click()

sleep(5)

