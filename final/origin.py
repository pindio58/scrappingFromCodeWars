
# TODo
# To take care of authorization
# Close browser 

# import modules
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from viewprofile.viewprofile import followedSection
from lgn.login import loggingIn
from scrapping.scrap import Scrapping

# make instances of login, solutions and scrap
logi = loggingIn()
follow = followedSection()
scrap=Scrapping()

# call their respective "main" methods
logi.main()
follow.main()
repositories=scrap.main()

# print
print(repositories)