#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    new = my_list.copy()
    if not (search or replace):
        return my_list
    for i in range(len(new)):
        if (new[i] == search):
            new[i] = replace
    return new
