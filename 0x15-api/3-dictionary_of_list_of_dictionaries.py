#!/usr/bin/python3
""" exports fake to-do info for all fake employees from jsonplaceholder API """

from collections import OrderedDict
from json import dump
from requests import get

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    usernames = {}
    for user in get(url + 'users').json():
        user_id = str(user.get('id'))
        usernames[user_id] = user.get('username')

    tasks_by_id = OrderedDict()
    for task in get(url + 'todos').json():

        user_id = str(task.get("userId"))

        task_dict = OrderedDict(
            username=usernames.get(user_id),
            task=task.get("title"),
            completed=task.get("completed")
        )

        if tasks_by_id.get(user_id) is None:
            tasks_by_id[user_id] = [task_dict]
        else:
            tasks_by_id[user_id].append(task_dict)

    with open('todo_all_employees.json', 'w') as json_file:
        dump(tasks_by_id, json_file)
