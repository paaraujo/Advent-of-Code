def part1(noun,verb):
    with open('inputs/day2.txt') as f:
        seq = f.read()
        seq = list(map(int,seq.split(',')))
        # initialization
        seq[1] = noun
        seq[2] = verb
        for i in range(0, len(seq),4):
            if seq[i] != 99:
                if seq[i] == 1:
                    # addition
                    seq[seq[i+3]] = seq[seq[i+1]] + seq[seq[i+2]]
                else:
                    # multiplication
                    seq[seq[i+3]] = seq[seq[i+1]] * seq[seq[i+2]]
            else:
                break
    return seq[0]

def part2():
    for n in range(0, 100):
        for v in range(0,100):
            if part1(n,v) == 19690720:
                return 100 * n + v

print(part1(12,2))
print(part2())