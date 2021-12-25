from selenium import webdriver
import time

try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome( )
    #browser = webdriver.Chrome('D:/chromedriver/chromedriver.exe')
    browser.get(link)

    first_name = browser.find_element_by_class_name("form-control.first[placeholder='Input your first name']")
    first_name.send_keys('Ivan')

    last_name = browser.find_element_by_class_name("form-control.second[placeholder='Input your last name']")
    last_name.send_keys('Petrov')

    email = browser.find_element_by_class_name("form-control.third[placeholder='Input your email']")
    email.send_keys('ivan.petrov@stepik.ru')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

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