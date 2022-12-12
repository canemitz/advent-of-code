import re
import json

def part1(puzzle_input):
    print('Q: What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?')
    monkeys = puzzle_input

    num_rounds = 20
    for round_i in range(num_rounds):
        for monkey_i in range(len(monkeys)):
            monkeys = inspect_and_throw_items(monkey_i, monkeys)

    monkey_inspections = [ monkey['num_inspections'] for monkey in monkeys ]
    monkey_inspections.sort()
    monkey_business_level = monkey_inspections.pop() * monkey_inspections.pop()

    ans = monkey_business_level

    print(f'A: {ans}')


def inspect_and_throw_items(monkey_i, monkeys):
    """Track worry level as monkey inspects, gets bored, and throws its items. Track how many items this monkey inspects."""
    monkey = monkeys[monkey_i]

    try:
        monkey['num_inspections'] += len(monkey['items'])
    except:
        monkey['num_inspections'] = len(monkey['items'])

    while monkey['items']:
        item = int( monkey['items'].pop(0) )
        item = inspect_item(item, monkey['operator'], monkey['operand'])
        item = monkey_gets_bored(item)

        if test_item(item, monkey['test']):
            receiving_monkey = monkey['if_true']
        else:
            receiving_monkey = monkey['if_false']

        monkeys = throw_to_monkey(item, receiving_monkey, monkeys)

    return monkeys


def inspect_item(worry_level, operator, operand):
    """Modify worry level of an item based on the operations of a monkey"""
    if operand == 'old':
        operand = worry_level

    operand = int(operand)
    if operator == '*':
        worry_level *= operand
    elif operator == '/':
        worry_level /= operand
    elif operator == '+':
        worry_level += operand
    elif operator == '-':
        worry_level -= operand

    return int(worry_level)


def monkey_gets_bored(worry_level):
    """Worry level goes down by a factor of 3 when a monkey gets bored."""
    return int(worry_level / 3);


def test_item(item, test):
    """Return true if item is divisible by test."""
    return item % int(test) == 0


def throw_to_monkey(item, receiving_monkey, monkeys):
    """Add item to the end of the receiving monkey's items."""
    monkeys[receiving_monkey]['items'].append(item)
    return monkeys


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')


def parse_input(input_file_obj):
    """Given the input, return an array of dictionaries, one for each monkey."""
    puzzle_input = []

    digit_regex     = re.compile(r'(\d+)')
    operation_regex = re.compile(r'new = old (.) (old|\d+)')

    monkeys = input_file_obj.read().strip().split('\n\n')
    for monkey in monkeys:
        monkey = monkey.split('\n')

        # ex) Monkey 0:
        _ = monkey.pop(0)

        #   Starting items: 79, 98
        # items = [79, 98]
        items = digit_regex.findall(monkey.pop(0))
        items = [int(item) for item in items]

        # ex)   Operation: new = old * 19
        # operator = '*'
        # operand = 19
        operation_match = operation_regex.search(monkey.pop(0))
        operator = operation_match.group(1)
        operand  = operation_match.group(2)
        try:
            operand = int(operand)
        except:
            # operand can be 'old'
            pass

        # ex)   Test: divisible by 23
        # test = 23
        test = digit_regex.findall(monkey.pop(0))[0]
        test = int(test)

        # ex)     If true: throw to monkey 2
        # if_true = 2
        if_true = digit_regex.findall(monkey.pop(0))[0]
        if_true = int(if_true)

        # ex)     If false: throw to monkey 3
        # if_false = 3
        if_false = digit_regex.findall(monkey.pop(0))[0]
        if_false = int(if_false)

        puzzle_input.append({
            'items'   : items,
            'operator': operator,
            'operand' : operand,
            'test'    : test,
            'if_true' : if_true,
            'if_false': if_false
        })

    return puzzle_input