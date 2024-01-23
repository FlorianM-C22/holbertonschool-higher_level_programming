#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1

    if len(argv) == 0:
        print("{} arguments.".format(count))
    if count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count, argv[count]))
    else:
        print("{} arguments:".format(count))
        i = 1
        while i < len(argv):
            print("{}: {}".format(i, argv[i]))
            i += 1
