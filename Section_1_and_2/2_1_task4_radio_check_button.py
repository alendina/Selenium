from selenium import webdriver
import math
from time import sleep


def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    print(y)
    print(calc(978))
    input_y = browser.find_element_by_id('answer')
    input_y.send_keys(y)
    check = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    check.click()
    radio = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    radio.click()
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    sleep(5)
    browser.close()