#! /usr/bin/env python
# -*- coding: utf-8 -*-

# first part
total1 = 0
total2 = 0
for line in open("inputs/4.txt", "r").readlines():
    o, t = line.strip().split(',')
    os, oe = o.split('-')
    ts, te = t.split('-')
    ro = set(range(int(os), int(oe)+1))
    rt = set(range(int(ts), int(te)+1))
    isct = ro.intersection(rt)
    if isct:
        total2 += 1
    if isct == ro or isct == rt:
        total1 += 1

print("First result: ", total1)
print("Second result: ", total2)
