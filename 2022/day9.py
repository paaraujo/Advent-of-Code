
from collections import defaultdict


# Getting commands
with open('inputs/day9.txt') as f:
    commands = f.readlines()
    commands = [list(line.strip().split()) for line in commands ]
    commands = [[d,int(n)] for d,n in commands ]


def check_adjacency(pos_H, pos_T):
    # Creating possibilities
    P = [[pos_T[0]+1,pos_T[1]+1],
         [pos_T[0]+1,pos_T[1]],
         [pos_T[0]+1,pos_T[1]-1],
         [pos_T[0],pos_T[1]-1],
         [pos_T[0]-1,pos_T[1]-1],
         [pos_T[0]-1,pos_T[1]],
         [pos_T[0]-1,pos_T[1]+1],
         [pos_T[0],pos_T[1]+1],
         [pos_T[0],pos_T[1]],  # Tail and Head in the same position
    ]
    return pos_H in P


def move_H(pos_H, d):
    if d == 'R':
        pos_H[0] += 1
    elif d == 'L':
        pos_H[0] -= 1
    elif d == 'U':
        pos_H[1] += 1
    elif d == 'D':
        pos_H[1] -= 1
    return pos_H


def move_T(pos_H, pos_T, d):
    diff = [pos_H[0]-pos_T[0],pos_H[1]-pos_T[1]]
    temp = [pos_T[0], pos_T[1]]
    # Move T
    if diff[0] > 0:
        temp[0] += 1
    elif diff[0] < 0:
        temp[0] -= 1

    if diff[1] > 0:
        temp[1] += 1
    elif diff[1] < 0:
        temp[1] -= 1
    return temp


def part1():
    global commands

    # Preparing dictionary to hold visited places
    visited_H = defaultdict(int)
    visited_T = defaultdict(int)

    # Initializing nodes
    pos_H = [0, 0]
    pos_T = [0, 0]
    visited_H[str(pos_H)] += 1
    visited_T[str(pos_T)] += 1

    # Moving nots
    for d, n in commands:
        for _ in range(n):
            pos_H = move_H(pos_H, d)
            visited_H[str(pos_H)] += 1
            # Check adjencency
            is_adjacent = check_adjacency(pos_H=pos_H, pos_T=pos_T)
            if not is_adjacent:
                pos_T = move_T(pos_H, pos_T, d)
                visited_T[str(pos_T)] += 1

    return len(visited_T)


def part2():
    global commands
    # Preparing dictionary to hold visited places
    num_tails = 9
    visited_H = defaultdict(int)
    visited_T = [defaultdict(int) for _ in range(num_tails)]

    # Initializing nodes
    pos_H = [0, 0]
    pos_T = [[0, 0] for _ in range(num_tails)]
    visited_H[str(pos_H)] += 1
    for tail in visited_T:
        tail[str(pos_H)] += 1
    
    # Moving nots
    for d, n in commands:       
        for _ in range(n):
            pos_H = move_H(pos_H, d)
            visited_H[str(pos_H)] += 1
            unified = [pos_H] + pos_T
            for i in range(num_tails):
                # Check adjencency
                is_adjacent = check_adjacency(pos_H=unified[i], pos_T=unified[i+1])
                if not is_adjacent:
                    unified[i+1] = move_T(unified[i], unified[i+1], d)
                    visited_T[i][str(unified[i+1])] += 1
            pos_T = unified[1:]
    return len(visited_T[-1])


print(part1())
print(part2())
