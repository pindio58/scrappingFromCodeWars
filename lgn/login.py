# ===============================================================
# Author:           Bhupinderjit Singh
# Description:    This will login to 'codewars' using Github account
# Create Date:     Dec 18, 2021

# Change History:
# Date                  Name                            Modification
# Dec 18, 2021     Bhupinderjit Singh       Initial Version
# ===============================================================

# import modules
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from cfg.config import url, username, password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
import os


# define few other things
LOGINBYGITHUB = '//*[@id="new_user"]/button[1]'
EMAILPATH = '//*[@id="user_email"]'
PASSWORDPATH = '//*[@id="user_password"]'
DRIVERPATH = os.environ['DRIVERFULLPATH']
EMAILFIELD = 'login_field'
PASSWORDFIELD = 'password'
service = Service(executable_path=DRIVERPATH)
browser = webdriver.Chrome(service=service)                             # FYI, This single line opens a (empty) browser
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
        passwordelement.send_keys(password)
        passwordelement.submit()

    def main(self):
        self.signInWithGitHub(url, LOGINBYGITHUB)
        self.loggedin(EMAILFIELD, PASSWORDFIELD)


if __name__ == '__main__':
    logi = loggingIn()
    logi.main()
