#!/usr/bin/python3
""" defines the count_words function """

from requests import get


def count_words(subreddit, word_list, last_post="", child=0):
    """ prints hot posts titles word count (case-insensitive) for
        words in word_list
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

    word_list = [word.lower() for word in word_list]
    word_dict = {word: word_list.count(word) for word in set(word_list)}
    freq_dict = {}
    for word, frequency in word_dict.items():
        word_dict[word] = 0
        for title in titles:
            word_dict[word] += title.lower().split().count(word) * frequency
        frequency = word_dict[word]
        entry = freq_dict.get(frequency)
        if entry is None:
            freq_dict.update({frequency: [word]})
        else:
            freq_dict[frequency].append(word)
    if 0 in freq_dict:
        del freq_dict[0]
    frequencies_of_words = sorted(freq_dict.items(), reverse=True)
    for frequency, words in frequencies_of_words:
        words.sort()
        for word in words:
            print('{}: {}'.format(word, frequency))
