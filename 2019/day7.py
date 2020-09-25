from itertools import permutations
from intcode import Amplifier

def part1(input_instruction):
    with open('inputs/day7.txt') as f:
        seqS = f.read().rstrip('\n').split(',')
        phases = [0,1,2,3,4]
        all_phases = list(permutations(phases,5))
        # amplifiers
        A = Amplifier(seqS)
        B = Amplifier(seqS)
        C = Amplifier(seqS)
        D = Amplifier(seqS)
        E = Amplifier(seqS)
        # thrusters list
        thrusters = []
        for p in all_phases:
            # initiating system
            A.reset(); B.reset(); C.reset(); D.reset(); E.reset()
            a = A.run([p[0],input_instruction])
            b = B.run([p[1],a])
            c = C.run([p[2],b])
            d = D.run([p[3],c])
            e = E.run([p[4],d])
            thrusters.append(e)    
    return max(thrusters)

def part2(input_instruction):
    with open('inputs/day7.txt') as f:
        seqS = f.read().rstrip('\n').split(',')
        phases = [5,6,7,8,9]
        all_phases = list(permutations(phases,5))
        # amplifiers
        A = Amplifier(seqS)
        B = Amplifier(seqS)
        C = Amplifier(seqS)
        D = Amplifier(seqS)
        E = Amplifier(seqS)
        # thrusters list
        thrusters = []
        for p in all_phases:
            # initiating system with all phases
            A.reset(); B.reset(); C.reset(); D.reset(); E.reset()
            a = A.run([p[0],input_instruction])
            b = B.run([p[1],a])
            c = C.run([p[2],b])
            d = D.run([p[3],c])
            e = E.run([p[4],d])
            # feedback looping until all amplifiers get done
            while True:
                a = A.run([e])
                b = B.run([a])
                c = C.run([b])
                d = D.run([c])
                e = E.run([d])
                if A.pointer == -1 and \
                   B.pointer == -1 and \
                   C.pointer == -1 and \
                   D.pointer == -1 and \
                   E.pointer == -1:
                       thrusters.append(e)
                       break
    return max(thrusters)

print(part1(0))
print(part2(0))