from collections import defaultdict,deque

def get_indirect_orbits(universe):
    ''' Backpropagate the universe counting the indirect orbits '''
    count = 0
    for planet in universe:
        isAround = universe[planet]
        while isAround != 'COM':
            count += 1
            isAround = universe[isAround]
    return count

def orbital_transfer(universe,visited,distances,orig,dest):
    ''' Based on BFS '''
    origin_planet = universe[orig][0]
    destin_planet = universe[dest][0]
    queue = deque()
    queue.append(origin_planet)
    visited[origin_planet] = True
    while len(queue):
        x = queue.popleft()
        for k in universe[x]:
            if visited[k]:
                continue
            distances[k] += distances[x] + 1
            queue.append(k)
            visited[k] = True
    return distances[destin_planet]

def part1():
    with open('inputs/day6.txt') as f:
        universe = defaultdict(str)
        for l in f:
            isAround,planet = l.rstrip('\n').split(')')
            universe[planet] = isAround
    return get_indirect_orbits(universe) + len(universe)

def part2(orig,dest):
    with open('inputs/day6.txt') as f:
        universe  = defaultdict(list)
        visited   = defaultdict(bool)
        distances = defaultdict(int)
        for l in f:
            isAround,planet = l.rstrip('\n').split(')')
            visited[planet] = False
            distances[planet] = 0
            universe[isAround].append(planet) # edge from-to
            universe[planet].append(isAround) # edge to-from
    return orbital_transfer(universe,visited,distances,orig,dest)

print(part1())
print(part2('YOU','SAN'))