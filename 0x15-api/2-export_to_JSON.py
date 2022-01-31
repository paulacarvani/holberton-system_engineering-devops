#!/usr/bin/python3
""" import a json file"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]

    """REST API url"""
    url = "https://jsonplaceholder.typicode.com/"

    """gets for users info like name, id, tasks todo"""

    """Match the argv with the id in tables of users and
    todos of the rest api"""
    users = requests.get(url + "users/", params={"id": id}).json()
    tasks = requests.get(url + "todos/", params={"userId": id}).json()

    """if the argv is more than 0, get the username in the table users"""
    us_name = users[0].get("username") if len(users) > 0 else None

    """Variables to export in json file"""
    task_l = [{"task": task.get('title'),
               "completed": task.get('completed'),
               "username": us_name} for task in tasks]

    with open("{}.json".format(id), "w", newline="") as jsonfile:
        json.dump({id: task_l}, jsonfile)
