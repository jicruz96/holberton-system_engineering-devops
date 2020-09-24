#!/usr/bin/python3
""" defines the recurse function """

from requests import get
from json import dump
from urllib.parse import urlencode


def recurse(subreddit, **kwargs):
    """ returns list of all hot article titles for a given subreddit.
        If no results are found, returns None.
    """
    settings = {'allow_redirects': False, 'headers': {'User-agent': ''}}
    query = "?" + urlencode(kwargs)
    url = 'https://www.reddit.com/r/{}/hot.json{}'.format(subreddit, query)
    response = get(url, **settings).json().get('data')
    articles = response.get('children')
    after = response.get('after')
    print(after)
    titles = []
    for article in articles:
        titles.append(article['data']['title'])
    query_options = {'limit': 100, 'after': after}
    if after is not None:
        more_titles = recurse(subreddit, **query_options)
        titles += more_titles
    return titles
