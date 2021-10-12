def part1():
    with open('inputs/day1.txt') as f:
        l = [int(line.rstrip('\n')) for line in f]
        for i, n in enumerate(l):
            m: int
            for j, m in enumerate(l[i + 1:]):
                if n + m == 2020:
                    return n * m


def part2():
    with open('inputs/day1.txt') as f:
        l = [int(line.rstrip('\n')) for line in f]
        for i, n in enumerate(l):
            for j, m in enumerate(l[i + 1:]):
                if n + m < 2020:
                    for k, p in enumerate(l[j + 1:]):
                        if n + m + p == 2020:
                            return n * m * p


print(part1())
print(part2())
