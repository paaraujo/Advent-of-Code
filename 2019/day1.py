from math import floor

def part1():
    with open('inputs/day1.txt') as f:
        l = [floor(int(line.rstrip('\n'))/3)-2 for line in f]
    return sum(l)

def moduleFuel(f):
    m = []
    n = floor(f/3)-2
    while n > 0: 
        m.append(n)
        n = floor(n/3)-2
    return sum(m)

def part2():
    with open('inputs/day1.txt') as f:
        l = [moduleFuel(int(line.rstrip('\n'))) for line in f]
    return sum(l)

print(part1())
print(part2())