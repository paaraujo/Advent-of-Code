class Path():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.locations = []
        
def part1():
    global intersections, pathWire1, pathWire2
    
    with open('inputs/day3.txt') as f:
        wire1 = list(f.readline().rstrip('\n').split(','))
        wire2 = list(f.readline().rstrip('\n').split(','))
        pathWire1 = Path()
        pathWire2 = Path() 

        # wire1 looping
        for p in wire1:
            d = p[:1]
            n = int(p[1:])
            for i in range(n):
                if d == 'R':
                    pathWire1.x += 1
                elif d == 'L':
                    pathWire1.x -= 1
                elif d == 'U':
                    pathWire1.y -= 1
                elif d == 'D':
                    pathWire1.y += 1
                pathWire1.locations.append((pathWire1.x,pathWire1.y))
                
        # wire2 looping
        for p in wire2:
            d = p[:1]
            n = int(p[1:])
            for i in range(n):
                if d == 'R':
                    pathWire2.x += 1
                elif d == 'L':
                    pathWire2.x -= 1
                elif d == 'U':
                    pathWire2.y -= 1
                elif d == 'D':
                    pathWire2.y += 1
                pathWire2.locations.append((pathWire2.x,pathWire2.y))
                
        # intersections
        uniqueLocWire1 = set(pathWire1.locations)
        uniqueLocWire2 = set(pathWire2.locations)
        if len(uniqueLocWire1) < len(uniqueLocWire2):
            intersections = uniqueLocWire1.intersection(uniqueLocWire2)
        else:
            intersections = uniqueLocWire2.intersection(uniqueLocWire1)
            
        # distance from the origin
        dist = [abs(p[0])+abs(p[1]) for p in intersections]

    return min(dist)

def part2():
    steps = []
    for i in intersections:
        steps.append(pathWire1.locations.index(i)+pathWire2.locations.index(i)+2) # index begins in 0; therefore sum 1 for each list
    
    return min(steps)

print(part1())
print(part2())