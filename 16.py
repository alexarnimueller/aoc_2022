#! /usr/bin/env python

import re
import numpy as np

def read_file(filename):
    valves, tunnels = {}, {}
    for line in open(f'inputs/{filename}', 'r').readlines():
        m = re.search(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (\w+(?:, \w+)*)', line)
        valve, flow_rate, vaves = m.groups()
        tunnels[valve] = [t.strip() for t in vaves.split(', ')]
        valves[valve] = int(flow_rate)
    return valves, tunnels

def build_graph(tunnels):
    m = np.zeros(len(tunnels), dtype=int)
    for i, (v, neighbors) in enumerate(tunnels):
        for n in neighbors:
            pass
   