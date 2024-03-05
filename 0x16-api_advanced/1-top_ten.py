#!/usr/bin/python3
"""top ten"""
import requests

def top_ten(subreddit):
    """top ten posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url)
    if res.status_code != 200:
        return None
    data = res.json()
    top = []
    for i in range(10):
        top.append(data["data"]["children"][i]["data"]["title"])
    return print(top)
