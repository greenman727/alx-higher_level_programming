#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if "key" not in a_dictionary.keys():
        a_dictionary["key"] = value
    if value not in a_dictionary.values():
        a_dictionary["key"] = value
