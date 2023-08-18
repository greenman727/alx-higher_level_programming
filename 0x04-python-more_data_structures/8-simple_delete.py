#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for key in a_dictionary.keys():
        if key != 0:
            a_dictionary.update(del a_dictionary[key])
