#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from itertools import cycle
from string import ascii_lowercase

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
d = {l: i for i, l in enumerate(ascii_lowercase)}
d.update({'S': 0, 'E': 25})
m = np.array([[c for c in row.strip()] for row in open('inputs/12.txt', 'r').readlines()])
e = np.array([[d[c] for c in row] for row in m], dtype=int)

# first part
def main(part=1):
    visits = set()
    if part == 1:
        x, y = np.where(m == 'S')[0][0], np.where(m == 'S')[1][0]
        queue = [(x, y, 0)]
    else:
        queue = [(x, y, v) for (x,y), v in np.ndenumerate(e) if v == 0]
        x, y, steps = queue[0]
    while m[x, y] != 'E':
        x, y, steps = queue.pop(0)
        if (x, y) in visits:
            continue
        visits.add((x, y))
        for mov in dirs:
            nx, ny = np.array([x, y]) + mov
            if (0 <= nx < m.shape[0] and 
                0 <= ny < m.shape[1] and 
                e[nx, ny] <= e[x, y] + 1):
                queue.append((nx, ny, steps+1))
    print(f"Result part {part}: {steps}")

main(1)
main(2)