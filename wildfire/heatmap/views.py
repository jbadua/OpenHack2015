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
        tweet_dict["text"] = t.searchterm.encode('utf-8')
        tweet_dict["user"] = t.user.encode('utf-8')
        tweet_dict["sentiment"] = t.sentiment.encode('utf-8')
        tweet_dict["lat"] = t.lat
        tweet_dict["lng"] = t.lng
        tweet_dict["datetime"] = str(t.datetime)
        results.append(tweet_dict)
    return HttpResponse(json.dumps(results))


def index(request):
    return render_to_response("heatmap/home.html", {}, context_instance=RequestContext(request))

def heatmap(request):
    results = []
    for t in tweet.objects.all():
        tweet_dict = {}
        tweet_dict["text"] = t.text.encode('utf-8')
        tweet_dict["text"] = t.searchterm.encode('utf-8')
        tweet_dict["user"] = t.user.encode('utf-8')
        tweet_dict["sentiment"] = t.sentiment.encode('utf-8')
        tweet_dict["lat"] = t.lat
        tweet_dict["lng"] = t.lng
        tweet_dict["datetime"] = str(t.datetime)
        results.append(tweet_dict)
    return render_to_response("heatmap/heatmap.html", {"tweets" : json.dumps(results)}, context_instance=RequestContext(request))

def twitter_input(request):
    if request.method != 'POST':
        try:
            get_tweets(request.GET['term'], request.GET['max'])
        except Exception as e:
            return HttpResponse(str(e))
        return HttpResponse("input submitted")
        # fix return
        #return access_all_tweets(request)
    else:
        # fix CsrfViewMiddleware
        get_tweets(request.POST['term'])
        return HttpResponse("input submitted")
        # TODO: render map
        #return access_all_tweets(request)
