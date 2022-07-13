# Firstly to try it out you got to type your email adress and password into instagramUserInfo.py  

from instagramUserInfo import email,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self,email,password):
        self.browser=webdriver.Chrome("C:/Users/zaurs/OneDrive/Masaüstü/Selenium/chromedriver.exe")
        self.email=email
        self.password=password
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/") 
        time.sleep(3)
        emailInput=self.browser.find_element("xpath",'//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput=self.browser.find_element("xpath",'//*[@id="loginForm"]/div/div[2]/div/label/input')
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

instgram=Instagram(email,password)
instgram.signIn()


# //*[@id="loginForm"]/div/div[2]/div/label/input