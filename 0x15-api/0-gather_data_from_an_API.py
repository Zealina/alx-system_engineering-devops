#!/usr/bin/python3
"""Gather Data from an API"""

if __name__ == '__main__':
    import json
    from sys import argv
    import urllib.request

    todo_url = 'https://jsonplaceholder.typicode.com/todos/?userId=' + argv[1]
    todo_response = urllib.request.urlopen(todo_url)
    user_url = 'https://jsonplaceholder.typicode.com/users/?id=' + argv[1]
    user_response = urllib.request.urlopen(user_url)

    todo = todo_response.read()
    user = user_response.read()

    todo = json.loads(todo)
    user = json.loads(user)
    done = 0
    total = 0

    for entry in todo:
        if entry['completed'] is True:
            done += 1
        total += 1

    print(f"Employee {user[0]['name']} is done with ({done}/{total}):")
    for entry in todo:
        if entry['completed'] is True:
            print(f"\t {entry['title']}")
