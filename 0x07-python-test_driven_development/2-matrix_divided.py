#!/usr/bin/python3
def matrix_divided(matrix, div):
    """This function divides all elements in matrix by div"""

    n = len(matrix[0])
    new = []
    for row in matrix:
        if isinstance(row, list):
            for elem in row:
                if not isinstance(elem, int):
                    if not isinstance(elem, float):
                        raise TypeError('matrix must be a matrix\
(list of lists) of integers/floats')
        elif not isinstance(row, list):
            raise TypeError('matrix must be a matrix\
(list of lists) of integers/floats')

    for row in matrix:
        if len(row) != n:
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, int):
        if not isinstance(div, float):
            raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        new.append(list(map(lambda x: round(x / div, 2), row)))
    return new
