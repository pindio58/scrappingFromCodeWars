
# TODO: Close the browser at last
# TODO: print statement gives error on slower speed, might need to catch specific exception
# TODO: Raise exception in few cases

# import modules
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from viewprofile.viewprofile import followedSection
from lgn.login import loggingIn
from scrapping.scrap import Scrapping
from scrapping import scrap
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, WebDriverException
from gitHubPart.pushToGitHub import createAndPushToGitHub

# define few things
browser = scrap.browser

# Not used atm


class myexception(Exception):
    """Raise for my specific kind of exception"""


# make instances of login, solutions and scrap
logi = loggingIn()
follow = followedSection()
scrap = Scrapping()
push = createAndPushToGitHub()

# call their respective "main" methods
try:
    logi.main()
    follow.main()
    repositories = scrap.main()
    push.final()
    
except NoSuchElementException:
    browser.close()
except (NoSuchWindowException, WebDriverException) as e:
    print('Chrome has closed immaturely')
