#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
else:
    if number == 0:
        print("{} is zero".format(number))
    else:
        if number < 0:
            print("{} is negative".format(number))
