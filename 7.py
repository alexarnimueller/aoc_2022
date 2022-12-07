#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict

sizes = defaultdict(int)
path = []

# build the directory structure in "path"
for line in open('inputs/7.txt', 'r').readlines():
    cmnds = line.strip().split()
    if cmnds[1] == 'cd':
        if cmnds[2] == '..':
            path.pop()  # go out again
        else:
            path.append(cmnds[2])
    elif re.match('[0-9]+', line):
        # add the file size to all dirs in the path
        for i in range(1, len(path)+1):
            sizes['/'.join(path[:i])] += int(cmnds[0])

# now check which one of them are in the ok size range
total1 = 0
total2 = 70000000
for k, v in sizes.items():
    if v <= 100000:  # smaller than allowed max size
        total1 += v
    if v >= sizes['/'] - 40000000:  # larger than space need to be freed
        total2 = min(v, total2)

print("First result: ", total1)
print("Second result: ", total2)