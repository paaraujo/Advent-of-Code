from intcode import Intcode
    
def part1(input_instruction):
    with open('inputs/day5.txt') as f:
        seqS = f.read().rstrip('\n').split(',')
        computer = Intcode()
        computer.test(seqS,input_instruction)

def part2(input_instruction):
    output = -1
    with open('inputs/day5.txt') as f:
        seqS = f.read().rstrip('\n').split(',')
        computer = Intcode()
        _,_,output = computer.calculate(seqS,input_instruction,0)
    return output

part1([1])
print(part2([5]))