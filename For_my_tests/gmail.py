from selenium import webdriver
from time import sleep

link = "https://www.gmail.com/"
browser = webdriver.Chrome()

try:
    browser.get(link)
    sleep(1)
    # WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
finally:
    sleep(3)
    browser.quit()