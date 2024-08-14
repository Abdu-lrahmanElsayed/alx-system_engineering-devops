#!/usr/bin/python3
"""
or a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":

    empid = sys.argv[1]
    baseurl = "https://jsonplaceholder.typicode.com/users"
    url = baseurl + "/" + empid

    r = requests.get(url)
    empuname = r.json().get('username')
    todourl = url + "/todos"
    r = requests.get(todourl)
    tasks = r.json()
    d = {empid: []}
    for task in tasks:
        d[empid].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": empuname
            })

    with open('{}.json'.format(empid), 'w') as f:
        json.dump(d, f)
