from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
import os


DRIVERPATH=os.environ['DRIVERFULLPATH']
XPATH='//*[@id="new_user"]/button[1]'
url='https://www.codewars.com/users/sign_in'
emailpath='//*[@id="user_email"]'
passwordpath='//*[@id="user_password"]'
username = 'pindio58'
password = 'Github1!singh'

# click on github
service=Service(DRIVERPATH)
driver = webdriver.Chrome(service=service)
driver.get(url)
element=driver.find_element(By.XPATH, value=XPATH)
element.click()

# fill in details
driver.implicitly_wait(2)

emailelement=driver.find_element(By.ID, value='login_field')
passwordelement=driver.find_element(By.ID, value='password')
emailelement.send_keys(username)
passwordelement.send_keys(password)
passwordelement.submit()