#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return (list(set(set_1).difference(set_2)) and list(set(set_2).differnce(set_1)))
