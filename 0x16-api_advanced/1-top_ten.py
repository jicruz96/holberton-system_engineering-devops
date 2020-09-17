#!/usr/bin/python3
""" defines the top_ten function """

from requests import get
from urllib.parse import urlencode


def top_ten(subreddit):
    """ Returns the titles of the top 10 hot posts for a given subreddit """

    settings = {'allow_redirects': False, 'headers': {'User-agent': ''}}
    url = "https://www.reddit.com/r/{}/hot.json"
    url = url.format(subreddit)
    print(url)
    try:
        responses = get(url, **settings).json().get('data').get('children')
        posts = [post['data']['title'] for post in responses][:10]
        for post in posts:
            print(post)
    except:
        print("None")
