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

total2 = 0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        score = 1
        for di, dj in directions:
            d = 1
            ii, jj = i+di, j+dj
            while True:
                if not (0 <= ii < forest.shape[0] and 0 <= jj < forest.shape[1]):
                    d -= 1
                    break
                if forest[ii, jj] >= forest[i, j]:
                    break
                d += 1
                ii, jj = ii+di, jj+dj
            score *= d
        total2 = max(total2, score)
print("Second result: ", total2)

