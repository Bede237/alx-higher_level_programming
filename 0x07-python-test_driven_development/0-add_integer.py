#!/usr/bin/python3
def add_integer(a, b=98):
    """this function returns the sum of 2 numbers"""

    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
    return int(a) + int(b)
