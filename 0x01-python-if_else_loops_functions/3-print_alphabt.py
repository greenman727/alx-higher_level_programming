#!/usr/bin/python3
for ch in range(97 + 122):
    if ch == 'e' or ch == 'q':
        continue
    print("{:c}".format(ch), end = "")
