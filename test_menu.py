from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

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
menu = driver_g.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
menu.click()
time.sleep(1)
link_about = driver_g.find_element(By.XPATH, '//*[@id="about_sidebar_link"]')
link_about.click()
time.sleep(5)
now_date = datetime.datetime.utcnow().strftime('%d.%m.%Y.%H.%M.') # дата и время скрина
name_screenshot = 'screenshot.png' + now_date + '.png' # дата и время скрина
driver_g.save_screenshot('C:\\testing\\test_1\\screen\\' + name_screenshot) #  Скрин экрана

time.sleep(5)
driver_g.close()