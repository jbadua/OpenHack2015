from django.shortcuts import render_to_response
from django.http import HttpResponse
from heatmap.models import tweet
import json

def access_all_tweets(request):
    results = []
    for t in tweet.objects.all():
        tweet_dict = {}
        tweet_dict["text"] = t.text.encode('utf-8')
        tweet_dict["user"] = t.user.encode('utf-8')
        tweet_dict["sentiment"] = t.sentiment.encode('utf-8')
        tweet_dict["lat"] = t.lat
        tweet_dict["lng"] = t.lng
        tweet_dict["datetime"] = str(t.datetime)
        results.append(tweet_dict)
    return HttpResponse(json.dumps(results))