#!/usr/bin/python
def new_in_list(my_list, idx, element):
    result = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    result[idx] = element
    return result
