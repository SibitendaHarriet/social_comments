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
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Define the web driver and point it to the url of interest
driver = webdriver.Chrome(executable_path=driver_path,options=option)
driver.get(url)


driver.maximize_window()
wait = WebDriverWait(driver, 30)
email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
email_field.send_keys(input_username)
pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
pass_field.send_keys(input_key)
pass_field.send_keys(Keys.RETURN)

#time.sleep(5)

driver.get('URL') # once logged in, free to open up any target page

time.sleep(5)
# Log in to the url using the given credentials
element= driver.find_element(by=By.ID, value= "email")
element.send_keys(input_username)
element= driver.find_element(by=By.ID, value="pass")
element.send_keys(input_key)
element.send_keys(Keys.RETURN)

driver.implicitly_wait(30)

# Specify query 
query ='poverty 'and' senegal' 

xpath_search = "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/label/input"
selector_search = '#mount_0_0_A9 > div > div:nth-child(1) > div > div:nth-child(4) > div.rq0escxv.byvelhso.q10oee1b.poy2od1o.j9ispegn.kr520xx4.ajzd4i4n.ru5i1254.mhnrfdw6.cwj9ozl2 > div > div > div.bp9cbjyn.rq0escxv.j83agx80.byvelhso.hv4rvrfc.dati1w0a > div > div > label > input'
driver.implicitly_wait(100)
search = driver.find_element(by =By.XPATH,  value =xpath_search)
search.send_keys(query)  
search.send_keys(Keys.RETURN) 
driver.implicitly_wait(30)

#driver.send_keys(Keys.ESCAPE)

driver.implicitly_wait(100)
posts = driver.find_elements(by= By.CSS_SELECTOR, value='#mount_0_0_Ep > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.pfnyh3mw.jifvfom9.gs1a9yip.owycx6da.btwxx1t3.j83agx80.buofh1pr.dp1hu0rb.l9j0dhe7.du4w35lb.ka73uehy > div.rq0escxv.l9j0dhe7.du4w35lb.cbu4d94t.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.g5gj957u.j83agx80.dp1hu0rb > div > div > div > div > div > div:nth-child(3) > div')
driver.implicitly_wait(100) 
print(posts) 
for post in posts:
    print(post) 
