# ===============================================================
# Author:           Bhupinderjit Singh
# Description:    This will get the number of completed solutions and based on that number, it will iterate and get name of the questions
# Create Date:     Dec 18, 2021

# Change History:
# Date                  Name                            Modification
# Dec 18, 2021     Bhupinderjit Singh       Initial Version
# ===============================================================


# import modules
from selenium.webdriver.common.by import By
import sys
import pathlib
import re
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from viewprofile import viewprofile

# define few things
repositories = []
browser = viewprofile.browser


class Scrapping:

    def __init__(self):
        pass

    def scraps(self):
        totalCompleted = '//*[@id="shell_content"]/div[5]/div/div[1]/ul/li[1]/a'
        numberOfRepos = browser.find_element(
            By.XPATH, value=totalCompleted).text
        numberOfRepos = int(re.search(r'\d+', numberOfRepos).group())
        solutions = '//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/div[1]/a'
        for i in range(1, numberOfRepos):
            element = browser.find_element(By.XPATH, value=solutions.format(
                i))
            repositories.append(element.text)
        return repositories

    def main(self):
        repositories= self.scraps()
        return repositories
        
if __name__=='__main__':
    scrap=Scrapping()
    scrap.main()