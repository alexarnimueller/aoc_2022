#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

forest = [[int(t) for t in line.strip()] for line in open('inputs/8.txt', 'r').readlines()]
forest = np.array(forest)

total1 = 2*forest.shape[0] + 2*forest.shape[1] - 4
for i in range(1, forest.shape[0]-1):
    for j in range(1, forest.shape[1]-1):
        h = forest[i, j]
        if (all([t<h for t in forest[:i, j]]) or
            all([t<h for t in forest[i+1:, j]]) or
            all([t<h for t in forest[i, :j]]) or
            all([t<h for t in forest[i, j+1:]])):
            total1 += 1
            continue
print("First result :", total1)

total2 = 1
for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        c = forest[i, j]
        l, r, u, d = 1, 1, 1, 1
        for t in forest[:i, j][::-1]:
            if t < c:
                d += 1
            else:
                break
        for t in forest[i, :j][::-1]:
            if t < c:
                l += 1
            else:
                break
        for t in forest[i+1:, j]:
            if t < c:
                u += 1
            else:
                break
        for t in forest[i, j+1:]:
            if t < c:
                r += 1
            else:
                break
        total2 = max(total2, l*r*u*d)
print("Second result: ", total2)
