import git
import pathlib
from github.GithubException import UnknownObjectException
from github import Github
import subprocess
import os
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from cfg.config import folderName, username


# path of our project folder and take token
fullPath = str(pathlib.Path.home().joinpath(folderName))
token = os.environ['CODEWARS_GITHUB_TOKEN']
IS_PRIVATE = True                                                        # Change this accordingly whether the pushed repo should be public or private


class pushToGitHub:

    def __init__(self):
        pass

    # to check if folder is git
    def is_git_repo(self, path):
        '''This will return boolean whether the given folder is a git repo not'''
        try:
            _ = git.Repo(path).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    # Create new remote repo
    def create_repo(self, folderName):
        '''This will create a repository on github using provided username and token'''
        self.repo = Github(token)
        self.user = self.repo.get_user()
        try:
            self.user.get_repo(folderName).delete()
        except UnknownObjectException:
            pass
        self.user.create_repo(folderName, private=IS_PRIVATE)

    # Change path
    def change_path(self):
        os.chdir(fullPath)

    # Inialise if not already done(basicallly if it is first time)
    def init_and_create(self, fullPath, folderName):
        '''This will do the following:\n
                \tInitialize the git in folder\n
                \tCall the function create_repo internally
        '''
        if not self.is_git_repo(fullPath):
            git.Repo.init(fullPath)
            self.create_repo(folderName)

    def add_commit_push(self, username, token, folderName):
        '''After changnig path to the required folder, will add and push all new,modified files'''
        # FIXME  mask the output since it is showing the token on screen
        subprocess.call(['git', 'add', '.'])
        subprocess.call(
            ['git', 'commit', '-m', '{}'.format('adding new files')])
        subprocess.call(['git', 'branch', '-M', 'main'])
        subprocess.call(
            ['git', 'push', '--set-upstream', 'https://{0}:{1}@github.com/{0}/{2}.git'.format(username, token,  folderName), 'main'])

    def final(self):
        self.change_path()
        self.init_and_create(fullPath, folderName)
        self.add_commit_push(username, token, folderName)


if __name__ == '__main__':
    push = pushToGitHub()
    push.final()
