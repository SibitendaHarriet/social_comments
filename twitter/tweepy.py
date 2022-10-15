#!/usr/bin/env python
# -*- coding: utf-8 -*-
# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
#Creating a Twitter App

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
CONSUMER_KEY  = "kQTCXBR9IZ0701XGeuRaSyaLk"
CONSUMER_SECRET = "I0WlvVckzLQkL8oEOTnf2FSkQuVwHlPtxlXY2jfhg5a90UGPNO"
ACCESS_TOKEN = "1178714592-faLaBikVh1f9RaBm8VV3y16iuNHxfs0XuhVH7St"
ACCESS_SECRET = "GaxWepA5YxeFChVPtjCsLUVNn3PB3Skg7ZhbPqRvRRHad"

query = 'covid-19'
#method to get a user's last tweets
def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
    #query = 'covid-19'

	#set count to however many tweets you want
	number_of_tweets = 10

	#get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        #create array of tweet information: username, tweet id, date/time, text
		tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])

	#write to a new csv file from the array of tweets
	outfile = username + "_tweets.csv"
	print ("writing to ") + outfile
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)


#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print ("Error: enter one username")

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)