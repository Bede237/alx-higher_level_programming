#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """writes astring to a file"""
    with open(filename, 'w', encoding='UTF-8') as f:
        num = f.write(text)
    return num
