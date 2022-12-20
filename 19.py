#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Blueprint(object):
    def __init__(self, i: int, ore_robot_ore_cost: int, cly_robot_ore_cost: int, 
                 obs_robot_ore_cost: int, obs_robot_cly_cost: int, 
                 geo_robot_ore_cost: int, geo_robot_obs_cost: int) -> None:
        self.number = i
        self.ore_robot_ore_cost = ore_robot_ore_cost
        self.cly_robot_ore_cost = cly_robot_ore_cost
        self.obs_robot_ore_cost = obs_robot_ore_cost
        self.obs_robot_cly_cost = obs_robot_cly_cost
        self.geo_robot_ore_cost = geo_robot_ore_cost
        self.geo_robot_ore_cost = geo_robot_obs_cost
        self.minutes = 24
        self.ore_robots = 1
        self.cly_robots = 0
        self.obs_robots = 0
        self.geo_robots = 0
        self.ore = 0
        self.cly = 0
        self.obs = 0
        self.geo = 0

    def __repr__(self) -> str:
        return f"Blueprint {self.number}"

    def run(self) -> int:
        while self.minutes:
            new_ore_robot = 0
            new_cly_robot = 0
            new_obs_robot = 0
            new_geo_robot = 0

            if self.ore >= self.geo_robot_ore_cost and self.obs >= self.geo_robot_ore_cost:
                new_geo_robots = 1
                self.ore -= self.geo_robot_ore_cost 
                self.obs -= self.geo_robot_ore_cost                     

            elif self.ore >= self.obs_robot_ore_cost and self.cly >= self.obs_robot_cly_cost:
                new_obs_robots = 1
                self.ore -= self.obs_robot_ore_cost 
                self.cly -= self.obs_robot_cly_cost
 
            elif self.ore >= self.cly_robot_ore_cost:
                new_cly_robots = 1
                self.ore -= self.cly_robot_ore_cost
            
            elif self.ore >= self.ore_robot_ore_cost:
                new_ore_robot = 1
                self.ore -= self.ore_robot_ore_cost
            
            
            self.ore += self.ore_robots
            self.cly += self.cly_robots
            self.obs += self.obs_robots
            self.geo += self.geo_robots               
         
            self.ore_robots += new_ore_robot
            self.cly_robots += new_cly_robot
            self.obs_robots += new_obs_robot
            self.geo_robots += new_geo_robot
            
            self.minutes -= 1
            
        return self.geo * self.number


def read_input(filename):
    blueprints = []
    for line in open('inputs/'+filename, 'r').readlines():
        blueprints.append(Blueprint(*[int(x) for x in re.findall('\d+', line)]))
    return blueprints


blueprints = read_input('19.test')
print(sum(bp.run() for bp in blueprints))
for bp in blueprints:
    print(bp.__dict__)
