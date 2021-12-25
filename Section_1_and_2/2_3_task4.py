from selenium import webdriver
from time import sleep
from math import log, sin

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    sleep(2)
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id('input_value').text
    x = log(abs(12 * sin(int(x))))
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(str(x))

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    sleep(2)
    alert = browser.switch_to.alert
    alert_text = alert.text.split(':')[-1]
    print(alert_text)
    alert.accept()

finally:
    sleep(5)
    browser.quit()
