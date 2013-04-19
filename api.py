__author__ = 'hanwang'
import urllib
import simplejson, json


def searchTweets(q):
    data = {}
    user = urllib.urlopen('https://api.twitter.com/1/users/show.json?user_id='
                          + str(q) + '&TwitterAPI&include_entities=true')
    u = simplejson.loads(user.read())
    print '.'
    if 'lang' in u and u['lang'] == 'en':
        search = urllib.urlopen('https://api.twitter.com/1/statuses/user_timeline.json?'
                                + 'include_entities=true&include_rts=true&user_id=' + str(q) + '&count=101')
        d = simplejson.loads(search.read())
        print q, len(d)
        if len(d) > 99:
            for tweet in d:
                data[tweet['created_at'][:20]] = tweet['text']
            with open('./json/' + str(q) + '.json', 'w') as f:
                json.dump(data, f)


if __name__ == '__main__':
    s = 54000080
    while s < 60000000:
        searchTweets(s)
        s += 1