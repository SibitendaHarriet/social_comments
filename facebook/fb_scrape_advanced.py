# https://medium.com/nerd-for-tech/collecting-public-data-from-facebook-using-selenium-and-beautiful-soup-f0f918971000 

'''
Despite having an API, it is getting increasingly difficult to get data from Facebook — even the most transparent, public, basic information. Basically, anything that you are not an owner of is impossible to get without an app review, which makes life difficult to those needing social media data for academic research purposes as the development of an app is often not attainable or relevant, let alone the more convoluted review process. Unsatisfied with closed doors, I set out again to automatically get data from public Facebook pages. Readily available tools, such as this FB page scraper, are useful in getting the standard posts and basic metadata, but limited in other use cases, such as the one I have at hand — getting reviews from a public page together with all the comments and replies, such as this Universal Studios Hollywood page. These review data could be extremely helpful to competitor or benchmark analysis; insights could be generated from conducting text analysis or examining the interaction among the commenters, each of whom has an accessible social profile and varied social influence — another layer of analysis enabled by social networks.
After spending quite some time dissecting Facebook page structure and trying to figure out dozens of workarounds, this post is to serve as a summary of the process for myself and a showcase of the code (as of now) for anyone who might want to customize and build their own scrapers. It’s certainly a work in progress, as always in the case of web scraping. Sites are involving (FB especially) and better, smarter ways are always available. The following process is what made sense to me but may not be the most elegant or efficient. I’m leaving it here for any visitors or my future self to improve!
Pain points with collecting Facebook data include: 1) login required from the very beginning — no way around it; 2) many buttons to click in order to get sufficient (and usable) data, mainly of 2 types — “See More” and expand comments/replies (there are also “See More”’s in comments/replies); 3) it is not only hard to distinguish these buttons we want to click from the ones we don’t (FB’s HTML class naming is far from intuitive to begin with), but it is also very easy to accidentally click on an unwanted button that takes you entirely off track (and in my case, that means having to start over — I haven’t figured out an elegant way to solve this);
4) like many social media sites, there is no pagination, but infinite scroll, which could load rather slowly and unpredictably; 5) posts quickly “expire” after scrolling through, leaving a blank space with only a few active ones if you try to save HTML then (these stale posts as it turns out still exist, just invisible, so this can be an issue or not depending on your needs);
and 6) annoying hidden URL (that “#”) which becomes active only when being hovered over on an active page. I’m sure the list is longer, but let’s first leave it here.
In the meanwhile, all these data are open to public, visible on screen, but it takes too much time and energy for a manual collection. Without the API access, scraping becomes the only viable route. Therefore, the code below proposes a process that makes it possible to acquire at least some usable text data from this expansive pool of treasure.
Before we get started, as always, get the right version of the Chrome Driver and place it in the same folder (or provide a path to it). Then, the requirements for my purposes include:
'''

# selenium-related
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# other necessary ones
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
import re
import datetime


