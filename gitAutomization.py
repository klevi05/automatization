import json
from time import sleep
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
        chrome_options.headless = True
        driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        driver.get("https://www.github.com/login")
        driver.maximize_window()
        sleep(2)
        username = driver.find_element_by_name("login")
        password = driver.find_element_by_name("password")
        log_in = driver.find_element_by_name("commit")
        username.send_keys(self.username)
        sleep(2)
        password.send_keys(self.password)
        sleep(2)
        log_in.send_keys(Keys.RETURN)
        sleep(2)
        driver.get("https://www.github.com/new")
        sleep(2)
        driver.find_element_by_name('repository[name]').send_keys(self.repository_name)
        sleep(2)
        driver.find_element_by_id('repository_auto_init').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/summary').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/div/div/div[1]/ul/li/a').click()
        sleep(7)


with open('user.json', 'r') as P:
    information = json.load(P)
    context = information['te_dhena']
    data = context[0]
    name = data['username']
    passw = data['password']

repository = input('Enter the repository name: ')
start = GIT(repository, name, passw)
start.Login()
