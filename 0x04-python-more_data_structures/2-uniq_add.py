#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    new = []
    count = 0
    for i in my_list:
        if i not in new:
            count += i
            new.append(i)
    return count
