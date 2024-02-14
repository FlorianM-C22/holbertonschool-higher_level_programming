#!/usr/bin/python3
"""
This module contains a function for reading a text file
and printing its contents to stdout.

"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
