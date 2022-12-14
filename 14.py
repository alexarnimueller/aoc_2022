#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

YMAX, XMAX = 175, 1000

def build_cave(filename):
    cave = np.zeros((YMAX, XMAX), dtype=int)
    for line in open(f'inputs/{filename}', 'r').readlines():
        coords = [[int(v) for v in pair.split(',')] for pair in line.split(' -> ')]
        i = 0
        while i < len(coords) - 1:
            y1, y2 = sorted([coords[i][1], coords[i+1][1]])
            x1, x2 = sorted([coords[i][0], coords[i+1][0]])
            cave[y1:y2+1, x1:x2+1] = 1
            i += 1
    return cave


def add_floor(cave):
    lowest_stone = np.max(np.where(cave == 1)[0])
    cave[lowest_stone+2, :] = 1
    return cave


def first_part(cave):
    grains = 0
    start = 500
    y, x = 0, start
    while y < YMAX-1:
        if cave[y+1, x]:
            if cave[y+1, x-1]:
                if cave[y+1, x+1]:
                    grains += 1
                    cave[y, x] = -1
                    y, x = 0, start
                else:
                    x += 1
            else:
                x -= 1
        y += 1      
    return grains, cave


def second_part(cave):
    grains = 0
    start = 500
    y, x = -1, start
    while not cave[0, start]:
        if cave[y+1, x]:
            if cave[y+1, x-1]:
                if cave[y+1, x+1]:
                    grains += 1
                    cave[y, x] = -1
                    y, x = -1, start
                else:
                    x += 1
            else:
                x -= 1
        y += 1      
    return grains, cave

if __name__ == '__main__':
    cave = build_cave('14.txt')
    rslt1, cave = first_part(cave)
    print("First result: ", rslt1)
    cave = build_cave('14.txt')
    cave = add_floor(cave)
    rslt2, cave = second_part(cave)
    print("Second result: ", rslt2)
    plt.imshow(cave)
    plt.show()

