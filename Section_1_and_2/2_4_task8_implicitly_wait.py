'''
Требуется написать программу, которая будет бронировать нам дом для отдыха
по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой
цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод
text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве
ответа на это задание
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import log, sin

link = "http://suninjuly.github.io/explicit_wait2.html"


browser = webdriver.Chrome()
browser.implicitly_wait(5)
try:
    browser.get(link)

    # coloring find_element
    div_to_change = browser.find_element_by_id("price")
    browser.execute_script("arguments[0].setAttribute('style', 'background-color: rgb(222, 0, 0);')",
                           div_to_change)
    #

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    button = browser.find_element_by_id('book')
    button.click()

    input_value_element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "input_value")))
    x = input_value_element.text
    x = log(abs(12 * sin(int(x))))
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(str(x))

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text.split(':')[-1]
    print(alert_text)
    alert.accept()

finally:
    sleep(5)
    browser.quit()