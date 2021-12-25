from selenium import webdriver
from time import sleep

link = "https://www.google.com/"
browser = webdriver.Chrome()

try:
    browser.get(link)
    sleep(1)
    input_field = browser.find_element_by_css_selector('input[name="q"]')
    input_field.send_keys('курс доллара')
    input_field.click()
    sleep(1)
    button = browser.find_element_by_css_selector('input[name="btnK"]')
    button.click()
    sleep(2)
    num_field = browser.find_element_by_css_selector('div.H07hi > table > tbody > tr:nth-child(3) > td:nth-child(1) > input')
    num = num_field.get_attribute('value')
    print(f"Курс доллара: {num} грн за дол")

finally:
    sleep(3)
    browser.quit()