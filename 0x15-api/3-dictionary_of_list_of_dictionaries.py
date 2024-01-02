#!/usr/bin/python3
"""Gather Data from an API"""

if __name__ == '__main__':
    import json
    import requests

    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo = requests.get(todo_url).json()
    users_url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(users_url).json()

    filename = 'todo_all_employees.json'

    def to_dict(entry, user):
        """Convert entry to a dictionary in the required format"""
        new_dict = {}
        new_dict['username'] = user['username']
        new_dict['task'] = entry['title']
        new_dict['completed'] = entry['completed']
        return new_dict

    to_file = {}
    for user in users:
        user_list = []
        for entry in todo:
            if entry['userId'] == user['id']:
                user_dict = to_dict(entry, user)
                user_list.append(user_dict)
        to_file[user['id']] = user_list

    with open(filename, 'w', encoding='utf-8') as w:
        json.dump(to_file, w)
