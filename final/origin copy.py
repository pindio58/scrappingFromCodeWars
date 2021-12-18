#import modules
import sys
import pathlib

from selenium.webdriver.common.by import By
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from viewprofile.viewprofile import followedSection
from lgn.login import loggingIn
from viewprofile import viewprofile
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



# make instances of login and solutions tab
logi = loggingIn()
follow = followedSection()

# call their respective "main" methods
logi.main()
follow.main()


# ===========================================================================================

browser=viewprofile.browser
TOTALCOUNT=44
# test1='//*[@id="shell_content"]/div[5]/div/div[2]/div[1]/div[1]/a'
# test2='//*[@id="shell_content"]/div[5]/div/div[2]/div[2]/div[1]/a'
firstSolution='//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/div[1]/a'
# for i in range(1,TOTALCOUNT):
#     element=browser.find_element(By.XPATH, value=firstSolution.format(i))                                        # or by=
#     print(element.text)