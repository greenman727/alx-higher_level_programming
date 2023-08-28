#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in list(range(my_list)):
            print x
    except IndexError:
        pass
    return my_list[:]
