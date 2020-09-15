#!/usr/bin/python3
"""
exports fake to-do information for all fake employees from jsonplaceholder API,

USAGE:
    ./3-dictionary_of_list_of_dictionaries.py

RESULT:
    JSON file named todo_all_employes.json with all employee tasks
"""
from collections import OrderedDict
import json
import requests

if __name__ == "__main__":

    # Set main variables for script
    url = 'https://jsonplaceholder.typicode.com/{}/'

    # Get user list
    users = requests.get(url.format('users')).json()
    users = {str(user.get('id')): user.get('username') for user in users}

    # Get task list
    tasks = requests.get(url.format('todos')).json()

    tasks_by_id = OrderedDict()
    for task in tasks:

        # Create a new task dictionary for each task
        # First, get the user_id and username
        task_dict = OrderedDict()
        user_id = str(task.get("userId"))
        username = users.get(user_id)

        # Then, add the three task dictionary key/values
        task_dict.update({"username": username})
        task_dict.update({"task": task.get("title")})
        task_dict.update({"completed": task.get("completed")})

        # Add this new task dictionary to the list of tasks
        if tasks_by_id.get(user_id) is None:
            tasks_by_id[user_id] = [task_dict]
        else:
            tasks_by_id[user_id].append(task_dict)

    # Write JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(tasks_by_id, json_file)
