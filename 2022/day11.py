
class Monkey:

    def __init__(self, id, items, operation, test_denominator, monkey_test_true, monkey_test_false) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test_denominator = test_denominator
        self.monkey_test_true = monkey_test_true
        self.monkey_test_false = monkey_test_false
        self.inspections = 0

    
    def throw_item(self, dest_monkey):
        dest_monkey.items.append(self.items.pop(0))
        return None
    

    def update_worry_level(self, reduce_worry_level, reduction_type, reduction):
        old = self.items[0]
        variables = {'old': old}
        self.items[0] = eval(self.operation, variables)
        if reduce_worry_level:
            if reduction_type == 'part1':
                self.items[0] = int(self.items[0] / reduction)
            elif reduction_type == 'part2':
                self.items[0] = self.items[0] % reduction
        return None
    

    def test_worry_level(self):
        return self.items[0] % self.test_denominator == 0
    

    def inspect(self, system, reduce_worry_level, reduction_type, reduction):
        while len(self.items):
            self.inspections += 1
            self.update_worry_level(reduce_worry_level, reduction_type, reduction)
            result = self.test_worry_level()
            if result:
                self.throw_item(system.monkeys[self.monkey_test_true])
            else:
                self.throw_item(system.monkeys[self.monkey_test_false])


class System:

    def __init__(self) -> None:
        self.monkeys = []
        # Identifying monkeys
        with open('inputs/day11.txt') as f:
            instructions = f.readlines()
            instructions = [line.strip() for line in instructions]
            for i in range(len(instructions)):
                line = instructions[i]
                if 'Monkey' in line:
                    # Getting Monkey id
                    id = int(line.replace(':','').split()[1])
                    # Getting items
                    i += 1
                    line = instructions[i]
                    line = line.replace('Starting items: ','').split(',')
                    items = [int(n) for n in line]
                    # Getting operation
                    i += 1
                    line = instructions[i]
                    operation = line.replace('Operation: new = ','')
                    # Getting test denominator
                    i += 1
                    line = instructions[i]
                    test_denominator = int(line.replace('Test: divisible by ',''))
                    # Getting monkey if true
                    i += 1
                    line = instructions[i]
                    monkey_test_true = int(line.replace('If true: throw to monkey ',''))
                    # Getting monkey if false
                    i += 1
                    line = instructions[i]
                    monkey_test_false = int(line.replace('If false: throw to monkey ',''))
                    # Creating Monkey
                    self.monkeys.append(
                        Monkey(
                            id=id, items=items, 
                            operation=operation, test_denominator=test_denominator, 
                            monkey_test_true=monkey_test_true, monkey_test_false=monkey_test_false
                        )
                    )
            self.monkeys = tuple(self.monkeys)

    
def part1():
    system = System()

    # Looping the rounds
    rounds = 20
    for _ in range(rounds):
        for monkey in system.monkeys:
            monkey.inspect(system, reduce_worry_level=True, reduction_type='part1', reduction=3)
    monkeys_sorted = sorted(system.monkeys, key=lambda m: m.inspections, reverse=True)
    monkey_business = monkeys_sorted[0].inspections * monkeys_sorted[1].inspections
    return [monkey.inspections for monkey in monkeys_sorted], monkey_business


def part2():
    system = System()

    # Computing the common reduction
    reduction = 1
    for monkey in system.monkeys:
        reduction *= monkey.test_denominator

    # Looping the rounds
    rounds = 10000
    for i in range(rounds):
        for monkey in system.monkeys:
            monkey.inspect(system, reduce_worry_level=True, reduction_type='part2', reduction=reduction)
        # Debugging the results
        if i+1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(f'\n== After round {i+1} ==')
            for monkey in system.monkeys:
                print(f'Monkey {monkey.id} inspected items {monkey.inspections} times.')

    monkeys_sorted = sorted(system.monkeys, key=lambda m: m.inspections, reverse=True)
    monkey_business = monkeys_sorted[0].inspections * monkeys_sorted[1].inspections
    return [monkey.inspections for monkey in monkeys_sorted], monkey_business


print(part1())
print(part2())
