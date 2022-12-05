#! /usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

# first part
stack = defaultdict(list)

for line in open("inputs/5.txt", "r").readlines():
    if '[' in line:
        for i, j in enumerate(range(1, len(line), 4)):
            if line[j].strip():
                stack[i+1].append(line[j].strip())
    elif 'move' in line:
        l = line.strip().split(' ')
        n, f, t = int(l[1]), int(l[3]), int(l[5])
        for _ in range(n):
            stack[t] = [stack[f].pop(0)] + stack[t]

print("First result: " + "".join([stack[k+1][0] for k in range(len(stack))]))

# second part
stack = defaultdict(list)

for line in open("inputs/5.txt", "r").readlines():
    if '[' in line:
        for i, j in enumerate(range(1, len(line), 4)):
            if line[j].strip():
                stack[i+1].append(line[j].strip())
    elif 'move' in line:
        l = line.strip().split(' ')
        n, f, t = int(l[1]), int(l[3]), int(l[5])
        stack[t] = stack[f][:n] + stack[t]
        stack[f] = stack[f][n:]

print("Second result: " + "".join([stack[k+1][0] for k in range(len(stack))]))