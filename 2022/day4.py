def part1():
    with open('inputs/day4.txt') as f:
        # Reading lines
        lines = [line.rstrip('\n') for line in f]
        total = 0
        # Comparing groups
        for line in lines:
            # pair = []
            elf1, elf2 = line.split(',')
            elf1_i, elf1_e = elf1.split('-')
            elf2_i, elf2_e = elf2.split('-')
            elf1_i = int(elf1_i)
            elf1_e = int(elf1_e)
            elf2_i = int(elf2_i)
            elf2_e = int(elf2_e)
            # Checking overlap
            if (elf1_i >= elf2_i and elf1_e <= elf2_e) or \
                    (elf2_i >= elf1_i and elf2_e <= elf1_e):
                total += 1

        return total


def part2():
    with open('inputs/day4.txt') as f:
        # Reading lines
        lines = [line.rstrip('\n') for line in f]
        total = 0
        # Comparing groups
        for line in lines:
            elf1, elf2 = line.split(',')
            elf1_i, elf1_e = elf1.split('-')
            elf2_i, elf2_e = elf2.split('-')
            elf1_i = int(elf1_i)
            elf1_e = int(elf1_e)
            elf2_i = int(elf2_i)
            elf2_e = int(elf2_e)
            # Checking overlap
            if (elf1_i >= elf2_i and elf1_i <= elf2_e) or \
                    (elf2_i >= elf1_i and elf2_i <= elf1_e):
                total += 1

        return total


print(part1())
print(part2())
