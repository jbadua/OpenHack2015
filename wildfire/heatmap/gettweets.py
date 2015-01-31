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

# def get_tweets(s = None, items = 45):
#     #counter to bypass google geocode limit
#     counter = 0
#     for tweepy_tweet in tweepy.Cursor(api.search,
#                                q = s,
#                                rpp = 100,
#                                result_type = "recent",
#                                include_entities = True,
#                                lang = "en").items(items):
#
#         t = tweet()
#         t.text = tweepy_tweet.text.encode('utf-8')
#         t.searchterm = s
#         t.sentiment = c(tweepy_tweet.text).encode('utf-8')
#         t.user = tweepy_tweet.user.screen_name.encode('utf-8')
#         t.datetime = tweepy_tweet.created_at
#         if tweepy_tweet.user.location is not None:
#             try:
#                 loc = Geocoder.geocode(tweepy_tweet.user.location)
#                 t.lat = loc[0].coordinates[0]
#                 t.lng = loc[0].coordinates[1]
#             except:
#                 pass
#             if counter == 5:
#                 time.sleep(0.25)
#                 counter = 0
#         t.save()
def get_tweets(s = None, items = 45):
    return
    cities = [
        {'lat': 47.37, 'lng': -122.20, 'r': 2},
        {'lat': 37.47, 'lng': -122.26, 'r': .3},
        {'lat': 34.03, 'lng': -118.11, 'r': 1},
        {'lat': 40.47, 'lng': -73.58, 'r': 1},
        {'lat': 32.46, 'lng': -96.46, 'r': 3},
        {'lat': 41.50, 'lng': -87.37, 'r': 1},
        {'lat': 41.28, 'lng': -87.37, 'r': 1},
        {'lat': 39.45, 'lng': -105, 'r': 10},
        {'lat': 39.18, 'lng': -76.38, 'r': 1},
        {'lat': 45.31, 'lng': -122.41, 'r': 1},
    ]
    terms = [
        'Microsoft',
        'Apple',
        'Democrat',
        'Republican',
        'Obama',
        'Ferguson',
        'Windows',
        'Mac',
        'Linux',
        'Starbucks',
    ]
    for i in range(50000):
        t = tweet()
        t.text = terms[int(random.random() * 10)]
        t.searchterm = t.text
        if random.random() < 0.8:
            t.sentiment = 'pos'
        else:
            t.sentiment = 'neg'
        t.user = ''
        t.datetime = ''
        r = int(random.random() * 10)
        radius = random.random() * cities[r]['r']
        angle = random.random() * 2 * math.pi
        t.lat = str(cities[r]["lat"] + math.cos(angle) * radius)
        t.lng = str(cities[r]["lng"] + math.sin(angle) * radius)
        t.save()
