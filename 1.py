#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

cal = 0
maxcal = 0
cals = []

for line in open("inputs/1.txt", "r").readlines():
    if line.strip():
       cal += int(line.strip())
    else:
        cals.append(cal)
        maxcal = max(maxcal, cal)
        cal = 0
print("First result: ", maxcal)

cals = np.array(cals)
print("Second result: ", sum(cals[np.argsort(cals)[-3:]]))