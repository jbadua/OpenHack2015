import requests

while True:
    print "Sending queries..."

    print "Getting http://127.0.0.1:8000/input?term=Apple&max=45"
    r = requests.get('http://127.0.0.1:8000/input?term=Apple&max=45')
    print r.status_code

    print "Getting http://127.0.0.1:8000/input?term=Mac&max=45"
    r = requests.get('http://127.0.0.1:8000/input?term=Mac&max=45')
    print r.status_code

    print "Getting http://127.0.0.1:8000/input?term=Windows&max=45"
    r = requests.get('http://127.0.0.1:8000/input?term=Windows&max=45')
    print r.status_code

    print "Getting http://127.0.0.1:8000/input?term=Microsoft&max=45"
    r = requests.get('http://127.0.0.1:8000/input?term=Microsoft&max=45')
    print r.status_code

    time.sleep(1000)
