from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link2)
    input1 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control first"]')
    input1.send_keys("Kyrylo")
    input2 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control second"]')
    input2.send_keys("Kozhumyaka")
    input3 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control third"]')
    input3.send_keys("Kyrylo@gmail.com")

    #time.sleep(10)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
