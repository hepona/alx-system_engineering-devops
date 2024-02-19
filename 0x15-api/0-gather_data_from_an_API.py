#!/usr/bin/python3
"""0. Gather data from an API"""
import json
import requests as r
from sys import argv

# try:
if len(argv) != 2 or not argv[1].isdigit():
    print("Usage: ./0-gather_data_from_an_API <number>")
else:
    userdata = r.get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    todouser = r.get("https://jsonplaceholder.typicode.com/todos/")
    user = json.loads(userdata.text)
    todo = json.loads((todouser.text))
    # print((todo))
    count_completed_task = 0
    count_tot_task = 0
    for t in todo:
        if t["userId"] == int(argv[1]):
            count_tot_task += 1
            if t["completed"]:
                count_completed_task += 1
    print(
        f"Employee {user['name']} is done with tasks({count_completed_task}/{count_tot_task}):"
    )
    for t in todo:
        # print(t["title"])
        if t["userId"] == int(argv[1]) and t["completed"] == True:
            print("     ",t["title"])
# except Exception as e:
#     print(e)
