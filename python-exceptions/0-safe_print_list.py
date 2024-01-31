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
    try:
        count = 0

        for item in my_list:
            print(item, end='')
            count += 1

            if count == x:
                break

    except TypeError:
        print("Error: Non-printable element encountered!")

    finally:
        print()
        return count
