#!/usr/bin/python3
""" exports fake to-do info for all fake employees from jsonplaceholder API """

from collections import OrderedDict
from json import dump
from requests import get

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    unames_by_id = {}
    for user in get(url + 'users').json():
        user_id = str(user.get('id'))
        unames_by_id[user_id] = user.get('username')

    tasks_by_id = {user_id: [] for user_id in unames_by_id}
    for task in get(url + 'todos').json():

        user_id = str(task.get("userId"))

        task_dict = {
            "username": unames_by_id.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        }

        tasks_by_id[user_id].append(task_dict)

    with open('todo_all_employees.json', 'w') as json_file:
        dump(tasks_by_id, json_file)
