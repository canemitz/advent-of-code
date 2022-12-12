import re
import json

def part1(puzzle_input, num_rounds=20):
    print(f'Q: What is the level of monkey business after {num_rounds} rounds of stuff-slinging simian shenanigans?')

    monkeys = puzzle_input

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
    """Reduce worry level of an item.

    Part 1: Worry level goes down by a factor of 3 when a monkey gets bored.

    Part 2, initial attempt (not shown):
            We don't need the actual worry level value, we just need to be able to determine whether any of the monkeys' tests pass.
            That is, "worry level mod test" must be zero or non-zero.
            We notice that if X is divisible by Y, then X - kY is also divisible by Y.
            So, to ensure we don't alter the outcome of any of the monkeys' tests, we can multiple their test values together.
            Then, we can subtract that value (repeatedly) from the worry level, and all test outcomes will be the same.
            This way, we don't have to maintain an incredibly large worry_level when we don't need to.
            ...this solution runs in 3s on the example input, but seems like it'll take hours on my actual input.

    Part 2, better attempt:
            Okay, the above logic is sound, but slow, since product_of_tests is still a very large number.
            We notice that if X % Y = 0, then (X % kY) % Y = 0.
            So, instead of subtracting that large product, we can do worry_level % product_of_tests and return a much smaller number.

    """
    global product_of_tests

    if running_part1():
        worry_level = int(worry_level / 3);
    else:
        worry_level = worry_level % product_of_tests

    return worry_level


def test_item(item, test):
    """Return true if item is divisible by test."""
    return item % int(test) == 0


def throw_to_monkey(item, receiving_monkey, monkeys):
    """Add item to the end of the receiving monkey's items."""
    monkeys[receiving_monkey]['items'].append(item)
    return monkeys


def part2(puzzle_input):
    print('Q: Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?')

    global part
    part = 2

    global product_of_tests
    product_of_tests = 1
    for monkey in puzzle_input:
        product_of_tests *= monkey['test']

    part1(puzzle_input, 10000)


def running_part1():
    """We define the global part in part2, but not part1, so we can test whether that variable is defined to determine which part we're running."""
    global part

    try:
        return part != 2
    except:
        return True


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