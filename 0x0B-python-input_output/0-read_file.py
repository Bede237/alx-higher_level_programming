#!/usr/bin/python
def read_file(filename=""):
    """reads data from file """
    with open(filename, 'r',  encoding="utf-8") as f:
        data = f.read()
        print(data[:-1])
