from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains, Keys
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
password = driver_g.find_element(By.XPATH, '//*[@id="password"]') # по Xpath --- всегда!!!
password.send_keys(password_all)
password.send_keys(Keys.ENTER) # дейсвие , подобное прожатию кнопки Enter
filter = driver_g.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
filter.click()
time.sleep(1)
filter.send_keys(Keys.DOWN) # Имитация кнопки "вниз"
time.sleep(1)
filter.send_keys(Keys.RETURN)
now_date = datetime.datetime.utcnow().strftime('%d.%m.%Y.%H.%M.') # дата и время скрина
name_screenshot = 'screenshot.png' + now_date + '.png' # дата и время скрина
driver_g.save_screenshot('C:\\testing\\test_1\\screen\\' + name_screenshot) #  Скрин экрана

time.sleep(5)
driver_g.close()