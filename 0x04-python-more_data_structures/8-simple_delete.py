#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary.keys():
       remove_key = i.pop(key, None):
           if remove_key != None:
               del remove_key