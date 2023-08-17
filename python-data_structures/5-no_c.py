#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    string_list.remove("c")
    string_list.remove("C")
    new_string = "".join(string_list)
    return new_string
