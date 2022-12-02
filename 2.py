#! /usr/bin/env python
# -*- coding: utf-8 -*-

oponent = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
me = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
wins = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
loos = {v: k for k, v in wins.items()}

# first part
total1 = 0
for line in open("inputs/2.txt", "r").readlines():
    o, m = line.strip().split(' ')
    o, m = oponent[o], me[m] 
    scr = scores[m]
    if o == m:
        scr += 3
    elif wins[m] == o:
        scr += 6
    total1 += scr

print("First result: ", total1)

# second part
target = {'X': 'loose', 'Y': 'draw', 'Z': 'win'}
total2 = 0
for line in open("inputs/2.txt", "r").readlines():
    o, m = line.strip().split(' ')
    o, t = oponent[o], target[m]
    if t == 'loose':
        m = wins[o]
        scr = 0
    elif t == 'win':
        m = loos[o]
        scr = 6
    else:
        m = o
        scr = 3
    scr += scores[m]
    total2 += scr

print("Second result: ", total2)
