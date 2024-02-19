#!/usr/bin/python3
"""1. Export to CSV"""
import json
import requests as r
from sys import argv

if __name__ == "__main__":
    filename = "USER_ID.csv"
    id = argv[1]

    if len(argv) != 2 or not id.isdigit():
        print("Usage: ./0-gather_data_from_an_API <number>")
    else:
        userdata = r.get(f"https://jsonplaceholder.typicode.com/users/{id}")
        todouser = r.get(
            f"https://jsonplaceholder.typicode.com/\
todos/?userId={id}"
            )
        user = json.loads(userdata.text)
        todo = json.loads(todouser.text)
        c_completed_task = [task for task in todo if task["completed"] is True]
        c = 0
        username = user['username']
        with open(filename, 'w') as f:
            for i in todo:
                f.write(f"\"{i.get('userId')}\",\"{username}\",\
\"{i.get('completed')}\",\"{i.get('title')}\"\n")
            f.close()
