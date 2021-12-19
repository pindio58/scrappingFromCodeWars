from pathlib import Path

home = str(Path.home())
home=home+'/codewarsProjects'
MAPPING = {'Python': '.py', 'SQL': '.sql', 'Java': '.java'}


class local:

    def __init__(self):
        pass

    def createDirAndFiles(self, language, questionName, questionSolution):
        dirName = home+'/'+str(language)+'/'+str(questionName)
        print(dirName)
        Path(dirName).mkdir(parents=True, exist_ok=True)

        with open(dirName+'/app'+MAPPING.get(language,'.txt') ,'w') as file:
            file.write(questionSolution)


if __name__=='__main__':
    pass