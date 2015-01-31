import tweepy
import json
import math
import time
import random
from classifier import Classifier
from pygeocoder import Geocoder
from models import tweet
from confidential import consumer_key, consumer_secret, access_token, access_token_secret

# authentication
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print 'Error - failure to initialize tweepy'

c = Classifier()

def get_tweets(s = None, items = 45):
    #counter to bypass google geocode limit
    counter = 0
    for tweepy_tweet in tweepy.Cursor(api.search,
                               q = s,
                               rpp = 100,
                               result_type = "recent",
                               include_entities = True,
                               lang = "en").items(items):

        t = tweet()
        t.text = tweepy_tweet.text.encode('utf-8')
        t.searchterm = s
        t.sentiment = c(tweepy_tweet.text).encode('utf-8')
        t.user = tweepy_tweet.user.screen_name.encode('utf-8')
        t.datetime = tweepy_tweet.created_at
        if tweepy_tweet.user.location is not None:
            try:
                loc = Geocoder.geocode(tweepy_tweet.user.location)
                t.lat = loc[0].coordinates[0]
                t.lng = loc[0].coordinates[1]
            except:
                pass
            if counter == 5:
                time.sleep(0.25)
                counter = 0
        t.save()