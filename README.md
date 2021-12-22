# Overview

I usually practice my python skills at [code wars](https://www.codewars.com/users/sign_in). Few of solutions I implemented there are on my GitHub profile.
This project has been created , as webscrapping practice, to scrap all the solutions and generate the code file(s) , be it python, java etc and also generate their respective MarkDown files.

### How it works

It will create a directory `codewarsProjects`  at your home page having all the projects scrapped. Further, it will create directories based on the languages used to implement solutions. Then scarpped solutions and thier `README` files will be placed in respective directory. See image at the end  for the clear picture.
There are technically three steps:

* **Login**
  * One of the available options at codewars to login is using GitHub account, which I use. This project will use that option.

* **Scroll down**
  * This will go to the 'solutions' tab and scroll down the screen until all solutions are visible on screen.

* **Scrap**
  * This will scrap the question name, which will also be used as directory name
  * Scrap the accepted solution code and generate the file with requited extension (e.g. .py, .sql).
  * Generate the README file. This file will have whatever details about the question are given on the site.

### How to use

* Install the dependencies from `requirements.txt` file.
* Download the chrome driver and set the path to environament variable, named `DRIVERFULLPATH`.
* Run `origin.py` under `final` folder.

### Login Methods

There are two different ways to login:

* **Username and password:** Here also, two ways.

  * Either set the username and password in `config.py` under cfg folder.
  * By default, it will ask for username and password on CLI.
* **Cookies:**
  * For this method, you will need to store cookies into a csv file (`cookies.csv`) under `lgn` directory when you have manually logged in. Please refer [here](https://www.youtube.com/watch?v=vhjKJ7huN-w) how to do it.
  * Once stored, please go to `login.py` file and do the follwoing:
    * Comment out `self.logInUsingUserPass(EMAILFIELD, PASSWORDFIELD)`.
    * Uncomment `self.loggedinusingCookies()`.

### Final structure

* After successfully running it, a nice directory will be created like below:
  
<img src="img/struct.png?raw=true" alt="drawing" width="700" align="right"/>
