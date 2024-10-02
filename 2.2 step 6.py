from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
link = "https://suninjuly.github.io/execute_script.html"

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    # Посчитать математическую функцию от x 
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(y)

    # Отметить checkbox "I'm the robot".
    cOption = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    cOption.click()
    
    # Проскролить до radiobutton
    rOption = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rOption)
    # Выбрать radiobutton "Robots rule!".
    rOption.click()

    # Проскролить до кнопки
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Нажать на кнопку Submit.
    button.click()  

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()