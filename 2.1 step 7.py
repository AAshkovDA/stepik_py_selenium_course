from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
link = "https://suninjuly.github.io/get_attribute.html"

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="treasure"]')
    x = x_element.get_attribute("valuex")
    # Посчитать математическую функцию от x 
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(y)

    # Отметить checkbox "I'm the robot".
    cOption = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    cOption.click()
    # Выбрать radiobutton "Robots rule!".
    rOption = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rOption.click()

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()