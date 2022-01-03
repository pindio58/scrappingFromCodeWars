import sys
import git
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from re import sub
from cfg.config import folderName, username
import os
import subprocess


# path of our project folder
fullPath = str(pathlib.Path.home().joinpath(folderName))
print(fullPath)
remoteURL = 'git@github.com:'+username+'/'+folderName+'.git'
autoInit = True
privateRepo = False
token = os.environ['CODEWARS_GITHUB_TOKEN']


# to check if folder is git
def is_git_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False


# inialise if not already done(basicallly if it is first time)
if not is_git_repo(fullPath):
    os.chdir(fullPath)
    print('First')
    git.Repo.init(fullPath)
    print('second')
    subprocess.run(['git', 'branch', '-M', 'main'])
    print('third')
    subprocess.run(['git', 'remote', 'add', 'origin', remoteURL])
    print('fourht')
    subprocess.run(['curl', '-i', '-H', '"Authorization: token {}"'.format(token), '-d',
                   '{"name": "{}",  "auto_init": "{}",  "private": "{}"} https: // api.github.com/user/repos'.format(folderName, autoInit, privateRepo)])
    print('DOne')

# add new files and push them over
subprocess.run(['git', 'add', '.'])
print('Again First')
subprocess.run(['git', 'commit', '-m', 'added new files'])
print('Again Second')
subprocess.run('git push -u origin main', shell=True)
print('Again done')
# steps
# echo "# testttttt" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:pindio58/testttttt.git
# git push -u origin main
