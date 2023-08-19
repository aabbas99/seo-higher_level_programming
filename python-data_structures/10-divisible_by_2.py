#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = my_list[:]
    for i in enumerate(my_list):
        if i % 2 != 0:
            result[i] = False
        else:
            result[i] = True
    return result
