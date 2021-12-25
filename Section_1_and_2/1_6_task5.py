import math
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

start_link = 'http://suninjuly.github.io/find_link_text'

browser = webdriver.Chrome()
try:
    browser.get(start_link)
    # sleep(5)
    # str(math.ceil(math.pow(math.pi, math.e)*10000))
    find_link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    print(find_link.text)
    find_link.click()
    # sleep(5)

    input1 = browser.find_element_by_tag_name('input[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")

    button = browser.find_element_by_tag_name('button[type="submit"]')
    # button = browser.find_element_by_css_selector("button.btn")
    button.click()
    sleep(10)
finally:
    sleep(10)
    browser.quit()
