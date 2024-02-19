#!/usr/bin/python3
import requests as r
from sys import argv

try:
    if len(argv) != 2 or not isinstance(int(argv[1]), int):
        print("Usage: ./0-gather_data_from_an_API <number>")
    else:
        url = r.get(f"https://jsonplaceholder.typicode.com/todos/{argv[1]}")
        print(url.text)
except Exception as e:
    print(e)
