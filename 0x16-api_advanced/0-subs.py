#!/usr/bin/python3
"""num of subs"""
import requests


def number_of_subscribers(subreddit):
    """return num of subs, 0 otherwise"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url)
    if res.status_code != 200:
        return 0
    data = res.json()
    return data["data"]["subscribers"]
