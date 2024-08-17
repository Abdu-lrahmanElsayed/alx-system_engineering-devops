#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first 10 hot posts
"""
from requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    p = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    r = get(url, params=p)
    result = r.json()

    try:
        data = result.get('data').get('children')
        for i in data:
            print(i.get('data').get('title'))
    except Exception:
        print("None")
