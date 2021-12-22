from pathlib import Path


home = str(Path.home())
home=home+'/codewarsProjects'
MAPPING = {'Python': '.py', 'SQL': '.sql', 'Java': '.java','Shell':'.sh'}               # till the time this part is hardcoded, please add here the languages, which have been used to solve the questions                           
# TODO: get rid of hardcode MAPPING

class local:

    def __init__(self):
        pass

    def createDirAndFiles(self, language, questionName, questionSolution):
        '''Will Create the required directories and file ,named `app` '''
        dirName = home+'/'+str(language)+'/'+str(questionName)
        Path(dirName).mkdir(parents=True, exist_ok=True)                                    # make directory if doesn't exist already

        with open(dirName+'/app'+MAPPING.get(language,'.txt') ,'w') as file:        # create the file(s)
            file.write(questionSolution)
        return dirName

if __name__=='__main__':
    pass