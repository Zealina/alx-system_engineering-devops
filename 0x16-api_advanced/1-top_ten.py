#!/usr/bin/python3
"""The top ten hot posts titles"""
import requests


def top_ten(subreddit):
    """Return the titles of the top ten hottest posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ZealinaHudson/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        data = data['data']['children']
        count = 0
        for entry in data:
            print(entry['data']['title'])
            count += 1
            if count == 10:
                return
