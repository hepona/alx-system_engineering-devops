#!/usr/bin/python3
"""1. Export to CSV"""
import json
import requests as r
from sys import argv

if __name__ == "__main__":
    filename = argv[1]+".csv"

    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./1-export_to_CSV <number>")
    else:
        id = argv[1]
        userdata = r.get(f"https://jsonplaceholder.typicode.com/users/{id}")
        todouser = r.get(
            f"https://jsonplaceholder.typicode.com/\
todos/?userId={id}"
            )
        user = json.loads(userdata.text)
        todo = json.loads(todouser.text)
        username = user['username']
        with open(filename, 'w') as f:
            for i in todo:
                f.write(f"\"{i.get('userId')}\",\"{username}\",\
\"{i.get('completed')}\",\"{i.get('title')}\"\n")
            f.close()
