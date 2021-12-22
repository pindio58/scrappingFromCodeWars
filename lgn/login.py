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
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome import options
from selenium import webdriver
from cfg.config import password, url, username
from csv import DictReader
import time
import os
from getpass import getpass

# define few static things that will be used as we move forward
LOGINBYGITHUB: str = '//*[@id="new_user"]/button[1]'
EMAILPATH: str = '//*[@id="user_email"]'
PASSWORDPATH: str = '//*[@id="user_password"]'
DRIVERPATH: str = os.environ['DRIVERFULLPATH']
EMAILFIELD: str = 'login_field'
PASSWORDFIELD: str = 'password'
COOKIESFILE=str(pathlib.Path(__file__).parent.resolve())
COOKIESFILE=COOKIESFILE+'cookies.csv'

# start the browser
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('headless')                                                                # Comment this to go headless
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
service = Service(executable_path=DRIVERPATH)                                   # FYI, This single line opens a (empty) browser
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()


class loggingIn:

    def __init__(self):
        self.username = input('Enter your GitHub username: ')
        self.password = getpass('Please enter your password: ')
        # FIXME: exit from asking username/ password popup if browser closed explictly
    #  click on github
    def signInWithGitHub(self, url=url, LOGINBYGITHUB=LOGINBYGITHUB):
        '''This method will be used to click on  GitHub option to log in'''
        browser.get(url)
        element = browser.find_element(By.XPATH, value=LOGINBYGITHUB)
        element.click()
        browser.implicitly_wait(2)
        # TODO: To take care of authorization when logged in too many times

    # fill in details

    def logInUsingUserPass(self, emailfield=EMAILFIELD, passwordfiled=PASSWORDFIELD):
        '''This will be used to fill in the details such as username, password.
        Another way to enter the username password is adding these details in config file and import them here however you need to be
        careful since password will be openly displayed!'''
        emailelement = browser.find_element(By.ID, value=emailfield)
        passwordelement = browser.find_element(By.ID, value=passwordfiled)
        emailelement.send_keys(self.username)
        time.sleep(1)
        passwordelement.send_keys(self.password)
        time.sleep(2)
        passwordelement.submit()

    def loggedInUsingCookies(self):
        '''This is another method to login. Rather than entering/asking username , password, it will use stored cookies of your GitHub account'''
        with open(COOKIESFILE, encoding='utf-8') as file:
            dict_read = DictReader(file)
            list_of_dicts = list(dict_read)
            for i in list_of_dicts:
                browser.add_cookie(i)
            browser.refresh()

    def main(self):
        self.signInWithGitHub(url, LOGINBYGITHUB)
        self.logInUsingUserPass(EMAILFIELD, PASSWORDFIELD)
        time.sleep(2)
        # self.loggedinusingCookies()


if __name__ == '__main__':
    logi = loggingIn()
    logi.main()
