def part1(puzzle_input):
    print('Q: Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?')

    sum_of_priorities = 0
    for rucksack_items in puzzle_input:
        split_idx = int(len(rucksack_items) / 2)
        compartment_1 = set(rucksack_items[:split_idx])
        compartment_2 = set(rucksack_items[split_idx:])

        items_in_both = compartment_1.intersection(compartment_2)
        for item in items_in_both:
            sum_of_priorities += get_priority(item)

    ans = sum_of_priorities

    print(f'A: {ans}')


def get_priority(char):
    priority = ord(char)

    if char.isupper():
        priority -= 38
    else:
        priority -= 96

    return priority


def part2(puzzle_input):
    print('Q: Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?')

    sum_of_priorities = 0
    for i in range(0, len(puzzle_input), 3):
        rucksack_0 = set(puzzle_input[i])
        rucksack_1 = set(puzzle_input[i+1])
        rucksack_2 = set(puzzle_input[i+2])

        items_in_all_three = rucksack_0.intersection(rucksack_1, rucksack_2)
        for item in items_in_all_three:
            sum_of_priorities += get_priority(item)

    ans = sum_of_priorities

    print(f'A: {ans}')