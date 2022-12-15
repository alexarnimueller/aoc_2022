#! /usr/bin/env python

def read_file(filename):
    sensor, beacon = set(), set()
    for line in open(f'inputs/{filename}', 'r').readlines():
        s, b = line.replace('Sensor at ', '').replace(' closest beacon is at ', '').split(':')
        sx, sy = int(s.split(', ')[0][2:]), int(s.split(', ')[1][2:])
        bx, by = int(b.split(', ')[0][2:]), int(b.split(', ')[1][2:])
        d = abs(sy - by) + abs(sx - bx)  # manhattan distance
        sensor.add((sx, sy, d))  # keep triple for easy access to distance
        beacon.add((bx, by))
    return sensor, beacon


def part_one():
    s, b = read_file("15.txt")
    rslt1 = 0
    limit = 10000000
    y = int(2000000)
    for x in range(-limit, limit):
        for (sx, sy, d) in s:
            if abs(x - sx) + abs(y - sy) <= d and (x, y) not in b:
                rslt1 += 1
                break
    print("First result: ", rslt1)
    

def part_two():
    s, b = read_file("15.txt")
    limit = 4000000
    moves = [[1, 1],[-1, 1], [1, -1], [-1, -1]]
    for (sx, sy, d) in s:
        for dx in range(d + 2):
            dy = d - dx + 1
            for deltax, deltay in moves:
                x = dx * deltax + sx
                y = dy * deltay + sy
                if (0 <= x <= limit and  # within limits
                    0 <= y <= limit and  # within limits
                    (x, y) not in b and  # no beacon
                    abs(x - sx) + abs(y - sy) - 1 == d): # distance + 1
                        # check if closer to any other sensor
                        if all([abs(x - xx) + abs(y - yy) > d for (xx, yy, d) in s]):                       
                            return x * limit + y
                        
if __name__ == '__main__':
    print("Running part one...")
    part_one()
    print("Running part two...")
    print("Second result: ", part_two())
