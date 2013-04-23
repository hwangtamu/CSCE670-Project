__author__ = 'han'
import simplejson
from api import searchTweets

with open('./1.json', 'r') as f:
    d = simplejson.loads(f.read())
for i in d['ids'][400:]:
    searchTweets(i)
