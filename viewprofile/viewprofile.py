# ===============================================================
# Author:           Bhupinderjit Singh
# Description:    After successful login, this script will take us all the way till 'solutions' section under 'View Profile' tab
# Create Date:     Dec 18, 2021

# Change History:
# Date                  Name                            Modification
# Dec 18, 2021     Bhupinderjit Singh       Initial Version
# ===============================================================


# import modules
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from lgn import login
import time

# define few things
HOVER = '//*[@id="main_header"]/ul/li[4]'
VIEWPROFILE = '//*[@id="main_header"]/ul/li[4]/div/div/ul/li[1]/a'
SOLUTION = '//*[@id="shell_content"]/div[5]/ul/li[3]'
browser=login.browser

class followedSection:

    def __init__(self):
        pass

    def hoverOnimage(self):
        hover = browser.find_element(By.XPATH, HOVER)
        browser.implicitly_wait(10)
        print("Hover is visible? " + str(hover.is_displayed()))
        hover.click()

    def clickOnViewProfile(self):
        viewpr = browser.find_element(By.XPATH, VIEWPROFILE)
        browser.implicitly_wait(10)
        print("View profile is visible? " + str(viewpr.is_displayed()))
        viewpr.click()

    def clickOnSolutions(self):
        solution = browser.find_element(By.XPATH, SOLUTION)
        browser.implicitly_wait(10)
        print("Solution is visible? " + str(solution.is_displayed()))
        solution.click()

    def fullscreen(self):
        initialheight=browser.execute_script("return document.body.scrollHeight")
        print('First Height: ',initialheight)
        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            # browser.implicitly_wait(2)
            newheight=browser.execute_script("return document.body.scrollHeight")
            print('Next Height: ',newheight)
            if newheight==initialheight:
                break
            else:
                initialheight=newheight
        # browser.execute_script("window.scrollTo(0, 1080)") 
        # browser.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")


    def main(self):
        try:
            self.hoverOnimage()
            self.clickOnViewProfile()
            self.clickOnSolutions()
            time.sleep(2)
            # browser.implicitly_wait(2)
            self.fullscreen()
        except ElementNotInteractableException:
            print("Hover is visible? " +
                  str(self.hoverOnimage.hover.is_displayed()))
            print("View profile is visible? " +
                  str(self.clickOnViewProfile.viewpr.is_displayed()))
            print("Solution is visible? " +
                  str(self.clickOnSolutions.solution.is_displayed()))
        except StaleElementReferenceException:
            print('Some clickable object has passed and not in visibility scope anymore')


if __name__ == '__main__':
    follow = followedSection()
    follow.main()
