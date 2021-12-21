# ===============================================================
# Author:           Bhupinderjit Singh
# Description:    This will login to 'codewars' using Github account
# Create Date:     Dec 18, 2021

# Change History:
# Date                  Name                            Modification
# Dec 18, 2021     Bhupinderjit Singh       Initial Version
# Dec 20,2021      Bhupinderjit Singh       Chnaged login method using cookies , since Chrome wasn't allowing bot to login
# ===============================================================

# import modules
import sys
import pathlib
import time
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from cfg.config import url, username, password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
import os
from csv import DictReader

# define few other things
LOGINBYGITHUB = '//*[@id="new_user"]/button[1]'
EMAILPATH = '//*[@id="user_email"]'
PASSWORDPATH = '//*[@id="user_password"]'
DRIVERPATH = os.environ['DRIVERFULLPATH']
EMAILFIELD = 'login_field'
PASSWORDFIELD = 'password'

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
service = Service(executable_path=DRIVERPATH)
browser = webdriver.Chrome(service=service, options=options)                             # FYI, This single line opens a (empty) browser
browser.maximize_window()                                                        # comment this when we browser goes headless


class loggingIn:

    def __init__(self):
        pass

    #  click on github
    def signInWithGitHub(self, url=url, LOGINBYGITHUB=LOGINBYGITHUB):
        browser.get(url)
        element = browser.find_element(By.XPATH, value=LOGINBYGITHUB)
        element.click()
        browser.implicitly_wait(2)
        # TODO: To take care of authorization when logged in too many times

    
    # fill in details
    def loggedin(self, emailfield=EMAILFIELD, passwordfiled=PASSWORDFIELD):
        emailelement = browser.find_element(By.ID, value=emailfield)
        passwordelement = browser.find_element(By.ID, value=passwordfiled)
        emailelement.send_keys(username)
        time.sleep(1)
        passwordelement.send_keys(password)
        time.sleep(2)
        passwordelement.submit()

    def loggedinusingCookies(self):
        with open('/home/jeet/projects/scrappingFromCodeWars/lgn/cookies.csv',encoding='utf-8') as file:
            dict_read=DictReader(file)
            list_of_dicts=list(dict_read)
            for i in list_of_dicts:
                browser.add_cookie(i)
            browser.refresh()
        

    def main(self):
        self.signInWithGitHub(url, LOGINBYGITHUB)
        self.loggedin(EMAILFIELD, PASSWORDFIELD)
        time.sleep(2)
        # self.loggedinusingCookies()

if __name__ == '__main__':
    logi = loggingIn()
    logi.main()

# with open('/home/jeet/projects/scrappingFromCodeWars/lgn/cookies.csv',encoding='utf-8') as file:
#     dict_read=DictReader(file)
#     list_of_dicts=list(dict_read)
#     for i in list_of_dicts:
#         print(i)