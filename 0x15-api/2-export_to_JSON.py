#!/usr/bin/python3
"""Gather Data from an API"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    todo_url = 'https://jsonplaceholder.typicode.com/todos/?userId=' + argv[1]
    todo = requests.get(todo_url).json()
    user_url = 'https://jsonplaceholder.typicode.com/users/?id=' + argv[1]
    user = requests.get(user_url).json()

    user = user[0]
    filename = argv[1] + '.json'

    list_of_tasks = []
    for task in todo:
        new_dict = {}
        new_dict['task'] = task['title']
        new_dict['completed'] = task['completed']
        new_dict['username'] = user['username']
        list_of_tasks.append(new_dict)

    to_file = {argv[1]: list_of_tasks}

    with open(filename, 'w', encoding='utf-8') as w:
        json.dump(to_file, w)
