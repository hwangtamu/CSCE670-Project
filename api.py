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
                                + 'include_entities=true&include_rts=true&user_id=' + str(q) + '&count=100')
        d = simplejson.loads(search.read())
        print q, len(d)
        if len(d) > 99:
            for tweet in d:
                data[tweet['created_at'][:20]] = tweet['text']
            with open('./verified/' + str(q) + '.json', 'w') as f:
                json.dump(data, f)

def getfollower(q):
    data = {}
    data['ids'] = []
    follower = urllib.urlopen('https://api.twitter.com/1/friends/ids.json?cursor=-1&user_id=' + str(q))
    follow = simplejson.loads(follower.read())
    for i in follow['ids']:
        data['ids'].append(i)
    while follow['next_cursor'] != 0:
        follower = urllib.urlopen('https://api.twitter.com/1/friends/ids.json?cursor='
                                  + follow['next_cursor_str'] + '&user_id=' + str(q))
        follow = simplejson.loads(follower.read())
        for i in follow['ids']:
            data['ids'].append(i)
    with open('./follower/' + str(q) + '.json', 'w') as f:
        json.dump(data, f)