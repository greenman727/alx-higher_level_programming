#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in my_list:
        if idx < 0:
            return None
        elif idx > (len(my_list) - 1):
            return None
        else:
            return (del my_list[idx])
