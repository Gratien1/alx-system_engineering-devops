#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID
'''
import json
import requests
import sys


if __name__ == "__main__":
    userID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userID)
    tasks = requests.get('{}/todos'.format(url)).json()
    info = requests.get(url).json()
    list = []
    for task in tasks:
        data = {}
        data["task"] = task.get('title')
        data["completed"] = task.get('completed')
        data["username"] = info.get('username')
        list.append(data)
    datas = {}
    datas[userID] = list
    filename = '{}.json'.format(userID)
    with open(filename, mode='w') as jsonfile:
        json.dump(datas, jsonfile)
