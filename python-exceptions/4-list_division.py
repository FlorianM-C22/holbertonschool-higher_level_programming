#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.

    Parameters:
    - my_list_1: can contain any type (integer, string, etc.)
    - my_list_2: can contain any type (integer, string, etc.)
    - list_length: length of the list which should be returned

    Returns:
    - A new list (length = list_length) with all divisions

    """

    new_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)

    return new_list
