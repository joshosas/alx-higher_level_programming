#!/usr/bin/python3
"""Can I ? - Yep!"""


def add_attribute(obj, attr, val):
    """A function that adds a new attribute to
    an object if it’s possible

    Args:
        obj(obj): input object
        attr(attr): name of the attribute
        value(val): value of the attribute

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
