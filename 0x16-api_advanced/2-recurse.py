#!/usr/bin/python3
""" defines the recurse function """

from requests import get


def recurse(subreddit, last_post="", hot_list=[]):
    """ returns list of all hot article titles for a given subreddit.
        If no results are found, returns None.
    """
    try:
        if last_post is None:
            return hot_list
        query = "?limit=100&after=" + last_post
        url = "https://www.reddit.com/r/{}/hot.json{}".format(subreddit, query)
        settings = {'headers': {'User-agent': ''}, 'allow_redirects': False}
        data = get(url, **settings).json().get('data')
        hot_list += [post['data']['title'] for post in data.get('children')]
        return recurse(subreddit, data['after'], hot_list)
    except:
        return None
