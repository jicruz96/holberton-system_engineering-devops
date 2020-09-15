#!/usr/bin/python3
"""
uses jsonplaceholder API to return fake to-do information for a fake employee,
given a fake employee ID number as an argument.

USAGE:
    ./0-gather_data_from_an_API.py <employee-id>
"""

import requests
from sys import argv

if __name__ == "__main__":

    # Set main variables for script
    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1])

    # Get employee_name
    employee_name = requests.get(url).json().get('name')

    # Get employee task list
    tasks = requests.get(url + 'todos').json()

    # Get number of tasks (total_tasks)
    total_tasks = len(tasks)

    # Narrow down to completed tasks only
    tasks = [task for task in tasks if task.get('completed') is True]

    # Get number of completed tasks (done_tasks)
    done_tasks = len(tasks)

    # Print output
    first_line = "Employee {} is done with tasks({}/{}):"
    first_line = first_line.format(employee_name, done_tasks, total_tasks)
    print(first_line)
    for task in tasks:
        print("\t {}".format(task.get('title')))
