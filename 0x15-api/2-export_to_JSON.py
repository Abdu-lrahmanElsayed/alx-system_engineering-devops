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

    with open('{}.csv'.format(empid), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(
                empid, empname, task.get('completed'), task.get('title')))
