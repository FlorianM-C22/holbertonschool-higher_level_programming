#!/usr/bin/python3
"""
This module contains a function that writes an Object to a text file,
using a JSON representation:

"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation:
    """
    json_obj = json.dumps(my_obj)

    with open(filename, 'w') as outfile:
        outfile.write(json_obj)
