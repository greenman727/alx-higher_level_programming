#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score = 0
    weight = 0

    for tupl in mylist:
        score += tupl[0] * tupl[1]
        weight += tupl[1]

    return (score/weight)

