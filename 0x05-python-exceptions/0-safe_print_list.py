#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        my_list = []
        for x in my_list:
            if type(x) == int or type(x) == str:
                my_list.append(x)
            print(my_list)
    except IndexError:
        pass
    return my_list
