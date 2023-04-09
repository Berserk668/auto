from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

print('------')
print('Переход на url')

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver_g.find_element(By.ID, 'user-name') # по ID
user_name.send_keys(login_standard_user)
print('Логин введен')
password = driver_g.find_element(By.XPATH, '//*[@id="password"]') # по Xpath --- всегда!!!
password.send_keys(password_all)
print('Пароль введен')
button_click = driver_g.find_element(By.XPATH, '//*[@id="login-button"]')
button_click.click()
print('Нажатие на кнопку прошло успешно')
print('Вердикт: Успешно')
print('------')


# text_products = driver_g.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == 'Products'
# print('GOOD')

url = 'https://www.saucedemo.com/inventory.html'
get_url = driver_g.current_url
print(get_url)
assert url == get_url
print('url совподает')
print('Вердикт: Успешно')
print('------')
time.sleep(5)
driver_g.close()