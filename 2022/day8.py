import numpy as np


with open('inputs/day8.txt') as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    lines = [list(map(int, line)) for line in lines]
    grid = np.array(lines, dtype=np.int8)


def check_visibility(row, column, grid):
    height = grid[row,column]
    up = np.sum(grid[:row+1,column] >= height)
    down = np.sum(grid[row:,column] >= height)
    left = np.sum(grid[row, :column+1] >= height)
    right = np.sum(grid[row, column:] >= height)
    if 1 in [up, down, left, right]:
        return True
    else:
        return False
    

def check_scenic_score(row, column, grid):
    height = grid[row,column]
    # Up-View
    up_score = 0
    up_view = grid[:row,column] >= height
    up_view = np.flip(up_view)
    for upper_tree in up_view:
        up_score += 1
        if upper_tree:
            break
    # Down-View
    down_score = 0
    down_view = grid[row+1:,column] >= height
    for lower_tree in down_view:
        down_score += 1
        if lower_tree:
            break
    # Left-View
    left_score = 0
    left_view = grid[row, :column] >= height
    left_view = np.flip(left_view)
    for left_tree in left_view:
        left_score += 1
        if left_tree:
            break
    # Right-View
    right_score = 0
    right_view = grid[row, column:] >= height
    for right_tree in right_view[1:]:
        right_score += 1
        if right_tree:
            break
    return up_score*down_score*right_score*left_score


def part1():
    global grid
    # Getting inner visible trees
    visible = 0
    for row in range(1,grid.shape[0]-1):
        for column in range(1,grid.shape[1]-1):
            if check_visibility(row, column, grid):
                visible += 1
    # Adding trees on the edges
    visible += grid.shape[0] * 2
    visible += (grid.shape[1]-2) * 2
    return visible


def part2():
    global grid
    highest = 0
    # Getting scenic score for all trees
    for row in range(1,grid.shape[0]-1):
        for column in range(1,grid.shape[1]-1):
            scenic_score = check_scenic_score(row, column, grid)
            if scenic_score > highest:
                highest = scenic_score
    return highest


print(part1())
print(part2())
