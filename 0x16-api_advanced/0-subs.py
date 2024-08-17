#!/usr/bin/python3
"""
queries the Reddit API
and returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """The function"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        r = requests.get(url)
        result = r.json()
        return result.get('data').get('subscribers')
    except Exception:
        return 0
