#! /usr/bin/env python
# -*- coding: utf-8 -*-

s = open("inputs/6.txt", "r").read().strip()

# part one
for i in range(4, len(s)):
    if len(set(s[i-4:i])) == 4:
        print("First result: ", i)
        break

# part two
for i in range(14, len(s)):
    if len(set(s[i-14:i])) == 14:
        print("Second result: ", i)
        break

