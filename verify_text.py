from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    #message = browser.find_element_by_id("verify_message")

    # Нажимаем на кнопку

    #button.click()


    #берём текстовое значение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    #вводим ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)


    # Отправляем заполненную форму
    button2 = browser.find_element_by_id("solve")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


assert True
