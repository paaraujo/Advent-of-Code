def part1():
    with open('inputs/day1.txt') as f:
        # Reading lines
        lines = [line.rstrip('\n') for line in f]
        # Splitting the calories
        elves = []
        elf = 0
        for line in lines:
            if line == '':
                elves.append(elf)
                elf = 0.
            else:
                elf += int(line)
        # Finding the elf with more calories
        m = max(elves)
        idx = elves.index(m)
        return idx, m


def part2():
    with open('inputs/day1.txt') as f:
        # Reading lines
        lines = [line.rstrip('\n') for line in f]
        # Splitting the calories
        elves = []
        elf = 0
        for line in lines:
            if line == '':
                elves.append(elf)
                elf = 0.
            else:
                elf += int(line)
        # Finding the top three with more calories
        elves.sort(reverse=True)
        return sum(elves[:3])


print(part1())
print(part2())
