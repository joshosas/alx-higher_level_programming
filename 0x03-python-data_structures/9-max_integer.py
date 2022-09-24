#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for elm in my_list:
            if elm > max_int:
                max_int = elm
        return max_int
    return None
