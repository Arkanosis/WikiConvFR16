#! /usr/bin/env python3
import math, sys
f = math.factorial
for line in sys.stdin:
    count = int(line.rstrip())
    print(int(f(count) / f(2) / f(count-2)))
