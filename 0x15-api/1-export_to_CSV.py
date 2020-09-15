#!/usr/bin/python3
"""
exports fake to-do information for a fake employee from jsonplaceholder API,
given a fake employee ID number as an argument, to USER_ID.csv

USAGE:
    ./1-export_to_CSV.py <user-id>

RESULT:
    CSV file named <user-id>.csv with user tasks
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    # Set main variables for script
    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(employee_id)

    # Get employee_name
    employee_name = requests.get(url).json().get('name')

    # Get employee task list
    tasks = requests.get(url + 'todos').json()

    # Write CSV
    with open('{}.csv'.format(employee_id), 'w', newline='') as csv_file:

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in tasks:

            # Make row
            is_complete = str(task.get('completed'))
            title = task.get('title')
            row = [employee_id, employee_name, is_complete, title]

            # Write row to file
            writer.writerow(row)
