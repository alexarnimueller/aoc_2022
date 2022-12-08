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

total2 = {}
for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        h = forest[i, j]
        v1, v2, v3, v4 = 0, 0, 0, 0
        for t in forest[:i, j][::-1]:
            v1 += 1
            if t >= h:
                break
        for t in forest[i+1:, j]:
            v2 += 1
            if t >= h:
                break
        for t in forest[i, :j][::-1]:
            v3 += 1
            if t >= h:
                break
        for t in forest[i, j+1:]:
            v4 += 1
            if t >= h:
                break
        total2[f'{i}-{j}'] = v1 * v2 * v3 * v4
print("Second result: ", max(total2.values()))

