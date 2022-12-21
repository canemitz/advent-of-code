import re
from sympy import simplify, solve


def part1(puzzle_input):
    print('Q: What number will the monkey named root yell?')

    global monkeys
    monkeys = puzzle_input

    ans = monkey_yells('root')

    print(f'A: {ans}')


def monkey_yells(name):
    """Update global monkeys dictionary with integer value or symbolic expression of what the monkey yells."""
    global monkeys

    # If a monkey doesn't have a job, just return the monkey's name (only used for 'humn')
    try:
        job = monkeys[name]
    except:
        return name

    if type(job) is int:
        this_monkey_yells = job
    else:
        # Replace monkey names in this job with their current value or expression
        monkey_names = re.findall(r'[a-z]{4}', job)
        for name in monkey_names:
            job = job.replace(name, str(monkey_yells(name)))

        # Attempt to reduce the length of this expression
        try:
            this_monkey_yells = eval(job)
            this_monkey_yells = int(this_monkey_yells)
        except:
            this_monkey_yells = f'({simplify(job)})'

    monkeys[name] = this_monkey_yells

    return this_monkey_yells


def part2(puzzle_input):
    print("Q: What number do you yell to pass root's equality test?")

    global monkeys
    monkeys = puzzle_input
    del monkeys['humn']

    root_a, _, root_b = monkeys['root'].split()
    root_a_expr = monkey_yells(root_a)
    root_b_expr = monkey_yells(root_b)

    ans = solve( f'{root_a_expr} - {root_b_expr}' )[0]

    print(f'A: {ans}')


def parse_input(input_file_obj):
    """Put monkeys into a dictionary, and cast their job as an int if it is one."""
    puzzle_input = {}

    for line in input_file_obj.readlines():
        monkey_name, job = line.strip().split(': ')

        try:
            job = int(job)
        except:
            pass

        puzzle_input[monkey_name] = job

    return puzzle_input