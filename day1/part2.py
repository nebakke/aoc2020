#!/usr/bin/env python

with open("day1.dat") as datafile:
    numbers = map(int, datafile.read().splitlines())

#result = list(set([ n1 * (2020 - n1) for n1 in numbers if (2020 - n1) in numbers ]))

#result = [n1 * n2 * n3 for n1 in numbers for n2 in numbers for n3 in numbers if n1 not in [n2, n3] and n2 not in [n1, n3] and n3 not in [n1,n2] and n1 + n2 + n3 == 2020]
#result = [n1 * n2 * n3 for n1 in numbers for n2 in numbers for n3 in numbers if [n1,n2,n3].count(n1) == 1 and [n1,n2,n3].count(n2) == 1 and [n1,n2,n3].count(n3) == 1 and n1 + n2 + n3 == 2020]
result = list(set([n1 * n2 * n3 for n1 in numbers for n2 in numbers for n3 in numbers if n1 + n2 + n3 == 2020]))

print(result)
