#! /usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Monkey(object):
    def __init__(self, items, operation, test, iftrue, iffalse):
        self.items = items
        self.operation = operation.strip()
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
    
    def cycle(self, modulo: int = None):
        for old in self.items:
            new =  eval(self.operation)                
            if modulo:
                new %= modulo
            else:
                new = int(new / 3)
            if new % self.test == 0:
                yield new, self.iftrue
            else:
                yield new, self.iffalse
        self.items = []
    
    def receive(self, item):
        self.items.append(item)


def parse():
    monkeys = {}
    groups = open('inputs/11.txt', 'r').read().split('\n\n')
    for i, grp in enumerate(groups):
        lines = grp.split('\n')
        items = [int(v) for v in lines[1].split(': ')[1].split(', ')]
        ops = lines[2].split(' = ')[1]
        tst = int(lines[3].split(' ')[-1])
        tru = int(lines[4].split(' ')[-1])
        fls = int(lines[5].split(' ')[-1])
        monkeys[i] = Monkey(items, ops, tst, tru, fls)
    return monkeys


def get_modulo_divider(l: list = None):
    rslt = 1
    if l:
        for v in l:
            rslt = rslt * (rslt*v)
    return rslt


def iterate(monkeys, counter, modulo=None):
    for i, m1 in monkeys.items():
        for v, m2 in m1.cycle(modulo=modulo):
            monkeys[m2].receive(v)
            counter[i] += 1

if __name__ == '__main__':
    mkcnt1 = defaultdict(int)
    mks1 = parse()
    for _ in range(20):
        iterate(mks1, mkcnt1)
    vals = sorted(mkcnt1.values())
    print("First result: ", vals[-1] * vals[-2])
    
    mkcnt2 = defaultdict(int)
    mks2 = parse()
    modulo = get_modulo_divider([m.test for m in mks1.values()])
    for _ in range(10000):
        iterate(mks2, mkcnt2, modulo=modulo)
    vals = sorted(mkcnt2.values())
    print("Second result: ", vals[-1] * vals[-2])
    