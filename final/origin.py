
# TODO: Close the browser at last
# TODO: print statement gives error on slower speed, might need to catch specific exception
# TODO: Raise exception in few cases

# import modules
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, WebDriverException
from scrapping import scrap
from scrapping.scrap import Scrapping
from lgn.login import loggingIn
from viewprofile.viewprofile import followedSection


# define few things
browser = scrap.browser

# Not used atm
class myexception(Exception):
    """Raise for my specific kind of exception"""


# make instances of login, solutions and scrap
logi = loggingIn()
follow = followedSection()
scrap = Scrapping()

# call their respective "main" methods
try:
    logi.main()
    follow.main()
    repositories = scrap.main()
except NoSuchElementException:
    browser.close()
except (NoSuchWindowException, WebDriverException) as e:
    print('Chrome has closed immaturely')

# print
print(repositories)
