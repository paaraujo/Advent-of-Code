import re


def part1():
    with open('inputs/day2.txt') as f:
        l = [line.rstrip('\n') for line in f]
        valids = 0
        for s in l:
            match = re.match('(\d+)-(\d+) (\w)', s)
            if match:
                lower, upper, letter = match.groups()
                count = re.findall(letter, s)
                if int(lower) <= (len(count) - 1) <= int(upper):
                    valids += 1
    return valids


def part2():
    with open('inputs/day2.txt') as f:
        l = [line.rstrip('\n') for line in f]
        valids = 0
        for s in l:
            match = re.match('(\d+)-(\d+) (\w): (\w+)', s)
            if match:
                pos1, pos2, letter, seq = match.groups()
                if (seq[int(pos1) - 1] == letter and seq[int(pos2) - 1] != letter) \
                        or (seq[int(pos2) - 1] == letter and seq[int(pos1) - 1] != letter):
                    valids += 1
    return valids


print(part1())
print(part2())
