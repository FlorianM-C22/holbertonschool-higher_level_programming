#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Parameters:
    - my_list: can contain any type (integer, string, etc.)
    - x: represents the number of elements to access in my_list

    Returns:
        - The real number of integers printed

    """

    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except IndexError:
            raise
        except Exception as e:
            pass
    print()

    return count
