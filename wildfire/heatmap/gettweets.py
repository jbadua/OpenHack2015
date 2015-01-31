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

'''
consumer_key = '1RXXDQ3SLzehbZN7BsEEtaKSH'
consumer_secret = 'apYkynrSy3QoWlnFwOsDHfjEDYJsZWanitEeNTijfHVmSOuNJ9'
access_token = '193893228-huzd54cY9JAgn8oUjTLfX8JqJEw5QDnqVEiAeNhw'
access_token_secret = 'ZU2bG3lKH28CcFO3AiWM9GNu2NMEnU97llJyebd7DLevW'
'''
'''
consumer_key = 'le4suBUUdkxInMWj5LJobEA7T'
consumer_secret = 'K4HH6tmOtIwc9rQav328UR8IbhqhlDrXaA9X9Xwlc41T5Fusgs'
access_token = '3004587368-MU18bd5RAPwFYFULqPjpqHCACxEgaFveHrMcT3H'
access_token_secret = 'l1GTfnKxFVuT1c2L4zkOmsmyPpdAeeuwkYTkWK1HTtLKl'
'''

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
                               lang = "en",
                               #geocode="39.5,-98.35,1500mi",
                               geocode="37.7833,-122.4167, 50mi",
                               wait_on_rate_limit_notify=True).items(30):

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