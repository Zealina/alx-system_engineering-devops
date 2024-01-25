#!/usr/bin/python3
"""Return the title of all the hot topics"""
import requests


def recurse(subreddit, hot_list=[]):
    """Recursively return the titles of all hot topics"""
    if hot_list == []:
