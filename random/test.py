from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from markdownify import markdownify
from bs4 import BeautifulSoup

url='https://www.codewars.com/users/pindio58/completed_solutions'
DRIVERPATH = os.environ['DRIVERFULLPATH']

service = Service(executable_path=DRIVERPATH)
browser = webdriver.Chrome(service=service)
browser.maximize_window()       
browser.get(url)

click='//*[@id="shell_content"]/div[5]/div/div[2]/div[1]/div[1]/a'
element=browser.find_element(By.XPATH,click)
element.click()