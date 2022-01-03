from selenium import webdriver
from time import sleep

link = "https://www.gmail.com/"
browser = webdriver.Chrome()

try:
    browser.get(link)
    sleep(1)

finally:
    sleep(3)
    browser.quit()