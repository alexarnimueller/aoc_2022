#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = 1
cycles = []
screen = np.zeros(6*40, dtype=int)
cyc = 0
for line in open('inputs/10.txt', 'r').readlines():
    cycles.append(x)
    if cyc % 40 in [x-1, x, x+1]:
        screen[cyc] = 1
    if ' ' in line:
        cycles.append(x)
        cyc += 1
        if cyc % 40 in [x-1, x, x+1]:
            screen[cyc] = 1
        x += int(line.strip().split()[-1])
    cyc += 1
    
total = 0
for i, v in enumerate(cycles):
    if i+1 in [20, 60, 100, 140, 180, 220]:
        total += int((i+1) * v)   
print("First result: ", total)

plt.imshow(screen.reshape((6, 40)))
plt.show()
