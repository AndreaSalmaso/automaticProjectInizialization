import sys, subprocess
from selenium import webdriver

repoName = sys.argv[1]

# your GitHub credentials
USERNAME = sys.argv[2]
PASSWORD = ""

browser = webdriver.Chrome()
browser.get("https://github.com/login")

def create():
    browser.find_element_by_id('login_field').send_keys(USERNAME)
    browser.find_element_by_id('password').send_keys(PASSWORD)
    browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]').click()
    browser.get('https://github.com/new')
    browser.find_element_by_id('repository_name').send_keys(repoName)
    browser.find_elements_by_xpath('//div[@class="js-with-permission-fields"]/button')[0].submit()
    
    browser.close()


create()
