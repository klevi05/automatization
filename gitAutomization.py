import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class GIT:
    def __init__(self, repository_name, username, password):
        self.repository_name = repository_name
        self.username = username
        self.password = password

    def Login(self):
        chrome_options = Options()
        chrome_options.headless = False
        driver = webdriver.Chrome(executable_path='C:\\webdriver\\chromedriver_win32\\chromedriver.exe', options=chrome_options)
        driver.get("https://www.github.com/")
        time.sleep(3)


with open('user.json', 'r') as P:
    information = json.load(P)
    context = information['te_dhena']
    data = context[0]
    username = data['username']
    password = data['password']

repository = input('Enter the repository name: ')
start = GIT(repository,username,password)
start.Login()

