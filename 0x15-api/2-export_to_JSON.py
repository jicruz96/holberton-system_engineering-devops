#!/usr/bin/python3
"""
exports fake to-do information for a fake employee from jsonplaceholder API,
given a fake employee ID number as an argument, to USER_ID.json

USAGE:
    ./1-export_to_CSV.py <user-id>

RESULT:
    JSON file named <user-id>.json with user tasks
"""
from collections import OrderedDict
import json
import requests
from sys import argv

if __name__ == "__main__":

    # Set main variables for script
    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(employee_id)

    # Get employee username
    username = requests.get(url).json().get('username')

    # Get key
    key = str(employee_id)

    # Get values (list of tasks)
    values = []
    tasks = requests.get(url + 'todos').json()
    for task in tasks:

        # Each task is a dict with task title, completion status, and username
        task_dict = OrderedDict()
        task_dict.update({"task": task.get("title")})
        task_dict.update({"completed": task.get("completed")})
        task_dict.update({"username": username})
        values.append(task_dict)

    # Write JSON file
    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump({key: values}, json_file)
