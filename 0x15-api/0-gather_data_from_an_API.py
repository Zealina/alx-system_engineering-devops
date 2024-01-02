#!/usr/bin/python3
"""Gather Data from an API"""

if __name__ == '__main__':
    from sys import argv
    import requests

    todo_url = 'https://jsonplaceholder.typicode.com/todos/?userId=' + argv[1]
    todo = requests.get(todo_url).json()
    user_url = 'https://jsonplaceholder.typicode.com/users/?id=' + argv[1]
    user = requests.get(user_url).json()

    done = 0
    total = 0

    for entry in todo:
        if entry['completed'] is True:
            done += 1
        total += 1

    print("Employee {} is done with tasks({}/{}):".format(user[0]['name'],
                                                          done, total))
    for entry in todo:
        if entry['completed'] is True:
            print(f"\t {entry['title']}")
