#!/usr/bin/python3
"""2-export_to_JSON.py"""
import json
import requests as r
from sys import argv

if __name__ == "__main__":
    filename = argv[1] + ".json"
    id = argv[1]

    if len(argv) != 2 or not id.isdigit():
        print("Usage: ./2-export_to_JSON.py <number>")
    else:
        userdata = r.get(f"https://jsonplaceholder.typicode.com/users/{id}")
        todouser = r.get(
            f"https://jsonplaceholder.typicode.com/\
todos/?userId={id}"
        )
        user = json.loads(userdata.text)
        todo = json.loads(todouser.text)
        # print(user.values())
        with open(filename, "w") as f:
            data = {
                id: [
                    {
                        "task": i.get("title"),
                        "completed": i.get("completed"),
                        "username": user["username"],
                    }
                    for i in todo
                ]
            }
            json.dump(data, f)
