#!/usr/bin/python3
""" defines number_of_subscribers function """

from requests import get


def number_of_subscribers(subreddit):
    """
    returns number of subscribers (not active users, total subscribers)
    for a given subreddit.

    Note: If an invalid subreddit is given, the function returns 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    settings = {'allow_redirects': False, 'headers': {'User-agent': ''}}
    try:
        response = get(url, **settings).json()
        return response.get('data').get('subscribers')
    except:
        return 0
