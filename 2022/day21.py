def part1(puzzle_input):
    print('Q: What number will the monkey named root yell?')

    global monkeys
    monkeys = puzzle_input

    ans = monkey_yells('root')

    print(f'A: {ans}')


def monkey_yells(name):
    global monkeys

    job = monkeys[name]
    if type(job) is int:
        this_monkey_yells = job
    else:
        monkey_a, operator, monkey_b = job.split()
        this_monkey_yells = eval(f'{monkey_yells(monkey_a)} {operator} {monkey_yells(monkey_b)}')
        this_monkey_yells = int(this_monkey_yells)

    monkeys[name] = this_monkey_yells

    return this_monkey_yells


def part2(puzzle_input):
    print('Q:')



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