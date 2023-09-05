#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
plum = number % 10
if (number < 0):
    plum = (number * -1) % 10
    plum = plum * -1
print(f"Last digit of {number} is {plum}", end=" ")
if ((plum < 6) and (plum != 0)):
    print("and is less than 6 and not 0")
elif (plum > 5):
    print("and is greater than 5")
else:
    print("and is 0")
