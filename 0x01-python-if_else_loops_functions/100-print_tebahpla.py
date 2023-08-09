#!/usr/bin/python3
for cha in range(26):
    if cha % 2 == 0:
        print("{:c}".format(122 - cha), end="")
    else:
        print("{:c}".format(90 - cha), end="")
