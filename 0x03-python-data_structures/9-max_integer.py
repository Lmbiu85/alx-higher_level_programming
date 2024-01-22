#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    v_max = my_list[0]
    for i in my_list:
        if not v_max or i > v_max:
            v_max = i
    return v_max
