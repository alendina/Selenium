from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
try:
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@name="first_name"]')
    input1.send_keys("Kyrylo")
    input2 = browser.find_element_by_xpath('//input[@name="last_name"]')
    input2.send_keys("Kozhumyaka")
    input3 = browser.find_element_by_xpath('//input[@class="form-control city"]')
    input3.send_keys("Poltava")
    input4 = browser.find_element_by_xpath('//input[@id="country"]') # //input[@id='country']
    input4.send_keys("Ukraine")

    button = browser.find_element(By.TAG_NAME, 'button[type="submit"]')
    #button = browser.find_element_by_css_selector("button.btn")
    button.click()
    #sleep(10)
finally:
    sleep(30)
    browser.quit()

# alternative:
# with webdriver.Chrome() as browser:
#     browser.get(link)
#     button = browser.find_element('id', "submit_button")
#     button.click()
