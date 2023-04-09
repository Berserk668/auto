


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

user_name = driver_g.find_element(By.ID, 'user-name') # по ID
user_name.send_keys('standard_user')
password = driver_g.find_element(By.XPATH, '//*[@id="password"]') # по Xpath --- всегда!!!
password.send_keys('secret_sauce')
button_click = driver_g.find_element(By.XPATH, '//*[@id="login-button"]')
button_click.click()







