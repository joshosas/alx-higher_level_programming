#!/usr/bin/python3
"""Is same object.

"""


def is_same_class(obj, a_class):
    """A function that returns True if the object is
    exactly an instance of the class else
    returns False

    Args:
        obj - object of the class
        a_class - the class

    """
    if isinstance(type(obj), a_class):
        return True
    return False
