#!/usr/bin/python3
"""class list"""


class MyList(list):
    """prints a sorted list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
