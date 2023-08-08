#!/usr/bin/python3 
import random 
number = random.randint(-10000, 10000)
numstr = repr(number)
lastdigit_str = numstr[-1]
lastdigit = int(lastdigit_str)
print(f"Last digit of {number} is {lastdigit}")
if lastdigit > 5:
    print(f"{lastdigit} is greater than 5")
if lastdigit == 0:
    print(f"{lastdigit} is 0")
if lastdigit < 6 and lastdigit != 0:
    print(f"{lastdigit} is less than 6 and not 0")
