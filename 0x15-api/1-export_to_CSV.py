#!/usr/bin/python3
"""Gather Data from an API"""

if __name__ == '__main__':
    import requests
    from sys import argv

    todo_url = 'https://jsonplaceholder.typicode.com/todos/?userId=' + argv[1]
    todo = requests.get(todo_url).json()
    user_url = 'https://jsonplaceholder.typicode.com/users/?id=' + argv[1]
    user = requests.get(user_url).json()

    user = user[0]
    filename = str(argv[1]) + '.csv'
    with open(filename, 'w', encoding='utf-8') as w:
        for entry in todo:
            row = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(entry['userId'],
                                                         user['username'],
                                                         entry['completed'],
                                                         entry['title'])
            w.write(row)
