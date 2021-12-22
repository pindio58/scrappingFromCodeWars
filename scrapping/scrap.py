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
from bs4 import BeautifulSoup
from markdownify import markdownify
from viewprofile import viewprofile
import re
import time
from selenium.webdriver.common.by import By
from dirandfiles.bringToLocal import local

# define few things
repositories = []
browser = viewprofile.browser
loc = local()


class Scrapping:

    def __init__(self):
        pass

    def generateMDfiles(self, language,dirName, hyperlinkToClick):
        fileFullPath=dirName+'/README.md'
        hyperlinkToClick.click()
        element = browser.find_element(By.XPATH, '//*[@id="description"]') 
        element = element.get_attribute('outerHTML')
        soup = BeautifulSoup(element, features='html.parser')
        
        if len(soup.find_all('pre'))>1:
            for pre in soup.find_all('pre'):
                if pre.code.has_attr('class'):
                    if ('sql' not in pre.code.attrs['class'][0].lower()) and ('sql' not in pre.code.attrs['class'][0].lower()) and ('java' not in pre.code.attrs['class'][0].lower()):
                        pre.decompose()
        
        html = markdownify(str(soup))

        with open(fileFullPath, 'w') as file:
            file.write(html)

        with open(fileFullPath, 'r') as file:
            ele = file.read()
            if '```' in ele:
                ele = ele.replace('```', '```'+language, 1)
            if '\\' in ele:
                ele = ele.replace('\\', '')
            with open(fileFullPath, 'w') as file:
                file.write(ele)

    def scrapAndSaveLocal(self):
        totalCompleted = '//*[@id="shell_content"]/div[5]/div/div[1]/ul/li[1]/a'
        numberOfRepos = browser.find_element(
            By.XPATH, value=totalCompleted).text
        numberOfRepos = int(re.search(r'\d+', numberOfRepos).group())+1
        questionNames = '//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/div[1]/a'
        questionSolutions = '//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/div[2]/pre/code'
        languages = '//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/h6'
        hyperlinksToClick = '//*[@id="shell_content"]/div[5]/div/div[2]/div[{}]/div[1]/a'
        print(numberOfRepos)

        
        for i in range(1, numberOfRepos):
            language = browser.find_element(By.XPATH, value=languages.format(
                i)).text.replace(':', '')
            questionName = browser.find_element(By.XPATH, value=questionNames.format(
                i)).text.replace(' ', '_').replace('-', '_')
            questionSolution = browser.find_element(By.XPATH, value=questionSolutions.format(
                i)).text
            hyperlinkToClick = browser.find_element(By.XPATH, value=hyperlinksToClick.format(
                i))

            # repositories.append(questionName)                                                                   # will be used furtther

            # create all required directories and code files
            dirName = loc.createDirAndFiles(
                language, questionName, questionSolution)
            
            # time.sleep(0.7)
            print('{}) {}'.format(i,questionName))
            

            # call the function to generate README files
            self.generateMDfiles(language=language,
                dirName=dirName, hyperlinkToClick=hyperlinkToClick)
            browser.execute_script("window.history.go(-1)")

        browser.close()
        return repositories

    def main(self):
        repositories = self.scrapAndSaveLocal()
        return repositories


if __name__ == '__main__':
    scrap = Scrapping()
    scrap.main()