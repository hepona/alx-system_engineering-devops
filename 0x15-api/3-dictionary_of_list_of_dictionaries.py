#!/usr/bin/python3
"""0. Gather data from an API"""
import json
import requests as r
from sys import argv

if __name__ == "__main__":
    filename = "todo_all_employees.json"

    userdata = r.get(f"https://jsonplaceholder.typicode.com/users/")
    todouser = r.get(
        f"https://jsonplaceholder.typicode.com/\
todos/?userId="
    )
    user = json.loads(userdata.text)
    todo = json.loads(todouser.text)
    with open(filename, "w") as f:
        data = {
            i.get("userId"): [
                {
                    "task": i.get("title"),
                    "completed": i.get("completed"),
                    "username": user["username"],
                }
            ]
            for i in todo
        }
        json.dump(data, f)
