#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx, my_list[idx] in enumerate(my_list):
            if my_list[idx] == search:
                my_list[idx] = replace
