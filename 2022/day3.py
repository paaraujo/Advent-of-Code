def part1():
    with open('inputs/day3.txt') as f:
        # Reading lines
        lines = [line.rstrip('\n') for line in f]
        items = []
        total = 0
        # Comparing groups
        for line in lines:
            l = len(line)
            n = l // 2
            comp1 = line[:n]
            comp2 = line[n:]
            for item in comp1:
                if item in comp2:
                    items.append(item)
                    break

        # Converting chars to integers
        items  = [ord(i) for i in items]
        for i in items:
            # lower case
            if 97 <= i <= 122:
                total += (i - 97) + 1
            # upper case
            if 65 <= i <= 90:
                total += (i - 65) + 27

        return total


def part2():
    with open('inputs/day3.txt') as f:
        # Reading lines
        lines = [line.rstrip('\n') for line in f]
        items = []
        total = 0
        # Comparing groups
        for i in range(0, len(lines), 3):
            m1 = lines[i]
            m2 = lines[i+1]
            m3 = lines[i+2]
            for i in m1:
                if i in m2:
                    if i in m3:
                        items.append(i)
                        break

        # Converting chars to integers
        items  = [ord(i) for i in items]
        for i in items:
            # lower case
            if 97 <= i <= 122:
                total += (i - 97) + 1
            # upper case
            if 65 <= i <= 90:
                total += (i - 65) + 27

        return total


print(part1())
print(part2())
