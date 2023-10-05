#!/usr/bin/python3
def print_square(size):
    """This function prints a square with dim size"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        print("#" * size)
