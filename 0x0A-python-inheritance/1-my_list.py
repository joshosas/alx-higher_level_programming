#!/usr/bin/python3
"""My list
"""


class MyList(list):
    """A class MyList that inherits from a parent class 'list'"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
