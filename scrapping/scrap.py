# ===============================================================
# Author:           Bhupinderjit Singh
# Description:    This will get the number of completed solutions and based on that number, it will iterate and get name of the questions
# Create Date:     Dec 18, 2021

# Change History:
# Date                  Name                            Modification
# Dec 18, 2021     Bhupinderjit Singh       Initial Version
# ===============================================================


# import modules
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from dirandfiles.bringToLocal import local
from selenium.webdriver.common.by import By
import time
import re
from viewprofile import viewprofile


# define few things
repositories = []
browser = viewprofile.browser
# filename = '/home/jeet/projects/scrappingFromCodeWars/allcodes.txt'
loc = local()

# with open(filename, 'w') as file:
#     file.write('Codes\n\n')


class Scrapping:

    def __init__(self):
        pass

    def scrapAndSaveLocal(self):
        totalCompleted = '//*[@id="shell_content"]/div[5]/div/div[1]/ul/li[1]/a'
        numberOfRepos = browser.find_element(
            By.XPATH, value=totalCompleted).text
        numberOfRepos = int(re.search(r'\d+', numberOfRepos).group())+1
        questionNames = '//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/div[1]/a'
        questionSolutions = '//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/div[2]/pre/code'
        languages = '//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/h6'

        for i in range(1, numberOfRepos):
            language = browser.find_element(By.XPATH, value=languages.format(
                i)).text
            language = language.replace(':', '')
            questionName = browser.find_element(By.XPATH, value=questionNames.format(
                i)).text.replace(' ','_').replace('-','_')
            questionSolution = browser.find_element(By.XPATH, value=questionSolutions.format(
                i)).text
            repositories.append(questionName)

            loc.createDirAndFiles(language, questionName, questionSolution)

        browser.close()
        return repositories

    def main(self):
        repositories = self.scrapAndSaveLocal()
        return repositories


if __name__ == '__main__':
    scrap = Scrapping()
    scrap.main()
