from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from heatmap.models import tweet
import json
from gettweets import get_tweets

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

def access_all_tweets_json(q):
    results = []
    for t in tweet.objects.all():
        tweet_dict = {}
        if q in t.text:
            tweet_dict["sentiment"] = t.sentiment.encode('utf-8')
            tweet_dict["lat"] = t.lat
            tweet_dict["lng"] = t.lng
            results.append(tweet_dict)
    return results

def index(request):
    return render_to_response("heatmap/home.html", {}, context_instance=RequestContext(request))

def heatmap(request, positive=None, negative=None):
    tweets = {'positive': positive, 'negative': negative}
    return render_to_response("heatmap/heatmap.html", tweets, context_instance=RequestContext(request))

def twitter_input(request):
    if request.method != 'POST':
        get_tweets(request.GET['term'])
        tweets = access_all_tweets_json(request.GET['term'])
        positive = []
        negative = []
        for t in tweets:
            output = json.dumps(t)
            if t['sentiment'] == 'neg':
                negative.append(output)
            else:
                positive.append(output)
        return heatmap(request, positive, negative)
    else:
        # fix CsrfViewMiddleware
        get_tweets(request.POST['term'])

        # TODO: render map
        return access_all_tweets(request)
