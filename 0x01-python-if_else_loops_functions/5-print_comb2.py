#!/usr/bin/python
for i in range(100):
    if i is not 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
