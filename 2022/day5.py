def part1():
    with open('inputs/day5.txt') as f:
        total = 0
        # Reading first part of the input to get the snapshot
        snapshot = []
        line = f.readline()
        while line != '\n':
            snapshot.append(line)
            line = f.readline()

        # Getting indexes where letters are placed
        snapshot = snapshot[::-1]
        idx = {}
        count = 1
        for i, c in enumerate(snapshot[0].rstrip()):
            if c != ' ':
                idx[count] = i
                count += 1

        # Building depot
        depot = {}
        for i in range(1,len(idx)+1):
            depot[i] = []

        for i in range(1,len(snapshot)):
            for key, val in idx.items():
                l = snapshot[i].rstrip()
                try:
                    c = l[val]
                    if c.isalpha():
                        depot[key].append(c)
                except:
                    pass

        # Organizing the depot
        lines = f.readlines()
        lines = [line.rstrip('\n').split() for line in lines]
        for line in lines:
            qtd = int(line[1])
            orig = int(line[3])
            dest = int(line[5])
            for i in range(qtd):
                depot[dest].append(depot[orig].pop())

        # Building message
        message = ''
        for key in idx.keys():
            message += depot[key][-1]

        return message


def part2():
    with open('inputs/day5.txt') as f:
        total = 0
        # Reading first part of the input to get the snapshot
        snapshot = []
        line = f.readline()
        while line != '\n':
            snapshot.append(line)
            line = f.readline()

        # Getting indexes where letters are placed
        snapshot = snapshot[::-1]
        idx = {}
        count = 1
        for i, c in enumerate(snapshot[0].rstrip()):
            if c != ' ':
                idx[count] = i
                count += 1

        # Building depot
        depot = {}
        for i in range(1,len(idx)+1):
            depot[i] = []

        for i in range(1,len(snapshot)):
            for key, val in idx.items():
                l = snapshot[i].rstrip()
                try:
                    c = l[val]
                    if c.isalpha():
                        depot[key].append(c)
                except:
                    pass

        # Organizing the depot
        lines = f.readlines()
        lines = [line.rstrip('\n').split() for line in lines]
        for line in lines:
            qtd = int(line[1])
            orig = int(line[3])
            dest = int(line[5])
            if qtd == 1:
                depot[dest].append(depot[orig].pop())
            else:
                temp = []
                for i in range(qtd):
                    temp.append(depot[orig].pop())
                temp = temp[::-1]
                depot[dest] += temp

        # Building message
        message = ''
        for key in idx.keys():
            message += depot[key][-1]

        return message


print(part1())
print(part2())
