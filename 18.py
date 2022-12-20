#! /usr/bin/env python
# -*- coding: utf-8 -*-


def read_input(filename):
    return set(tuple(int(n) for n in line.strip().split(',')) for line in open('inputs/'+filename, 'r').readlines())


def part_one(readings):
    # get free faces per block and sum up
    areas = {r: 6 for r in readings}
    for curr in readings:
        for block in readings:
            if (curr != block and  # don't compare to itself
                sum([int(bool(c != curr[i])) for i, c in enumerate(block)]) == 1 and  # one differing coordinate
                sum([abs(c - curr[i]) for i, c in enumerate(block)]) == 1):  # max dist 1 for differing coordinate
                areas[curr] -= 1  # remove one free face
    return sum(areas.values())


def get_min_max(readings):
    # get bounds for part 2
    x_min = min(r[0] for r in readings) - 1
    x_max = max(r[0] for r in readings) + 1
    y_min = min(r[1] for r in readings) - 1
    y_max = max(r[1] for r in readings) + 1
    z_min = min(r[2] for r in readings) - 1
    z_max = max(r[2] for r in readings) + 1
    return x_min, x_max, y_min, y_max, z_min, z_max


def get_adjacent(x, y, z):
    # neighbors
    return {(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)}


def part_two(readings):
    x_min, x_max, y_min, y_max, z_min, z_max = get_min_max(readings)
    queue = [(x_min, y_min, z_min)]
    seen = set()
    total = 0
    while queue:  # classic queue job
        curr = queue.pop(0)
        if not curr in seen:
            seen.add(curr)
            for x_nxt, y_nxt, z_nxt in get_adjacent(*curr):
                if (not (x_nxt, y_nxt, z_nxt) in seen and
                    x_min <= x_nxt <= x_max and
                    y_min <= y_nxt <= y_max and 
                    z_min <= z_nxt <= z_max):
                    if (x_nxt, y_nxt, z_nxt) in readings:
                        total += 1
                    else:
                        queue.append((x_nxt, y_nxt, z_nxt))
    return total


if __name__ == "__main__":
    inputs = read_input(filename='18.txt')
    rslt1 = part_one(inputs)
    print("First result: ", rslt1)
    rslt2 = part_two(inputs)
    print("Second result: ", rslt2)
