
# TODo
# Authorization

# import modules
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from viewprofile.viewprofile import followedSection
from lgn.login import loggingIn

# make instances of login and solutions tab
logi = loggingIn()
follow = followedSection()

# call their respective "main" methods
logi.main()
follow.main()
