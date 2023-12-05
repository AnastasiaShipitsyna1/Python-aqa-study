#установка selenium: pip install selenium (в командной строке VSC)

from selenium import webdriver
driver = webdriver.Firefox
# pypi.org --> webrdiver manager for Python (Chrome, Firefox and etc) for Firefox is GeckoDriver
# pip install webdriver-manager

# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))