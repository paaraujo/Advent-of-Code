from collections import defaultdict
from math import atan2,pi,sqrt

class Asteroid():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ecldst = 0
        self.id = None
        
def map_visible(origin):
    temp = defaultdict(list)
    x1 = origin.x
    y1 = origin.y
    # mapping all surrounding asteroids
    for k in asteroids:
        if origin.id == k:
            continue
        x2 = asteroids[k].x
        y2 = asteroids[k].y
        deltaX = x2-x1
        deltaY = y1-y2 # inverted because y is always in the negative quadrant
        ang = atan2(deltaY,deltaX)
        a = Asteroid()
        a.x = x2
        a.y = y2
        a.ecldst = sqrt(deltaX**2 + deltaY**2)
        a.id = k
        temp[ang].append(a)
    # ordering aligned asteroids based on their distance from the origin
    for ang in temp:
        temp[ang].sort(key=lambda a: a.ecldst)
    return temp

def part1():
    global asteroids, best_asteroid
    with open('inputs/day10.txt') as f:
        # getting all asteroids in the input puzzle
        asteroids = defaultdict(Asteroid)
        idx = 0
        for y,line in enumerate(f):
            line = line.rstrip('\n')
            for x,c in enumerate(line):
                if c == "#":
                    a = Asteroid()
                    a.x = x
                    a.y = y
                    a.id = idx
                    asteroids[idx] = a
                    idx += 1
        # couting all detectable asteroids from a particular asteroid
        mapping = defaultdict(int)
        for k in asteroids:
            mapping[k] += len(map_visible(asteroids[k]))
        # getting the best asteroid
        best_id, detections = max(mapping.items(),key=lambda i: i[1])
        best_asteroid = asteroids[best_id]
    return (best_asteroid.x, best_asteroid.y), detections

def part2():
    t = map_visible(best_asteroid)
    # ordering keys to start from pi/2
    o = sorted(t.keys(),reverse=True)
    # finding the key "neareast" to pi/2  
    for k in o:
        if k <= pi/2:
            break
    # building sequence of rotation
    seq  = [i for i in range(o.index(k),len(t))]
    seq += [i for i in range(0,o.index(k))]
    # initializing vaporization
    count = 0
    vaporized = None
    done = False
    while not done:
        for i in seq:
            if len(t[o[i]]):
                vaporized = t[o[i]].pop(0)
                count += 1
            if count == 200: # sequence control
                done = True
                break
    return vaporized.x*100 + vaporized.y

print(part1())
print(part2())