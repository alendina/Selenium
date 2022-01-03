import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    first = browser.find_element_by_name('firstname')
    first.send_keys('F name')

    last = browser.find_element_by_name('lastname')
    last.send_keys('L name')

    email = browser.find_element_by_name('email')
    email.send_keys('F name')

    #current_dir = os.path.abspath(os.path.dirname(__file__))
    current_dir = os.getcwd()
    file_name = "Info_XPath.txt"
    print(current_dir)
    print(file_name)
    file_path = os.path.join(current_dir, file_name)
    print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    sleep(2)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print('Code is: ' + alert_text.split(': ')[-1])
    alert.accept()

finally:
    sleep(5)
    browser.quit()

