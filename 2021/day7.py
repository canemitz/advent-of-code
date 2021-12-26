import statistics as stat

def part1(input_data):
    print('Q: Determine the horizontal position that the crabs can align to using the least fuel possible.')
    print('   How much fuel must they spend to align to that position?')

    crabs = [int(x) for x in input_data.readline().split(',')]

    ans = calculate_fuel_cost(crabs, stat.median(crabs))

    print(f'A: {ans}')


def calculate_fuel_cost(crabs, goal_position):
    fuel_cost = 0

    for crab in crabs:
        fuel_cost += int(abs(crab - goal_position))

    return fuel_cost


def part2(input_data):
    print('Q:')
    print(f'A: {ans}')