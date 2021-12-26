import statistics as stat

def part1(input_data):
    print('Q: Determine the horizontal position that the crabs can align to using the least fuel possible.')
    print('   How much fuel must they spend to align to that position?')

    crabs = get_crabs_list(input_data)
    ans = calculate_fuel_cost(crabs, stat.median(crabs))

    print(f'A: {ans}')


def get_crabs_list(input_data):
    crabs_list = [int(x) for x in input_data.readline().split(',')]
    return crabs_list


def calculate_fuel_cost(crabs, goal_position, weighted=False):
    fuel_cost = 0

    for crab in crabs:
        position_diff = int(abs(crab - goal_position))

        if weighted:
            fuel_cost += sum(range(position_diff+1))
        else:
            fuel_cost += position_diff

    return fuel_cost


def part2(input_data):
    print('Q: Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route!')
    print('   How much fuel must they spend to align to that position?')

    crabs = get_crabs_list(input_data)

    fuel_costs = []
    for goal_position in range(len(crabs)):
        fuel_costs.append(calculate_fuel_cost(crabs, goal_position, True))

    ans = min(fuel_costs)

    print(f'A: {ans}')