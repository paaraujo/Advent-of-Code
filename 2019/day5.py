from intcode import Intcode
    
def part1(input_instruction):
    with open('inputs/day5.txt') as f:
        seq = f.read().rstrip('\n').split(',')
        computer = Intcode()
        computer.initialize_memory(seq)
        computer.set_pointer(0)
        computer.test(input_instruction)

def part2(input_instruction):
    output = -1
    with open('inputs/day5.txt') as f:
        seq = f.read().rstrip('\n').split(',')
        computer = Intcode()
        computer.initialize_memory(seq)
        computer.set_pointer(0)
        output = computer.calculate(input_instruction)
    return output[-1]

part1(1)
print(part2(5))