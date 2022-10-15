#https://towardsdatascience.com/how-to-scrape-youtube-comments-with-python-61ff197115d4
# https://medium.com/analytics-vidhya/extracting-youtube-comments-using-selenium-b29ee4f743ef
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os
import csv
import pandas as pd 
from math import ceil
import getpass


current_user = getpass.getuser() 

if not current_user =='pilgrim':
    # Define resources to be used in the program 
    driver_path = "C:/chromedriver_win32/chromedriver.exe"
  
else:
    # Define resources to be used in the program 
    driver_path = "chromedriver.exe"


url = "https://www.youtube.com/watch?v=UGe_eK12OVw" 
youtube_pages = "https://www.youtube.com/"

# Define the web driver and point it to the url of interest
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(youtube_pages)
permission_to_proceed = input('Press y to proceed:') 

if permission_to_proceed=='y':
    # Creates a new .csv file that the data will be written to

    csv_file = open('output_scraping.csv', 'w', encoding="UTF-8", newline="")
    writer = csv.writer(csv_file) 

    # write header names
    writer.writerow(
        ['url', 'link_title', 'channel', 'no_of_views', 'time_uploaded', 'comment', 'author', 'comment_posted', 
        'no_of_replies','upvotes','downvotes'])


    print("=" * 40)  # Shows in terminal when youtube summary page with search keyword is being scraped
    print("Scraping " + youtube_pages)
    search = driver.find_element_by_id('search')
    search.send_keys("Kishore Kumar")    
    driver.find_element_by_id('search-icon-legacy').click()
    time.sleep(20)    
    vtitle = driver.find_elements_by_id('video-title')
    subscription = driver.find_elements_by_id('byline')
    for element in subscription:
        print(element.text)
        

views = driver.find_elements_by_xpath('//div[@id="metadata-line"]/span[1]')
for element in views:
    print(element.text)
posted = driver.find_elements_by_xpath('//div[@id="metadata-line"]/span[2]')
for element in posted:
    print(element.text)

tcount = 0
href = []
title = []
channel = []
numview = []
postdate = []
    
while tcount < 10:
    href.append(vtitle[tcount].get_attribute('href'))
    channel.append(subscription[tcount].get_attribute('title'))
    title.append(vtitle[tcount].text)
    numview.append(views[tcount].text)
    postdate.append(posted[tcount].text)  
    tcount = tcount +1
print(href, channel, title, numview, postdate)


# launch top ten extracted links and extract comment details
tcount = 0    
while tcount < 10:  
    youtube_dict ={}
    # extract comment section of top ten links
    url = href[tcount]
    print (url)
    driver.get(url)
    time.sleep(5)
    
    try:
        print("+" * 40)  # Shows in terminal when details of a new video is being scraped
        print("Scraping child links ")
        #scroll down to load comments
        driver.execute_script('window.scrollTo(0,390);')
        time.sleep(15)
        #sort by top comments
        sort= driver.find_element_by_xpath("""//*[@id="icon-label"]""")
        sort.click()
        time.sleep(10)
        topcomments =driver.find_element_by_xpath("""//*[@id="menu"]/a[1]/paper-item/paper-item-body/div[1]""")
        topcomments.click()
        time.sleep(10)
        # Loads 20 comments , scroll two times to load next set of 40 comments. 
        for i in range(0,2):
            driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,document.documentElement.clientHeight))")
            time.sleep(10)
        
        #count total number of comments and set index to number of comments if less than 50 otherwise set as 50. 
        totalcomments= len(driver.find_elements_by_xpath("""//*[@id="content-text"]"""))
        
        if totalcomments < 50:
            index= totalcomments
        else:
            index= 50 
            
        ccount = 0
        while ccount < index: 
            try:
                comment = driver.find_elements_by_xpath('//*[@id="content-text"]')[ccount].text
            except:
                comment = ""
            try:
                authors = driver.find_elements_by_xpath('//a[@id="author-text"]/span')[ccount].text
            except:
                authors = ""
            try:
                comment_posted = driver.find_elements_by_xpath('//*[@id="published-time-text"]/a')[ccount].text
            except:
                comment_posted = ""
            try:
                replies = driver.find_elements_by_xpath('//*[@id="more-text"]')[ccount].text                    
                if replies =="View reply":
                    replies= 1
                else:
                    replies =replies.replace("View ","")
                    replies =replies.replace(" replies","")
            except:
                replies = ""
            try:
                upvotes = driver.find_elements_by_xpath('//*[@id="vote-count-middle"]')[ccount].text
            except:
                upvotes = ""
                    
            youtube_dict['url'] = href[tcount]
            youtube_dict['link_title'] = title[tcount]
            youtube_dict['channel'] = channel[tcount]
            youtube_dict['no_of_views'] = numview[tcount]
            youtube_dict['time_uploaded'] =  postdate[tcount]
            youtube_dict['comment'] = comment
            youtube_dict['author'] = authors
            youtube_dict['comment_posted'] = comment_posted
            youtube_dict['no_of_replies'] = replies
            youtube_dict['upvotes'] = upvotes
            
            writer.writerow(youtube_dict.values())
            ccount = ccount +1
            
    except Exception as e:
        print(e)
        driver.close()
    tcount = tcount +1 
print("Scrapping process Completed")   
csv_file.close()    


