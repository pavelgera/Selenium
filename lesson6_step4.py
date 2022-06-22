#-----Заполнение формы-------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#     input1 = driver.find_element(By.TAG_NAME, "Input").send_keys("Selenium")
#     input2 = driver.find_element(By.NAME, "last_name").send_keys("webdriver" )
#     input3 = driver.find_element(By.CLASS_NAME, "city").send_keys("Minsk" )
#     input4 = driver.find_element(By.ID, "country").send_keys("Belarus" )
#     button = driver.find_element(By.XPATH, '//*[@id="submit_button"]').click()
#
# finally:
#     time.sleep(10)
#     driver.quit()

#-----------Поиск ссылки, переход по ней и заполнение формы по ссылке--------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_link_text"
#
# driver = webdriver.Chrome()
# driver.get(link)
#
# link = driver.find_element(By.LINK_TEXT, '224592').click()
# input1 = driver.find_element(By.TAG_NAME, "Input").send_keys("Selenium")
# input2 = driver.find_element(By.NAME, "last_name").send_keys("webdriver" )
# input3 = driver.find_element(By.CLASS_NAME, "city").send_keys("Minsk" )
# input4 = driver.find_element(By.ID, "country").send_keys("Belarus" )
# button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#
# time.sleep(10)
# driver.quit()

#-------------------Поиск локатора и заполнение множества полей----------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     driver = webdriver.Chrome()
#     driver.get("http://suninjuly.github.io/huge_form.html")
#     elements = driver.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Selenium")
#
#     button = driver.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     driver.quit()

#Поиск кнопки по XPATH

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#     input1 = driver.find_element(By.TAG_NAME, "Input").send_keys("Selenium")
#     input2 = driver.find_element(By.NAME, "last_name").send_keys("webdriver" )
#     input3 = driver.find_element(By.CLASS_NAME, "city").send_keys("Minsk" )
#     input4 = driver.find_element(By.ID, "country").send_keys("Belarus" )
#     button = driver.find_element(By.XPATH, '/html/body/div/form/div[6]/button[3]').click()
#
# finally:
#     time.sleep(10)
#     driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#     input1 = driver.find_element(By.TAG_NAME, "Input").send_keys("Selenium")
#     input2 = driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input').send_keys("webdriver" )
#     input3 = driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input').send_keys("Minsk@mail.ru" )
#
#     # Отправляем заполненную форму
#     button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     time.sleep(10)
#     driver.quit()

# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/math.html"
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#     x_element = driver.find_element(By.ID, 'input_value')
#     x = x_element.text
#     y = calc(x)
#     input = driver.find_element(By.ID, 'answer').send_keys(y)
#     option1 = driver.find_element(By.ID, "robotCheckbox").click()
#     option2 = driver.find_element(By.ID, "robotsRule").click()
#     button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
# finally:
#     time.sleep(10)
#     driver.quit()

#Заполнение формы с вводом автоматической проверкой(решение задачи)
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/get_attribute.html"
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#     a_element = driver.find_element(By.ID, "treasure")
#     x_element = a_element.get_attribute("valuex")
#     x = x_element
#     y = calc(x)
#     input = driver.find_element(By.ID, 'answer').send_keys(y)
#     option1 = driver.find_element(By.ID, "robotCheckbox").click()
#     option2 = driver.find_element(By.ID, "robotsRule").click()
#     button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
# finally:
#     time.sleep(10)
#     driver.quit()

# Задание: работа с выпадающим списком
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.select import Select
#
# link = "http://suninjuly.github.io/selects2.html"
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#     a_el = driver.find_element(By.ID, 'num1')
#     b_el = driver.find_element(By.ID, 'num2')
#     x, y = a_el.text, b_el.text
#     z = int(x) + int(y)
#
#     select = Select(driver.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(str(z))
#     button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#
# finally:
#     time.sleep(10)
#     driver.quit()

# Скроллинг обходя foobar методом execute_script
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/execute_script.html"
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#     x_element = driver.find_element(By.ID, 'input_value')
#     x = x_element.text
#     y = calc(x)
#     input = driver.find_element(By.ID, 'answer').send_keys(y)
#     driver.execute_script("window.scrollBy(0, 120);")
#     option1 = driver.find_element(By.ID, "robotCheckbox").click()
#     option2 = driver.find_element(By.ID, "robotsRule").click()
#     button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#
# finally:
#     time.sleep(10)
#     driver.quit()


# Заполнение полей и загрузка файла с компьютера(из рабочей директории)
# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/file_input.html"
#
# try:
#      driver = webdriver.Chrome()
#      driver.get(link)
#
#      input1 = driver.find_element(By.NAME, "firstname").send_keys("Selenium")
#      input2 = driver.find_element(By.NAME, "lastname").send_keys("webdriver" )
#      input3 = driver.find_element(By.NAME, "email").send_keys("Minsk@gmail.com" )
#      element = driver.find_element(By.ID, 'file')
#      current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#      file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
#      element.send_keys(file_path)
#      button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#
# finally:
#      time.sleep(10)
#      driver.quit()


# Нажать на кнопку, Принять allert, вычислить функцию и нажать submit
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/alert_accept.html"
#
# try:
#    driver = webdriver.Chrome()
#    driver.get(link)
#
#    button_1 = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#    confirm = driver.switch_to.alert
#    confirm.accept()
#    def calc(x):
#        return str(math.log(abs(12 * math.sin(int(x)))))
#    x_element = driver.find_element(By.ID, 'input_value')
#    x = x_element.text
#    y = calc(x)
#    input = driver.find_element(By.ID, 'answer').send_keys(y)
#    button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#
# finally:
#     time.sleep(10)
#     driver.quit()

# Переход на новую вкладку и заполнение поля в ней
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/redirect_accept.html"
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#     button_1 = driver.find_element(By.CSS_SELECTOR, "button.trollface").click()
#     new_window = driver.window_handles[1]
#     driver.switch_to.window(new_window)
#     def calc(x):
#        return str(math.log(abs(12 * math.sin(int(x)))))
#     x_element = driver.find_element(By.ID, 'input_value')
#     x = x_element.text
#     y = calc(x)
#     input = driver.find_element(By.ID, 'answer').send_keys(y)
#     button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#
# finally:
#     time.sleep(10)
#     driver.quit()

#Ожидание implicitly_wait
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)#каждый вызов команды find_element WebDriver будет ждать 5 секунд
# # до появления элемента на странице прежде, чем выбросить исключение NoSuchElementException.
# driver.get("http://suninjuly.github.io/wait1.html")
#
# button = driver.find_element(By.ID, "verify")
# button.click()
# message = driver.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

#Ожидание когда кнопка станет активной
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

#Ожидание определенного числа и клик после
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")


# Ждем 12 секунд пока появится нужная нам цифра
    element = WebDriverWait(driver, 12).until(
             EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    driver.find_element(By.ID, "book").click()#После того как дождались кликаем на кнопку

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))# Вычисляем значение
    x_element = driver.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    driver.find_element(By.ID, 'answer').send_keys(y)#Вставляем значение
    driver.find_element(By.ID, "solve").click()#Кликаем

finally:
    time.sleep(10)
    driver.quit()