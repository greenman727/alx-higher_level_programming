#!/usr/bin/python3
def raise_exception():
    try:
        print("word")
    except TypeError:
        print("TypeError")
        raise
