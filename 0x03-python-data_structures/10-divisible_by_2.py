#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list[:]:
        if int(i) % 2 == 0:
            return True
        else:
            return False
