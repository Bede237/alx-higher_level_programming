#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def __int__(self):
        """init func"""
        pass

    def area(self):
        """raise exception"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """checks if value is an int"""

        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
