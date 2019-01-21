#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 6]
data2 = gen_random(1, 3, 10)

print(5 in [1, 2, 3])

# Реализация задания 2
S = Unique(data1, False)
d = True
while d:
    try:
        print(next(S))
    except StopIteration:
        d = False

S = Unique(data2, False)
d = True
while d:
    try:
        print(next(S))
    except StopIteration:
        d = False

try:
    while True:
        print(next(S))

except StopIteration:
    pass
