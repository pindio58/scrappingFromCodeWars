# final code

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from markdownify import markdownify
from bs4 import BeautifulSoup

url='https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python'
DRIVERPATH = os.environ['DRIVERFULLPATH']

service = Service(executable_path=DRIVERPATH)
browser = webdriver.Chrome(service=service)
browser.maximize_window()       
browser.get(url)

element=browser.find_element(By.XPATH,'//*[@id="description"]')
element=element.get_attribute('outerHTML')

# print(type(element))

soup=BeautifulSoup(element, features='html.parser')

for pre in soup.find_all('pre'):
    if 'python' not in pre.code.attrs['class'][0]:
        pre.decompose()

# print(type(soup))

html=markdownify(str(soup))

with open('done.md','w') as file:
    file.write('###Description\n')
    file.write(html)

with open ('done.md','r') as file:
    ele=file.read()
    n=ele.index('```')
    ele=ele.replace('```','```python',1)
    ele=ele.replace('\\','')
    with open('done.md','w') as file:
        file.write(ele)