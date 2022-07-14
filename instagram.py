# Firstly to try it out you got to type your username and password into instagramUserInfo.py  

from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome("C:/Users/zaurs/OneDrive/Masaüstü/Selenium/chromedriver.exe")
        self.username=username
        self.password=password
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/") 
        time.sleep(3)
        usernameInput=self.browser.find_element("xpath",'//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput=self.browser.find_element("xpath",'//*[@id="loginForm"]/div/div[2]/div/label/input')
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
    def getFollowers(self):
             self.browser.get(f"https://www.instagram.com/{self.username}")
             time.sleep(2)

             self.browser.find_element('xpath','//*[@id="mount_0_0_S4"]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/span').click()
             time.sleep(2)
             followers=self.browser.find_element('cssSelector','div[role=dialog] ul').find_element('cssSelector','li')
             for user in followers:
                link=user.find_element('cssSelector','a').get_attribute('href')
                print(link)

    
instgram=Instagram(username,password)
instgram.signIn()
instgram.getFollowers()  
