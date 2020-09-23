#!/usr/bin/python3
""" defines the count_words function """

from requests import get


def count_words(subreddit, word_list):
    """ prints word count for words in word list from titles of hot posts
        of a given subreddit. If no results are found, prints None.
    """
    if word_list is None or len(word_list) is 0:
        return

    get_titles = __import__('2-recurse').recurse
    titles = get_titles(subreddit)
    if titles is None:
        return
    results = []
    word_list = set(word_list)

    for word in word_list:
        sum = 0
        for title in titles:
            sum += title.lower().split().count(word.lower())

        if sum:
            results.append((word, sum))

    results.sort(key=lambda x: x[1], reverse=True)
    for result in results:
        print("{}: {}".format(result[0], result[1]))
