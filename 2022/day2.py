def part1():
    with open('inputs/day2.txt') as f:
        # Reading lines
        lines = [line.rstrip('\n') for line in f]
        points = 0
        for line in lines:
            P1,P2 = line.split()
            # Initial points
            if P2 == 'X':
                points += 1
            elif P2 == 'Y':
                points += 2
            elif P2 == 'Z':
                points += 3
            # draw
            if P1 == 'A' and P2 == 'X' or \
                P1 == 'B' and P2 == 'Y' or \
                P1 == 'C' and P2 == 'Z':
                points += 3
            # lost
            elif P1 == 'A' and P2 == 'Z' or \
                P1 == 'B' and P2 == 'X' or \
                P1 == 'C' and P2 == 'Y':
                points += 0
            # win
            else:
                points += 6
        return points


def part2():
    with open('inputs/day2.txt') as f:
        # Reading lines
        lines = [line.rstrip('\n') for line in f]
        points = 0
        for line in lines:
            P1, P2 = line.split()
            # lost
            if P2 == 'X':
                points += 0
                if P1 == 'A':
                    points += 3
                elif P1 == 'B':
                    points += 1
                elif P1 == 'C':
                    points += 2
            # draw
            elif P2 == 'Y':
                points += 3
                if P1 == 'A':
                    points += 1
                elif P1 == 'B':
                    points += 2
                elif P1 == 'C':
                    points += 3
            # win
            elif P2 == 'Z':
                points += 6
                if P1 == 'A':
                    points += 2
                elif P1 == 'B':
                    points += 3
                elif P1 == 'C':
                    points += 1
        return points


print(part1())
print(part2())
