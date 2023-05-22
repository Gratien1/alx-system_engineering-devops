#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID
'''
import csv
import requests
import sys


data = [
    ['John', 'Doe', 'john@example.com'],
    ['Jane', 'Doe', 'jane@example.com'],
    ['Bob', 'Smith', 'bob@example.com']
]
if __name__ == "__main__":
    userID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userID)
    tasks = requests.get('{}/todos'.format(url)).json()
    info = requests.get(url).json()
    filename = '{}.csv'.format(userID)
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([userID, info.get('username'),
                             task.get('completed'), task.get('title')])
