#!/usr/bin/python3
"""
This module contains a script that adds all arguments to a Python list
and then save them to a file

"""

import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list(args_list):
    filename = "add_item.json"

    # Check if the file exists
    if not os.path.isfile(filename):
        # If the file doesn't exist, create an empty list
        data_list = []
    else:
        # Load existing data from the file
        existing_data = load_from_json_file(filename)
        if existing_data is None:
            data_list = []
        else:
            data_list = existing_data

    # Add command-line arguments to the list
    data_list.extend(args_list)

    # Save the updated list to the file
    save_to_json_file(data_list, filename)


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    add_items_to_list(args)
