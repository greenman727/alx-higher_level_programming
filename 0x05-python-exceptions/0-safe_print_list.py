#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in my_list:
            count = count+1
    except ValueError:
        pass
    print(count)
    return count
