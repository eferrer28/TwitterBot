import requests
import random
import time
import tweepy
from secrets import *

#url = "http://numbersapi.com/58"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#create api instance

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

def randomNum():


def getFacts():
    try:
        r = requests.get('http://numbersapi.com/58')
        print r.text
        #return r.json()
    except IOError:
        print "error"

randomNum()

getFacts()
