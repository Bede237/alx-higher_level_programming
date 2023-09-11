#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for i, v in enumerate(row):
            if i == (len(row) - 1):
                print("{:d}".format(v))
                continue
            print("{:d}".format(v), end=" ")
