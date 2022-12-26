def part1():
    with open('inputs/day6.txt') as f:
        lower = 0
        upper = 4
        code = f.readline().rstrip()
        seq = code[lower:upper]
        while upper < len(code):
            s = set(seq)
            if len(s) == 4:
                break
            else:
                upper += 1
                lower += 1
                seq = code[lower:upper]

        return upper


def part2():
    with open('inputs/day6.txt') as f:
        lower = 0
        upper = 14
        code = f.readline().rstrip()
        seq = code[lower:upper]
        while upper < len(code):
            s = set(seq)
            if len(s) == 14:
                break
            else:
                upper += 1
                lower += 1
                seq = code[lower:upper]

        return upper


print(part1())
print(part2())
