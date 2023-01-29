#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10 if number > 10 else number % -10
print("Last digit of {:d} is {:d} and is ".format(number, digit), end="")
if digit > 5:
print("greater than 5")
if digit == 0:
print("is 0")
else:
print("less than 6 and not 0")
