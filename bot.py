 #!/usr/bin/env python

import requests
import random
import time
import tweepy
from secrets import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#create api instance

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

def randomNum():
    return str(random.randrange(1,250))


def getFacts(num):
    try:

        #print num - debug
        r = requests.get(url + num)
        print r.text
        return r.text
    except IOError:
        print "error"

def postTweet(msg):
    if(len(msg) > 140):
        print "too long"
        number = randomNum()
        tweet = getFacts(msg)
        postTweet(tweet)
        api.update_status(tweet)
    else:
        api.update_status(msg)


number = randomNum()
tweet = getFacts(number)
postTweet(tweet)

print len(tweet)
print tweet

#api.update_status(tweet)
