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

login_standard_user = 'standard_use'
password_all = 'secret_sauce'
user_name = driver_g.find_element(By.ID, 'user-name') # по ID
user_name.send_keys(login_standard_user)
password = driver_g.find_element(By.XPATH, '//*[@id="password"]') # по Xpath --- всегда!!!
password.send_keys(password_all)
button_click = driver_g.find_element(By.XPATH, '//*[@id="login-button"]')
button_click.click()

warring_text = driver_g.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
print('хуй там')
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: You can only access '/inventory.html' when you are logged in."
print('негативный тeст пройдет успешно')