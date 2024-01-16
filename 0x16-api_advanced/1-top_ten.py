#!/usr/bin/python3
"""Top ten posts in subreddit"""

import requests


def top_ten(subreddit):
    """Return top topics in subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ZealinaHudson/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
