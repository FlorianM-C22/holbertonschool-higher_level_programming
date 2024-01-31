#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list

    Parameters:
    - my_list: A list of any type
    - x: The number of elements to be printed

    Returns:
    The real number of elements printed

    """

    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            break
        count += 1
    print()

    return count
