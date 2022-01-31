#!/usr/bin/python3
"""
Python script that, using a REST API in url,
for a given employee ID, returns information about his/her TODO list progress
"""

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

    """if the argv is more than 0, get the name in the table users"""
    us_name = users[0].get("name") if len(users) > 0 else None

    """Shows the description of the task when the status is completed"""
    desc_task = [task.get('title') for task in tasks
                 if task.get('completed') is True]

    """counts all task and the completes"""
    task_all = len(tasks)
    task_comp = len(desc_task)

    """Prints info of user"""
    print("Employee {} is done with tasks({}/{}):".format(us_name,
                                                          tasks_comp,
                                                          tasks_all))

    """Prints info of todos"""
    [print("\t {}".format(task)) for task in desc_task]
