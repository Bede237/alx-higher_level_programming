#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """returns true if obj is an instance of class"""
    if issubclass(type(0bj), a_class):
        return not (type(obj) is a_class)
    return False
