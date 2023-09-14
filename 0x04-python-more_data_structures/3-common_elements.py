#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not (set_1 or set_2):
        return None
    new = []
    for elm in set_1:
        if elm in set_2:
            new.append(elm)
    return set(new)
