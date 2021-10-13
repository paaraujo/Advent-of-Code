import math


def part1():
    with open('inputs/day3.txt') as f:
        forest = [list(line.rstrip('\n')) for line in f]
        rows = len(forest)
        cols = len(forest[0])
        row = 0
        col = 1
        right = 3
        down = 1
        trees = 0
        while True:
            if col + right > cols:
                col = ((col + right) - cols)
            else:
                col += right
            if row < rows - down:
                row += down
            else:
                break
            element = forest[row][col - 1]
            if element == '#':
                trees += 1

    return trees


def part2():
    with open('inputs/day3.txt') as f:
        forest = [list(line.rstrip('\n')) for line in f]
        rows = len(forest)
        cols = len(forest[0])
        row = 0
        col = 1
        trees = 0
        slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        result = []
        for right, down in slopes:
            while True:
                if col + right > cols:
                    col = ((col + right) - cols)
                else:
                    col += right
                if row < rows - down:
                    row += down
                else:
                    break
                element = forest[row][col - 1]
                if element == '#':
                    trees += 1
            result.append(trees)
            col = 1
            row = 0
            trees = 0

    return math.prod(result)


print(part1())
print(part2())
