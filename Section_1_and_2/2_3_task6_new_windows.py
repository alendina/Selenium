from selenium import webdriver
from time import sleep
from math import log, sin

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser.get(link)
    sleep(2)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    print(new_window)
    first_window = browser.window_handles[0]
    print(first_window)

    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    x = log(abs(12 * sin(int(x))))
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(str(x))
    sleep(2)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    sleep(2)
    alert = browser.switch_to.alert
    alert_text = alert.text.split(':')[-1]

    print(alert_text.lstrip())
    alert.accept()

finally:
    sleep(5)
    browser.quit()
