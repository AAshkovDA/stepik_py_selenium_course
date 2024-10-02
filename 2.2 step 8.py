from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os   

link = "http://suninjuly.github.io/file_input.html"

try: 
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("IvanPetrov@mail.ml")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    addFile = browser.find_element(By.CSS_SELECTOR, '[id="file"]')
    addFile.send_keys(file_path)

    # Нажать на кнопку Submit.
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()  

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()