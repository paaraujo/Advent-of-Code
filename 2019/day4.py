# import re

puzzle_input = '240298-784956'
puzzle_input = puzzle_input.split('-')
lowerBound   = int(puzzle_input[0])
upperbound   = int(puzzle_input[1])

def never_decrease(number):
    ok = True
    for i in range(1,len(number)):
        if number[i] < number[i-1]:
            ok = False
            break
    return ok

def just_two(number):
    number = list(number)
    unique = set(number)
    counting = []
    for u in unique:
        counting.append(number.count(u))
    return any((i==2 for i in counting))  

def part1():
    allNumbers = [str(i) for i in range(lowerBound,upperbound)]
    options = [i for i in allNumbers if never_decrease(i)]
    options = [i for i in options if len(i)>len(set(i))] # [i for i in options if len(re.findall(r"([0-9])\1",i))]
    return len(options)

def part2():
    allNumbers = [str(i) for i in range(lowerBound,upperbound)]
    options = [i for i in allNumbers if never_decrease(i)]
    options = [i for i in options if just_two(i)]
    return len(options)

print(part1())
print(part2())