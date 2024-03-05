#!/usr/bin/python3
"""Recurse it"""
import requests


def recurse(subreddit, hot_list=[], c=0):
    """Prints the titles of the first 10 hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Toto"}
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return
    data = res.json()
    if c <= 10:
        hot_list.append(data["data"]["children"][c]["data"]["title"])
        recurse(subreddit, hot_list, c+1)
    return hot_list
    # top = [post["data"]["title"] for post in data["data"]["children"][:10]]

    # for title in top:
    #     print(title)
