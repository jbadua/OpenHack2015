import tweepy
import json
import time
from classifier import classifier
from pygeocoder import Geocoder
from models import tweet

# Oauth2
consumer_key = '5xexsRJABVUKsoLZhGUDElKrg'
consumer_secret = 'LXOtAnZQpTsid3FyYb7fNNDxcnXqxzbvqFt02dieDE60nbSIsO'
access_token = '989863279-rcASOGkZxbZXzRd6S6OPlVfCbzNHsPCD0oJHTmeP'
access_token_secret = 'VxKLxNuOgpVeoFXrbF495fSeJiKjZB2ZukbHGN9mdTkVK'

# authentication
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print 'Error - failure to initialize tweepy'

c = classifier()

def get_tweets(s = None):
    #counter to bypass google geocode limit
    counter = 0
    for tweepy_tweet in tweepy.Cursor(api.search,
                               q = s,
                               rpp = 100,
                               result_type = "recent",
                               include_entities = True,
                               lang = "en").items(10):

        t = tweet()
        t.text = tweepy_tweet.text.encode('utf-8')
        t.searchterm = s
        t.sentiment = c(tweepy_tweet.text).encode('utf-8')
        t.user = tweepy_tweet.user.screen_name.encode('utf-8')
        t.datetime = tweepy_tweet.created_at
        if(tweepy_tweet.user.location is not None):
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