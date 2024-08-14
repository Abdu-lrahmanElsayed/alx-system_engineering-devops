#!/usr/bin/python3
"""
or a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":

    empid = sys.argv[1]
    baseurl = "https://jsonplaceholder.typicode.com/users"
    url = baseurl + "/" + empid

    r = requests.get(url)
    empname = r.json().get('name')
    todourl = url + "/todos"
    r = requests.get(todourl)
    tasks = r.json()
    done = 0
    tasks_done = []
    for task in tasks:
        if task.get('completed'):
            tasks_done.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(
        empname, done, len(tasks)))

    for task in tasks_done:
        print("\t {}".format(task.get('title')))
