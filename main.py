#!/usr/bin/env python

import string
import sys

sum = 0

with open(sys.argv[1], "r") as file:

    for line in file:
    
        digits = list(filter(lambda ch: ch in string.digits, line))
        
        if len(digits) == 0:
            continue

        number = int(digits[0] + digits[-1])
        sum += number

print(sum)