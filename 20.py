#! /usr/bin/env python
# -*- coding: utf-8 -*-

def read_input(filename):
    return [int(n.strip()) for n in open('inputs/'+filename, 'r').readlines()]


def mix(numbers, key=1, times=1):
    # add original index to keep track
    mixer = [(i, n*key) for i, n in enumerate(numbers)]
    for _ in range(times):
        for dest in range(len(mixer)):
            for i, (k, n) in enumerate(mixer):
                if k == dest:
                    old = i
                    break
            new = (old + n) % (len(numbers) - 1)  # circular
            mixer.pop(old)
            mixer.insert(new, (k, n))

    # find index of 0 and return sum of steps
    out = [n for _, n in mixer]
    i = out.index(0)
    return sum(out[(i + step) % len(numbers)] for step in [1000, 2000, 3000])
    

if __name__ == "__main__":
    inputs = read_input(filename='20.txt')
    rslt1 = mix(inputs)
    print("First result: ", rslt1)
    rslt2 = mix(inputs, key=811589153, times=10)
    print("Second result: ", rslt2)
