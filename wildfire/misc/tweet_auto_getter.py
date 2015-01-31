import requests
import time

while True:
    print "Sending queries..."

    print "Getting http://127.0.0.1:8000/input?term=Linux&max=45"
    r = requests.get('http://127.0.0.1:8000/input?term=Linux&max=45')
    print r.status_code

    print "Getting http://127.0.0.1:8000/input?term=Democrat&max=45"
    r = requests.get('http://127.0.0.1:8000/input?term=Democrat&max=45')
    print r.status_code

    print "Getting http://127.0.0.1:8000/input?term=Republican&max=45"
    r = requests.get('http://127.0.0.1:8000/input?term=Republican&max=45')
    print r.status_code

    print "Getting http://127.0.0.1:8000/input?term=Google&max=45"
    r = requests.get('http://127.0.0.1:8000/input?term=Google&max=45')
    print r.status_code

    time.sleep(1000)

'''
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
'''