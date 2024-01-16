#!/usr/bin/python3
"""Total Number of Subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ZealinaHudson/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json().get('data').get('subscribers'))
    return 0
