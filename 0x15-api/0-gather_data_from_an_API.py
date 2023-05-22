#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID
'''
import requests
import sys

if __name__ == "__main__":
    userID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userID)
    todo_r = requests.get('{}/todos'.format(url))
    info_r = requests.get(url)
    done = []
    for todo in todo_r.json():
        if todo.get('completed') is True:
            done.append(todo)
    print('Employee {} is done with tasks({}/{}):'
          .format(info_r.json().get('name'), len(done), len(todo_r.json())))
    for task in done:
        print('\t {}'.format(task.get('title')))
