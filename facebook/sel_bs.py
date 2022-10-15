# Import the required modules 

import getpass
import os
import click 
import selenium 
from selenium import webdriver 
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import random
import time 
import requests

# Specify the facebooks URL 
url = "https://facebook.com"

# Specify credentials
current_user = getpass.getuser() 

if not current_user =='pilgrim':
    # Define resources to be used in the program 
    driver_path = "chromedriver.exe"
    input_username = "nkarietn@gmail.com"
    input_key = "Sibitary1#"  
else:
    # Define resources to be used in the program 
    driver_path = "chromedriver101.exe"
    input_username = "amroy776@gmail.com"
    input_key = "PB21@pilgrim" 

# Define the web driver and point it to the url of interest
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)


# Log in to the url using the given credentials
element= driver.find_element(by=By.ID, value= "email")
element.send_keys(input_username)
element= driver.find_element(by=By.ID, value="pass")
element.send_keys(input_key)
element.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

group = 'https://www.facebook.com/groups/952018951499518/' 

driver.get(group) 


soup=BeautifulSoup(driver.page_source,"html.parser")
all_posts=soup.find_all("div",{"class":"du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"})

for post in all_posts:
    print(post)
    try:
        name=post.find("a",{"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"}).text()
    except:
        name="not found"
    print(name) 

    