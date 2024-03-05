#!/usr/bin/python3
"""top ten"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Toto"}
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print("None")
        return

    data = res.json()
    top = [post["data"]["title"] for post in data["data"]["children"][:10]]

    for title in top:
        print(title)
