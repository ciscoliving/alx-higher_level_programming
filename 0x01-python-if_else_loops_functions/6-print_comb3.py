#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a < b:
            if a < 8:
                print('{}{}'.format(a, b), end=', ')
            else:
                print('{}{}'.format(a, b))
