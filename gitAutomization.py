from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class GIT:
    def __init__(self,kenga):
        self.kenga = kenga

    def entry(self):
        chrome_options = Options()
        chrome_options.headless = False
        driver = webdriver.Chrome(executable_path='C:\\webdriver\\chromedriver_win32\\chromedriver.exe', options=chrome_options)
        driver.get("https://www.youtube.com/")
        time.sleep(3)
        search = driver.find_element_by_name('search_query')
        button = driver.find_element_by_id('search-icon-legacy')
        search.send_keys(self.kenga)
        time.sleep(2)
        button.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.quit()


start = GIT("the weekend")
start.entry()
