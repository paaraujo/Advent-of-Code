import numpy as np
import matplotlib.pyplot as plt


# Getting commands
with open('inputs/day10.txt') as f:
    commands = f.readlines()
    commands = [list(line.strip().split()) for line in commands ]
    for i, command in enumerate(commands):
        if len(command) > 1:
            c,v = command
        else:
            c = command[0]
            v = 0
        commands[i] = [c,int(v)]


def check_cycle(cycles):
    return cycles in [20, 60, 100, 140, 180, 220]


def part1():
    global commands
    cycles = 1
    register = 1
    scores = []
    for c,v in commands:
        cycles += 1
        if check_cycle(cycles):
            scores.append(cycles*register)
        if c == 'addx':
            cycles += 1
            register += v
            if check_cycle(cycles):
                scores.append(cycles*register)
    return sum(scores), scores


def check_sprite_update_screen(sprite, counter, row, screen):
    if sprite[counter] == 1:
        screen[row,counter] = 1
    else:
        screen[row,counter] = 0
    return screen


def move_sprite(register):
    sprite = np.zeros(40, dtype=np.uint8)
    sprite[register-1 : register + 2] = 1
    return sprite


def check_row(counter):
    return counter == 40


def init_sprite():
    sprite = np.zeros(40, dtype=np.uint8)
    sprite[:3] = [1,1,1]
    return sprite


def check_screen(screen):
    plt.imshow(screen)
    plt.show()
    return None


def part2():
    global commands
    screen = np.zeros((6,40), dtype=np.uint8)
    row = 0
    counter = 0
    register = 1
    sprite = init_sprite()
    # Looping the commands
    for c,v in commands:
        screen = check_sprite_update_screen(sprite, counter, row, screen)
        counter += 1
        if check_row(counter):
            row += 1
            counter = 0
            sprite = init_sprite()
        if c == 'addx':
            screen = check_sprite_update_screen(sprite, counter, row, screen)
            counter += 1
            register += v
            sprite = move_sprite(register)
            if check_row(counter):
                row += 1
                counter = 0
                sprite = init_sprite()
    # Plotting results
    check_screen(screen)
    return None


print(part1())
print(part2())