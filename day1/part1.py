#!/usr/bin/env python

numbers=[1721,979,366,299,675,1456]

with open("day1.dat") as datafile:
    numbers = map(int, datafile.read().splitlines())

result = list(set([ n1 * (2020 - n1) for n1 in numbers if (2020 - n1) in numbers ]))
print(result)
