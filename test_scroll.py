from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

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
button_click = driver_g.find_element(By.XPATH, '//*[@id="login-button"]')
button_click.click()
time.sleep(1)

action = ActionChains(driver_g)
red_t_shits = driver_g.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
action.move_to_element(red_t_shits).perform()

#driver_g.execute_script("window.scrollTo(0, 500)")



time.sleep(5)
driver_g.close()