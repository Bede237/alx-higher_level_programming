#!/usr/bin/python3
"""append to file"""


def append_write(filename="", text=""):
    """appends a string to a file"""

    with open(filename, 'a', encoding='UTF-8') as f:
        num = f.write(text)
    return num
