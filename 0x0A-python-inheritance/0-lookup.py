#!/usr/bin/python3
"""Lookup method"""


def lookup(obj):
    """returns List of attributes in obj"""

    return (items for attributes in dir(obj)
