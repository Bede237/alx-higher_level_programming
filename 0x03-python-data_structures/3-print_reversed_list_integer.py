#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    spam = len(my_list) - 1
    for i in range(len(my_list)):
        print("{}".format(my_list[spam - i]))
