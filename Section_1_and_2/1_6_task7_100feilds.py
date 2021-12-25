from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input[type='text']")
    for element in elements:
        element.send_keys("aaa")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    # alert = browser.alert = browser.switch_to.alert
    # print(alert.text)
    browser.quit()

# не забываем оставить пустую строку в конце файла
