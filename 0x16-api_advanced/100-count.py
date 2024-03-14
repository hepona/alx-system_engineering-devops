#!/usr/bin/python3
"""Count it!"""
import requests


def count_words(subreddit,word_list, c=0):
    """Prints the titles of the first 10 hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Toto"}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return
    data = res.json()
    titles = data["data"]["children"][c]["data"]["title"].split(sep= " ")
    if c < len(titles) and titles[c] == word_list:
            print(f"{titles[c]} : {titles.count(titles[c])}")
    count_words(subreddit, word_list, c+1)

