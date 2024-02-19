#!/usr/bin/python3
"""0. Gather data from an API"""
import json
import requests as r
from sys import argv

if __name__ == "__main__":
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
        print(
            f"Employee {user.get('name')} is done with \
tasks({len(c_completed_task)}/{len(todo)}):"
        )
        for t in c_completed_task:
            print("\t " + t.get("title"))
