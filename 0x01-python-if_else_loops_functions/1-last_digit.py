#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
    print("Last digit of {} is {} and is ".format(number, digit), end="")
else:
    if digit > 5:
        print("greater than 5")
    else:
        if digit == 0:
            print("0")
        else:
            if digit < 6 and != 0
            print("less than 6 and not 0")
