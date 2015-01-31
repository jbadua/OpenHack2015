import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier

import os.path
nltk.data.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'nltk_data/'))

def extract_features(s):
    return dict([(word.lower(), True) for word in s])

class Classifier:
    def __init__(self):
        negfeats = [(extract_features(movie_reviews.words(fileids=[f])), 'neg') for f in movie_reviews.fileids('neg')]
        posfeats = [(extract_features(movie_reviews.words(fileids=[f])), 'pos') for f in movie_reviews.fileids('pos')]
        self.classifier = NaiveBayesClassifier.train(negfeats + posfeats)

    def __call__(self, tweet):
        return (self.classifier.classify(extract_features(tweet.split())))
