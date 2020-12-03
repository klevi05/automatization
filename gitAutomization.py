import json
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GIT:
    def __init__(self, repository_name, username, password):
        self.repository_name = repository_name
        self.username = username
        self.password = password

    def Login(self):
        chrome_options = Options()
        chrome_options.headless = False
        driver = webdriver.Chrome(executable_path='C:\\webdriver\\chromedriver_win32\\chromedriver.exe', options=chrome_options)
        driver.get("https://www.github.com/login")
        driver.maximize_window()
        time.sleep(5)
        username = driver.find_element_by_name("login")
        password = driver.find_element_by_name("password")
        log_in = driver.find_element_by_name("commit")
        username.send_keys(self.username)
        time.sleep(2)
        password.send_keys(self.password)
        time.sleep(2)
        log_in.send_keys(Keys.RETURN)
        time.sleep(5)
        new_repo = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
        time.sleep(6)
        new_repo.send_keys(self.repository_name)
        time.sleep(600)


with open('user.json', 'r') as P:
    information = json.load(P)
    context = information['te_dhena']
    data = context[0]
    name = data['username']
    passw = data['password']

repository = input('Enter the repository name: ')
start = GIT(repository,name,passw)
start.Login()

