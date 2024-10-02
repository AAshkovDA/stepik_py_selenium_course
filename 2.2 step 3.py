from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

#def calc(x1,x2):
 #   return str(x1+x2)
  
link = "https://suninjuly.github.io/selects1.html"

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменных x
    x1 = browser.find_element(By.CSS_SELECTOR, '[id="num1"]').text # ищем 1 элемент
    x2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]').text # ищем 2 элемент
    y = str(int(x1)+int(x2))
    # Поиск в списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y) # ищем элемент с текстом "x1+x2"

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()