from selenium import webdriver
from time import sleep

link1 = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link2)
    x = browser.find_element_by_id('num1')
    y = browser.find_element_by_id('num2')
    z = int(x.text) + int(y.text)
    print(z)
    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector(f"[value='{str(z)}']").click()

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    sleep(5)
    browser.close()
