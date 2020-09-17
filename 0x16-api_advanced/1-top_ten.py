#!/usr/bin/python3
""" defines the top_ten function """

from requests import get


def top_ten(subreddit):
    """ Returns the titles of the top 10 hot posts for a given subreddit """

    settings = {'allow_redirects': False, 'headers': {'User-agent': ''}}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        responses = get(url, **settings).json().get('data').get('children')
        for post in responses[:10]:
            print(post['data']['title'])
    except:
        print("None")
