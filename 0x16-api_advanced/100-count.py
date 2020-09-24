#!/usr/bin/python3
""" defines the count_words function """
from requests import get


def count_words(subreddit, word_list, last_post="", child=0):
    """ returns list of all hot article titles for a given subreddit.
        If no results are found, returns None.
    """
    try:
        if last_post is None:
            return []
        query = "?limit=100&after=" + last_post
        url = "https://www.reddit.com/r/{}/hot.json{}".format(subreddit, query)
        settings = {'headers': {'User-agent': ''}, 'allow_redirects': False}
        data = get(url, **settings).json().get('data')
        titles = [post['data']['title'] for post in data.get('children')]
        titles = titles + count_words(subreddit, word_list, data['after'], 1)
        if child:
            return titles
    except:
        print()
        return

    results = {}
    for word in word_list:
        word = word.lower()
        n = 0
        for title in titles:
            n += title.lower().split().count(word)
        l = results.get(n)
        if l is None:
            results.update({n: {word}})
        else:
            results[n].add(word)

    nums = list(results.keys())
    if 0 in nums:
        nums.remove(0)
    if len(nums):
        nums.sort(reverse=True)
    for num in nums:
        words = list(results[num])
        words.sort()
        for word in words:
            print('{}: {}'.format(word, num))
