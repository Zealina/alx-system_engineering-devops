#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers"""
    headers = {'User-Agent': 'ZealinaHudson/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
