#!/usr/bin/python3
""" import a csv file"""

import csv
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

    """The variables to export in each row of the csv file"""
    rows = [[id, us_name, task.get('completed'), task.get('title')]
            for task in tasks]

    """Exports in csv file"""
    with open("{}.csv".format(id), "w", newline="") as csvfile:
        thewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        thewriter.writerows(rows)
