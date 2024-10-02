from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    # Нажать на кнопку Submit.
    button = browser.find_element(By.TAG_NAME, "button")
    button.click() 
    time.sleep(2)
  
    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)
  
    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    # Посчитать математическую функцию от x 
    y = calc(x)    

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(y)
   
    # Нажать на кнопку Submit.
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()  

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()