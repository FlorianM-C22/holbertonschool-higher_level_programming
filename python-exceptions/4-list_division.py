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
            elem_list1 = my_list_1[i]
            elem_list2 = my_list_2[i]
            result = elem_list1 / elem_list2
            new_list.append(result)
        except TypeError:
            print("wrong type")
            result = 0
            new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            new_list.append(result)
        except IndexError:
            print("out of range")
        finally:
            pass

    return new_list
