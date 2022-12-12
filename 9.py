#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.spatial.distance import euclidean

direcs = {'L': np.array([0, -1]),
         'R': np.array([0, 1]),
         'U': np.array([-1, 0]),
         'D': np.array([1, 0])}
visits1 = {}
head, tail = np.array([0, 0]), np.array([0, 0])
visits1['_'.join(tail.astype(str))] = 1

for line in open('inputs/9.txt', 'r').readlines():
    d, s = line.split()
    moves = direcs[d] * int(s)
    for head in np.linspace(head, head + moves, np.max(np.abs(moves))+1)[1:].astype(int):
        if euclidean(head, tail) > 1.4143:
            dists = np.where(head-tail > 0, 1, np.where(head-tail < 0, -1 , 0))
            tail += dists
            visits1['_'.join(tail.astype(str))] = 1
print("First result: ", sum(visits1.values()))

visits2 = {}
rope = np.zeros((10, 2), dtype=int)
for line in open('inputs/9.txt', 'r').readlines():
    d, s = line.split()
    moves = direcs[d] * int(s)
    for h in np.linspace(rope[0], rope[0] + moves, np.max(np.abs(moves))+1)[1:].astype(int):
        rope[0] = h
        for i in range(1, len(rope)):
            if euclidean(rope[i], rope[i-1]) > 1.4143:
                dists = np.where(rope[i-1]-rope[i] > 0, 1, np.where(rope[i-1]-rope[i] < 0, -1 , 0))
                rope[i] += dists
                visits2['_'.join(rope[-1].astype(str))] = 1
print("Second result: ", sum(visits2.values()))