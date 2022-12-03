#! /usr/bin/env python
# -*- coding: utf-8 -*-

from string import ascii_letters


prio = {l: v+1 for v, l in enumerate(ascii_letters)}

scr1 = 0
for line in open("inputs/3.txt", "r").readlines():
    line = line.strip()
    one = line[:int(len(line)/2)]
    two = line[int(len(line)/2):]
    for c in set(one).intersection(set(two)):
       scr1 += prio[c]

print("First result: ", scr1)


f = [line.strip() for line in open("inputs/3.txt", "r").readlines()]
scr2 = 0
for i in range(0, len(f), 3):
    c = list(set(f[i]).intersection(set(f[i+1])).intersection(set(f[i+2])))[0]
    scr2 += prio[c]

print("Second result: ", scr2)
