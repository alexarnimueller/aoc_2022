#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import cmp_to_key


def check(left: list, right: list):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        return 0
    elif isinstance(left, list) and isinstance(right, list):
        idx = 0
        while idx < len(left) and idx < len(right):  # dig into list of lists
            rslt = check(left[idx], right[idx])
            if rslt in [-1, 1]:
                return rslt
            idx += 1
                                
        if len(left) == idx and len(right) > idx:
            return 1
        elif len(left) > idx and len(right) == idx:
            return -1
        return 0
        
    elif isinstance(left, int) and isinstance(right, list):
        return check([left], right)
    else:
        return check(left, [right])

if __name__ == '__main__':
    ok, packets = [], []
    pairs = open('inputs/13.txt', 'r').read().split('\n\n')
    for i, p in enumerate(pairs, start=1):
        lft = json.loads(p.split('\n')[0])
        rgt = json.loads(p.split('\n')[1])
        packets.extend([lft, rgt])
        if check(lft, rgt) == 1:     
            ok.append(i)

    print("First result: ", sum(ok))

    # add divider packets
    packets.append([[2]])
    packets.append([[6]])

    # how to sort according to comparison?
    # fround this from Andrew Dalke: https://docs.python.org/3/howto/sorting.html#comparison-functions
    # try functools cmp_to_key
    rslt2 = 1
    for i, itm in enumerate(sorted(packets, key=cmp_to_key(lambda l, r: check(l, r)), reverse=True), start=1):
        if itm in [[[2]], [[6]]]:
            rslt2 *= i
    print("Second result: ", rslt2)
