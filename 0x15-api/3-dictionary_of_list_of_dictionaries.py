#!/usr/bin/python3
"""0. Gather data from an API"""
import json
import requests as r
from sys import argv

if __name__ == "__main__":
    filename = "todo_all_employees.json"
    data = {}
    userdata = r.get(f"https://jsonplaceholder.typicode.com/users/")
    todouser = r.get(f"https://jsonplaceholder.typicode.com/todos")
    user = json.loads(userdata.text)
    todo = json.loads(todouser.text)
    # for i in user:
    #     print(i.get("id"))
    # for t, u in zip(todo, user):
    #     data[u.get("id")]= [
    #         {
    #             "task": t.get("title"),
    #             "completed": t.get("completed"),
    #             "username": u.get("username"),
    #         }
    #     ]
    #     print(data)
    with open(filename, "w") as f:
        for t, u in zip(todo, user):
            data[u.get("id")] = [
                {
                    "username": u.get("username"),
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                }
            ]
            print(data)
            json.dump(data, f)
