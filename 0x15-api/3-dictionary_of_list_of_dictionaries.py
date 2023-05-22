#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID
'''
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()

    datas = {}
    for user in users:
        tasks = requests.get('{}{}/todos'.format(url, user.get('id'))).json()
        list = []
        for task in tasks:
            data = {}
            data["username"] = user.get('username')
            data["task"] = task.get('title')
            data["completed"] = task.get('completed')
            list.append(data)
        datas[user.get('id')] = list
    with open('todo_all_employees.json', mode='w') as jsonfile:
        json.dump(datas, jsonfile)
