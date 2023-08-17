#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    for item in string_list:
        if string_list[i] == 'c' or 'C':
            string_list.remove(string_list[i])
    new_string = "".join(string_list)
    return new_string
