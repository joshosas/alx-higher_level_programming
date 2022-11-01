#!/usr/bin/python3
"""Base class"""

import json
import os
import csv
import turtle


class Base:
    """Represents the base class

    Observation:
        The class is used to manage id attribute
        in all my future classes and to avoid duplicating
        the same code (by extension, same bugs)

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates the id class with

        Args:
            id(int): the class id

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
