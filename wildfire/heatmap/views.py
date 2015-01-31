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
        tweet_dict["searchterm"] = t.searchterm.encode('utf-8')
        tweet_dict["user"] = t.user.encode('utf-8')
        tweet_dict["sentiment"] = t.sentiment.encode('utf-8')
        tweet_dict["lat"] = t.lat
        tweet_dict["lng"] = t.lng
        tweet_dict["datetime"] = str(t.datetime)
        results.append(tweet_dict)
    return HttpResponse(json.dumps(results))

def access_all_tweets_json(q=''):
    results = []
    print q
    print len(tweet.objects.all())
    for t in tweet.objects.all():
        tweet_dict = {}
        print t.text
        if q in t.text:
            tweet_dict["sentiment"] = t.sentiment.encode('utf-8')
            tweet_dict["lat"] = t.lat
            tweet_dict["lng"] = t.lng
            tweet_dict["searchterm"] = t.searchterm.encode('utf-8')
            results.append(tweet_dict)
    return results

def index(request):
    return render_to_response("heatmap/home.html", {}, context_instance=RequestContext(request))

def heatmap(request):
    results = access_all_tweets_json()
    return render_to_response("heatmap/heatmap.html", {"tweets" : json.dumps(results)}, context_instance=RequestContext(request))

def twitter_input(request):
    if request.method != 'POST':
        get_tweets(request.GET['term'])
        results = access_all_tweets_json(request.GET['term'])
        return render_to_response("heatmap/heatmap.html", {"tweets" : json.dumps(results)}, context_instance=RequestContext(request))
    else:
        # fix CsrfViewMiddleware
        get_tweets(request.POST['term'])
        return HttpResponse("input submitted")
        # TODO: render map
        #return access_all_tweets(request)
