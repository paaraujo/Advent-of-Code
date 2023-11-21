from collections import defaultdict


dirs = defaultdict(list)
sizes = defaultdict(int)

def part1():
    dirs_seq = ['/']
    with open('inputs/day7.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            if line[0] == '$':
                if line[1] == 'cd':
                    if line[2] == '..':
                        dirs_seq.pop(-1)
                    elif line[2] == '/':
                        dirs_seq.clear()
                        dirs_seq.append('/')
                    else:
                        dirs[dirs_seq[-1]].append(line[2])
                        dirs_seq.append(line[2])
            elif line[0] != 'dir':
                for i, _ in enumerate(dirs_seq):
                    key = '/'.join(dirs_seq[0:i+1])
                    sizes[key[1:] if len(key) > 1 else key] += int(line[0])
    total = 0
    filtered_dirs = defaultdict(int)
    for dir, size in sizes.items():
        if size <= 100000:
            total += size
            filtered_dirs[dir] = size

    return total


def part2():
    total_space = 70000000
    space_required = 30000000
    space_available = total_space - sizes['/'] 
    space_needed = space_required - space_available
    filtered_dirs = defaultdict(int)
    for dir, size in sizes.items():
        if size >= space_needed:
            filtered_dirs[dir] = size
    filtered_dirs = dict(sorted(filtered_dirs.items(), key=lambda item: item[1]))
    return next(iter(filtered_dirs.items()))


print(part1())
print(part2())
