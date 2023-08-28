#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format())
    except ValueError:
        pass
    if value == 1:
        return True
    else:
        return False
