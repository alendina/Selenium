from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()
try:
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")

    button = browser.find_element(By.ID, "submit_button")
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
